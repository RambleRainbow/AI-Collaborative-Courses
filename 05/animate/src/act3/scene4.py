from manim import *
from src.utils import *
import random

def action(scene, cast):
    # Cleanup Scene 3
    scene.play(
        FadeOut(cast["sqs_4"]), 
        FadeOut(cast["lbls_4"]), 
        FadeOut(cast["frame_4"]), 
        FadeOut(cast["frame_lbl_4"])
    )
    
    # 1. Initialization (Frozen State)
    units_16 = cast["units_16"]
    
    # Set all squares to dimmed/frozen state initially
    all_squares = VGroup(*[sq for unit in units_16 for sq in unit])
    all_squares.set_fill(GREY, opacity=0.2).set_stroke(GREY, opacity=0.3)
    
    scene.play(FadeIn(units_16))
    scene.wait(1)
    
    # 2. Random System Dynamics (Seemingly Chaotic)
    # Each unit follows its own internally consistent cycle
    unit_sequences = cast["unit_sequences"] # 16 sequences
    
    # We run 4 steps of the system's "evolution"
    for step in range(4):
        anims = []
        for i in range(16):
            unit = units_16[i]
            seq = unit_sequences[i]
            # active square index for this step in this unit
            active_sq_idx = seq[step]
            
            for sq_idx in range(4):
                if sq_idx == active_sq_idx:
                    # Light it up!
                    anims.append(unit[sq_idx].animate.set_fill(BLUE, opacity=0.8).set_stroke(WHITE, opacity=1))
                else:
                    # Dim it
                    anims.append(unit[sq_idx].animate.set_fill(GREY, opacity=0.1).set_stroke(GREY, opacity=0.2))
        
        scene.play(*anims, run_time=0.8)

    # 3. Unit Identification (Highlight one unit)
    target_idx = cast["target_unit_idx"]
    target_unit = units_16[target_idx]
    frame = cast["frame_16"]
    label = cast["label_16"]
    
    # We make the target unit stay visible/active while others fade a bit
    scene.play(
        Create(frame), 
        Write(label),
        # Dim non-target units even more to emphasize
        *[units_16[i].animate.set_stroke(opacity=0.1) for i in range(16) if i != target_idx]
    )
    
    # Run one more cycle of the identified unit while target is highlighted
    for step in range(4):
        anims = []
        # Target unit logic (Consistent sequence)
        seq = unit_sequences[target_idx]
        active_sq_idx = seq[step]
        for sq_idx in range(4):
            if sq_idx == active_sq_idx:
                anims.append(target_unit[sq_idx].animate.set_fill(BLUE, opacity=1))
            else:
                anims.append(target_unit[sq_idx].animate.set_fill(BLACK, opacity=0))
        
        # Noise (Other units still flicker randomly)
        for i in range(16):
            if i == target_idx: continue
            other_unit = units_16[i]
            rand_idx = random.randint(0, 3)
            for sq_idx in range(4):
                if sq_idx == rand_idx:
                    anims.append(other_unit[sq_idx].animate.set_fill(GREY, opacity=0.4))
                else:
                    anims.append(other_unit[sq_idx].animate.set_fill(BLACK, opacity=0))
        
        scene.play(*anims, run_time=0.6)
    
    scene.wait(1)
