from manim import *
from src.utils import *

def action(scene, cast):
    units_16 = cast["units_16"]
    target_idx = cast["target_unit_idx"]
    target_unit = units_16[target_idx]
    frame = cast["frame_16"]
    label = cast["label_16"]
    
    # 1. Noise Reduction
    scene.play(FadeOut(label))
    
    # Dim all non-target units significantly
    anims = []
    for i in range(16):
        if i == target_idx:
            # Highlight target
            anims.append(target_unit.animate.set_stroke(WHITE, opacity=1).scale(1.1))
        else:
            # Fade others
            anims.append(units_16[i].animate.set_stroke(opacity=0.05).set_fill(opacity=0))
    
    filter_lbl = cast["filter_lbl"]
    scene.play(*anims, Write(filter_lbl), run_time=2)
    
    # 2. Focused Cycle (Mechanism emerges)
    # Use the specific sequence for the target unit from cast
    unit_sequences = cast["unit_sequences"]
    target_seq = unit_sequences[target_idx]
    
    for step in range(4):
        active_sq_idx = target_seq[step]
        u_anims = []
        for sq_idx in range(4):
            if sq_idx == active_sq_idx:
                u_anims.append(target_unit[sq_idx].animate.set_fill(BLUE, opacity=1))
            else:
                u_anims.append(target_unit[sq_idx].animate.set_fill(BLACK, opacity=0))
        scene.play(*u_anims, run_time=0.6)
    
    scene.wait(1)
