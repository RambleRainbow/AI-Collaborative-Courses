from manim import *
from src.utils import *

def action(scene, cast):
    # Cleanup
    scene.play(
        FadeOut(cast["comp_left"]), 
        FadeOut(cast["comp_right"]), 
        FadeOut(cast["comp_arrow"]), 
        FadeOut(cast["comp_insight"])
    )
    
    t1 = cast["s7_t1"]
    t2 = cast["s7_t2"]
    t3 = cast["s7_t3"]
    
    scene.play(Write(t1))
    scene.wait(1)
    scene.play(Write(t2))
    scene.wait(1)
    scene.play(Write(t3))
    scene.wait(3)
