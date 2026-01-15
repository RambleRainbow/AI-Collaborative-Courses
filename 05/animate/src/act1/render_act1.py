import subprocess
import sys
import os

def render_scene(scene_file, scene_class):
    print(f"==================================================")
    print(f"Rendering {scene_class} from {scene_file}...")
    print(f"==================================================")
    
    # Construct command
    # Assuming run from project root
    cmd = [
        "uv", "run", "manim", 
        "-ql",  # Low quality for faster preview (change to -qh for high)
        "--disable_caching", # Optional: force re-render
        scene_file, 
        scene_class
    ]
    
    try:
        # Run command with environment variables inheriting current env
        env = os.environ.copy()
        env["PYTHONPATH"] = os.getcwd() # Ensure root is in PYTHONPATH
        
        subprocess.run(cmd, check=True, env=env)
        print(f"✅ Successfully rendered {scene_class}\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to render {scene_class}")
        return False

def main():
    scenes = [
        ("src/act1/scene1.py", "Act1Scene1"),
        ("src/act1/scene2.py", "Act1Scene2"),
        ("src/act1/scene3.py", "Act1Scene3"),
        ("src/act1/scene4.py", "Act1Scene4"),
        ("src/act1/scene5.py", "Act1Scene5"),
    ]
    
    failed = []
    
    for scene_file, scene_class in scenes:
        if not render_scene(scene_file, scene_class):
            failed.append(scene_class)
            
    if failed:
        print("Summary: Some scenes failed to render:")
        for s in failed:
            print(f"- {s}")
        sys.exit(1)
    else:
        print("🎉 All Act 1 scenes rendered successfully!")

if __name__ == "__main__":
    main()
