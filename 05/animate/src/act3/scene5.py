from manim import *
from src.utils import *

def action(scene, cast):
    squares = cast["sqs_16"]
    unit_indices = cast["unit_indices"]
    other_indices = [i for i in range(16) if i not in unit_indices]
    
    # Noise reduction
    scene.play(FadeOut(cast["label_16"]))
    
    anims = []
    for i in other_indices:
        anims.append(squares[i].animate.set_stroke(opacity=0.3).set_fill(opacity=0.1))
    
    filter_lbl = cast["filter_lbl"]
    scene.play(*anims, Write(filter_lbl), run_time=1.5)
    
    # Continued unit cycle
    cycle = [0, 1, 5, 4]
    for step in range(4):
        active_idx = cycle[step]
        u_anims = []
        for u_idx in unit_indices:
            if u_idx == active_idx:
                u_anims.append(squares[u_idx].animate.set_fill(BLUE, opacity=1))
            else:
                u_anims.append(squares[u_idx].animate.set_fill(BLACK, opacity=0))
        scene.play(*u_anims, run_time=0.6)
    
    scene.wait(1)
