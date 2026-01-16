import os
import subprocess
import sys
import time
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a shell command and ensure it succeeds."""
    print(f"\n>>> Executing: {cmd}")
    env = os.environ.copy()
    # Disable debug mode for the sub-process
    env["ANIMATE_DEBUG"] = "0"
    # Ensure local modules are found
    env["PYTHONPATH"] = f"{os.getcwd()}:{env.get('PYTHONPATH', '')}"
    
    process = subprocess.Popen(
        cmd,
        shell=True,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Print output in real-time
    for line in process.stdout:
        print(line, end="")
        
    process.wait()
    if process.returncode != 0:
        print(f"\n!!! Error: Command failed with exit code {process.returncode}")
        sys.exit(process.returncode)

def main():
    start_time = time.time()
    
    # 1. Configuration
    acts = [
        ("Act1", "src/act1/render.py"),
        ("Act2", "src/act2/render.py"),
        ("Act3", "src/act3/render.py"),
        ("Act4", "src/act4/render.py"),
        ("Act5", "src/act5/render.py"),
        ("Act6", "src/act6/render.py"),
    ]
    
    # Manim 1080p path pattern
    base_video_dir = Path("media/videos/render/1080p60")
    rendered_files = []
    
    print("="*60)
    print("      KNOWLEDGE ONTOLOGY ANIMATION - RELEASE PIPELINE")
    print("="*60)
    print(f"Target: 1080p (Full HD), Debug Mode: OFF")
    
    # 2. Render all Acts
    for act_name, script_path in acts:
        print(f"\n--- Rendering {act_name} ---")
        # -qh: 1080p60, high quality
        # --flush_cache: ensure we don't pick up old debug versions if any
        cmd = f"uv run manim -qh --flush_cache {script_path} {act_name}"
        run_command(cmd)
        
        video_path = base_video_dir / f"{act_name}.mp4"
        if not video_path.exists():
            # Sometimes manim puts it in a subfolder named after the script file
            # e.g. media/videos/render/1080p60/Act1.mp4
            # If it's missing, we check if it's there
            print(f"Warning: Expected {video_path} not found.")
        else:
            rendered_files.append(video_path)
    
    # 3. Merge Videos
    if not rendered_files:
        print("No videos were rendered. Exiting.")
        return

    print("\n" + "="*60)
    print("      MERGING ACTS INTO FINAL VIDEO")
    print("="*60)
    
    concat_list_path = Path("concat_list.txt")
    with open(concat_list_path, "w") as f:
        for video in rendered_files:
            f.write(f"file '{video.absolute()}'\n")
    
    output_filename = f"Knowledge_Ontology_Full_1080p_{int(time.time())}.mp4"
    # -y: overwrite
    # -c copy: stream copy (no re-encoding, extremely fast)
    merge_cmd = f"ffmpeg -f concat -safe 0 -y -i {concat_list_path} -c copy {output_filename}"
    
    run_command(merge_cmd)
    
    # 4. Optional Cleanup
    if concat_list_path.exists():
        concat_list_path.unlink()
        
    duration = time.time() - start_time
    print("\n" + "="*60)
    print(f"SUCCESS!")
    print(f"Final Video: {os.path.abspath(output_filename)}")
    print(f"Total time: {duration/60:.2f} minutes")
    print("="*60)

if __name__ == "__main__":
    main()
