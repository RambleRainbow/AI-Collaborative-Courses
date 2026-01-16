from manim import *
from src.utils import *

def action(scene, cast):
    title = cast["fallacy_intro"][0]
    text = cast["fallacy_intro"][1]
    
    scene.play(Write(title))
    scene.wait(1)
    
    for line in text:
        scene.play(Write(line))
        scene.wait(0.5)
    
    scene.wait(2)
