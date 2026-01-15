from manim import *
from src.utils import *
import random

def action(scene, cast):
    # Cleanup Scene 3
    scene.play(
        FadeOut(cast["unit_s3"]), 
        FadeOut(cast["frame_4"]), 
        FadeOut(cast["frame_lbl_4"])
    )
    
    # 1. Initialization (Frozen State)
    units_16 = cast["units_16"]
    
    # Set all units to frozen state initially using internal method
    freeze_anims = []
    for unit in units_16:
        freeze_anims.extend(unit.get_frozen_state_anims())
    
    scene.play(FadeIn(units_16), *freeze_anims)
    scene.wait(1)
    
    # 2. Random System Dynamics
    # Run 4 steps of evolution. Each unit's to_next_state handles its own sequence.
    for step in range(4*5):
        all_anims = []
        for unit in units_16:
            all_anims.extend(unit.to_next_state(color=GREY, opacity=0.4))
        scene.play(*all_anims, run_time=0.8)

    # 3. Unit Identification
    target_idx = cast["target_unit_idx"]
    target_unit = units_16[target_idx]
    frame = cast["frame_16"]
    
    # Highlight one unit
    scene.play(
        Create(frame), 
        *[units_16[i].animate.set_stroke(opacity=0.1) for i in range(16) if i != target_idx]
    )
    
    # Run one more cycle of identified unit + others flickering
    for _ in range(4):
        anims = []
        # Target unit follows its correct sequence
        anims.extend(target_unit.to_next_state(color=BLUE, opacity=1.0))
        
        # Others move to some next state (still looks chaotic)
        for i in range(16):
            if i == target_idx: continue
            anims.extend(units_16[i].to_next_state(color=GREY, opacity=0.3))
            
        scene.play(*anims, run_time=0.6)
    
    scene.wait(1)
