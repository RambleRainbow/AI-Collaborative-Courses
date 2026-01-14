import json
import re

CN_NUM = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6}

def parse_script_md(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Map: "act1_scene1" -> "full text..."
    scene_map = {}
    
    current_act_num = 0
    current_scene_num = 0
    current_lines = []
    
    # Act pattern: ## 第X幕
    act_pattern = re.compile(r'^##\s+第([一二三四五六])幕')
    # Scene pattern: ### **场景(\d+).*?**
    # Special: 场景6-8 -> treat as scene 6 (or special case)
    scene_pattern = re.compile(r'^###\s+\*\*场景(\d+).*?\*\*')
    scene_range_pattern = re.compile(r'^###\s+\*\*场景(\d+)[-~](\d+).*?\*\*')

    def save_current():
        nonlocal current_lines, current_act_num, current_scene_num
        if current_act_num > 0 and current_scene_num > 0 and current_lines:
            key = f"act{current_act_num}_scene{current_scene_num}"
            content = "".join(current_lines).strip()
            scene_map[key] = content
            
            # Special case handling for range mapping? 
            # If the json has act3_scene68, but script has Scene 6-8.
            # We'll handle exact scene match primarily.
        current_lines = []

    for line in lines:
        # Check Act
        act_match = act_pattern.match(line.strip())
        if act_match:
            save_current()
            current_act_num = CN_NUM.get(act_match.group(1), 0)
            current_scene_num = 0 # reset
            continue

        # Check Scene
        line_stripped = line.strip()
        
        # Try range first? No, single num is more common.
        scene_match = scene_pattern.match(line_stripped)
        range_match = scene_range_pattern.match(line_stripped)
        
        if range_match:
             save_current()
             # e.g. 6-8
             # We might need to know how the JSON keys are named.
             # JSON uses "act3_scene68" for "场景6-8"
             # Let's just save it as proper key?
             # Hack: if range 6-8, save as scene 68? or just 6?
             # Let's save as 'actX_scene68' if X=3?
             # Or more generically: act3_scene6
             start_n = range_match.group(1)
             end_n = range_match.group(2)
             current_scene_num = int(f"{start_n}{end_n}") # 68
             if current_act_num == 3 and start_n == '6':
                 current_scene_num = 68 # align with json convention found
        
        elif scene_match:
            save_current()
            current_scene_num = int(scene_match.group(1))
        
        else:
            if current_act_num > 0 and current_scene_num > 0:
                if not line.startswith('---'): # skip separators
                    current_lines.append(line)

    save_current()
    return scene_map

def update_json(json_file, script_map):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_count = 0
    for item in data:
        # Item id: act1_scene1
        # Extract parsing structure from ID
        # id is "actX_sceneY"
        
        # Simple lookup
        if item['id'] in script_map:
             item['desc'] = script_map[item['id']]
             updated_count += 1
        else:
             print(f"Warning: No script content for ID {item['id']}")

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"Updated {updated_count} scenes.")


if __name__ == "__main__":
    script_content = parse_script_md("script.md")
    # Debug: print keys found
    # print("Found scenes in script:", script_content.keys())
    
    update_json("scripts.json", script_content)
