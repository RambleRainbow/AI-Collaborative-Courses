from manim import *
from src.utils import *

def action(scene, cast):
    units_16 = cast["units_16"]
    target_idx = cast["target_unit_idx"]
    target_unit = units_16[target_idx]
    
    # 1. Noise Reduction
    
    anims = []
    for i in range(16):
        if i == target_idx:
            anims.append(target_unit.animate.set_stroke(WHITE, opacity=1).scale(1.1))
        else:
            anims.append(units_16[i].animate.set_stroke(opacity=0.05).set_fill(opacity=0))
    
    scene.play(*anims, run_time=2)
    
    # 2. Focused Cycle
    for _ in range(4*3):
        scene.play(*target_unit.to_next_state(), run_time=0.6)
    
    scene.wait(1)
