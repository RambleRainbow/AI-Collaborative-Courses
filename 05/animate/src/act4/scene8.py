from manim import *
from src.utils import *

def action(scene, cast):
    summary = cast["summary_act4"]
    title = summary[0]
    lines = summary[1]
    
    scene.play(Write(title))
    scene.wait(1)
    
    for line in lines:
        scene.play(Write(line))
        scene.wait(1)
        
    scene.wait(3)
    
    # Final cleanup
    scene.play(FadeOut(summary))
