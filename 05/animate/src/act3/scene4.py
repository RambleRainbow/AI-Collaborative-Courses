from manim import *
from src.utils import *
import random

def action(scene, cast):
    # Cleanup
    scene.play(
        FadeOut(cast["sqs_4"]), 
        FadeOut(cast["lbls_4"]), 
        FadeOut(cast["frame_4"]), 
        FadeOut(cast["frame_lbl_4"])
    )
    
    squares = cast["sqs_16"]
    scene.play(FadeIn(squares))
    
    unit_indices = cast["unit_indices"]
    other_indices = [i for i in range(16) if i not in unit_indices]
    
    # chaos phase
    for _ in range(2):
        anims = []
        for i in range(16):
            if random.random() > 0.5:
                anims.append(squares[i].animate.set_fill(GREY, opacity=0.8))
            else:
                anims.append(squares[i].animate.set_fill(BLACK, opacity=0))
        scene.play(*anims, run_time=0.4)
    
    # Unit identification
    frame = cast["frame_16"]
    label = cast["label_16"]
    scene.play(Create(frame), Write(label))
    
    # Cyclic operation
    cycle = [0, 1, 5, 4] 
    for step in range(4):
        anims = []
        active_idx = cycle[step]
        for u_idx in unit_indices:
            if u_idx == active_idx:
                anims.append(squares[u_idx].animate.set_fill(BLUE, opacity=1))
            else:
                anims.append(squares[u_idx].animate.set_fill(BLACK, opacity=0))
        
        # chaos logic for others
        for o_idx in other_indices:
            if random.random() > 0.5:
                anims.append(squares[o_idx].animate.set_fill(GREY, opacity=0.5))
            else:
                anims.append(squares[o_idx].animate.set_fill(BLACK, opacity=0))
        
        scene.play(*anims, run_time=0.6)
