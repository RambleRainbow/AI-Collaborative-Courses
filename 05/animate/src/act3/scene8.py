from manim import *
from src.utils import *

def action(scene, cast):
    # Cleanup
    scene.play(
        FadeOut(cast["s7_t1"]), 
        FadeOut(cast["s7_t2"]), 
        FadeOut(cast["s7_t3"])
    )
    
    title = create_title("第三幕总结")
    lines = cast["summ_lines"]
    
    scene.play(Write(title))
    scene.play(Write(lines), run_time=4)
    scene.wait(3)
