from manim import *
from src.utils import *

def action(scene, cast):
    summary = cast["summary_act5"]
    
    title = create_title("第五幕总结")
    scene.play(Write(title))
    scene.wait(1)
    
    for line in summary:
        scene.play(Write(line))
        scene.wait(1)
        
    scene.wait(3)
    scene.play(FadeOut(summary), FadeOut(title))
