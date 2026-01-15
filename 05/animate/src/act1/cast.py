from manim import *
from src.utils import *

def get_act1_cast():
    """
    Returns a dictionary of ALL cast members for Act 1.
    All objects are initialized in a default state.
    """
    cast = {}
    
    # --- 1. The Sentence Parts ---
    # "如果"(0,1) "天下雨"(2,3,4) "，"(5) "那么"(6,7) "地会湿"(8,9,10)
    part1 = create_text("如果", font_size=40).shift(LEFT*3)
    part_p = create_text("天下雨").next_to(part1, RIGHT)
    part_comma = create_text("，", font_size=40).next_to(part_p, RIGHT)
    part2 = create_text("那么", font_size=40).next_to(part_comma, RIGHT)
    part_q = create_text("地会湿").next_to(part2, RIGHT)
    
    # Store individual parts
    cast["text_if"] = part1
    cast["text_p"] = part_p
    cast["text_comma"] = part_comma
    cast["text_then"] = part2
    cast["text_q"] = part_q
    
    # Helper group for Scene 1 (optional, but Scene 1 treats them as one)
    # We can reconstruct VGroup in Scene 1 from these parts if needed, 
    # OR we can register "act1_full_sentence" as a VGroup of these.
    # Note: If we register both the group and children, state saving might be redundant but safe.
    # Actually, Scene 1 uses the Group. Scene 2 splits them.
    # Let's register logical parts mostly.
    
    # --- 2. Structural Elements (Arrows, Boxes, Labels) ---
    # Initialize them relative to the default positions of text_p/text_q
    # This ensures they have valid initial geometry.
    arrow = Arrow(LEFT, RIGHT, color=GOLD).set_fill(opacity=1)
    arrow.next_to(part_p, RIGHT) # Default pos
    
    box_p = SurroundingRectangle(part_p, color=BLUE, buff=0.2)
    box_q = SurroundingRectangle(part_q, color=BLUE, buff=0.2)
    
    label_p = Text("前件命题", font=DEFAULT_FONT, font_size=24).set_color(GREY).next_to(box_p, UP)
    label_q = Text("后件命题", font=DEFAULT_FONT, font_size=24).set_color(GREY).next_to(box_q, UP)
    label_rel = Text("蕴含", font=DEFAULT_FONT, font_size=24).set_color(GOLD).next_to(arrow, UP)
    
    cast["arrow"] = arrow
    cast["box_p"] = box_p
    cast["box_q"] = box_q
    cast["label_p"] = label_p
    cast["label_q"] = label_q
    cast["label_rel"] = label_rel
    
    # --- 3. Concept Map Elements (Scene 3 & 4) ---
    # Left Side: Sky/Rain
    # Aligned with text_p (approx x=-1.3)
    ALIGN_X_LEFT = LEFT * 1.3
    concept_sky = create_concept_node("天空", UP*1.5 + ALIGN_X_LEFT)
    concept_rain = create_concept_node("下雨", DOWN*1.5 + ALIGN_X_LEFT)
    line_left = DashedLine(concept_sky.get_bottom(), concept_rain.get_top(), color=BLUE_A)
    line_label_left = Text("(发生)", font=DEFAULT_FONT, font_size=20, color=WHITE).next_to(line_left, RIGHT)
    
    cast["concept_sky"] = concept_sky
    cast["concept_rain"] = concept_rain
    cast["line_left"] = line_left
    cast["line_label_left"] = line_label_left
    
    # Right Side: Ground/Wet
    concept_ground = create_concept_node("地面", UP*1.5)
    concept_wet = create_concept_node("湿", DOWN*1.5)
    line_right = DashedLine(concept_ground.get_bottom(), concept_wet.get_top(), color=BLUE_A)
    line_label_right = Text("(具有状态)", font=DEFAULT_FONT, font_size=20, color=WHITE).next_to(line_right, LEFT)
    
    cast["concept_ground"] = concept_ground
    cast["concept_wet"] = concept_wet
    cast["line_right"] = line_right
    cast["line_label_right"] = line_label_right
    
    return cast
