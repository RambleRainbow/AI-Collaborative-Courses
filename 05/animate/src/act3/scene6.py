from manim import *
from src.utils import *

def action(scene, cast):
    # Cleanup Act 3 Scene 5 elements
    scene.play(
        FadeOut(cast["units_16"]), 
        FadeOut(cast["frame_16"]), 
        FadeOut(cast["filter_lbl"])
    )
    
    left = cast["comp_left"]
    right = cast["comp_right"]
    arrow = cast["comp_arrow"]
    insight = cast["comp_insight"]
    
    scene.play(FadeIn(left))
    scene.play(FadeIn(right))
    scene.play(Create(arrow))
    scene.play(Write(insight))
    
    scene.wait(3)
