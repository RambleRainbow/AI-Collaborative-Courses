from manim import *
from src.utils import *

def action(scene, cast):
    layers = cast["layers"]
    
    title = create_title("关于知识的知识 (元知识)")
    scene.play(Write(title))
    
    # Show layers
    scene.play(Create(layers[0]), Write(layers[2])) # Object
    scene.play(Create(layers[1]), Write(layers[3])) # Meta
    
    scene.wait(2)
    scene.play(FadeOut(layers), FadeOut(title))
