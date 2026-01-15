from manim import *
from src.utils import *

def action(scene, cast):
    # Cleanup Intro
    scene.play(FadeOut(cast["simp_net"]), FadeOut(cast["intro_note"]))
    
    unit = cast["unit_s3"]
    frame = cast["frame_4"]
    frame_label = cast["frame_lbl_4"]
    
    scene.play(Create(unit), Create(frame), Write(frame_label))
    
    # 5 steps: A, B, D, C, A
    for _ in range(4*5):
        scene.play(*unit.to_next_state(), run_time=0.5)
        scene.wait(0.5)
