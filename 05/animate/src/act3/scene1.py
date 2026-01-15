from manim import *
from src.utils import *

def action(scene, cast):
    text = cast["intro_txt"]
    note = cast["intro_note"]
    
    scene.play(Write(text))
    scene.wait(1)
    
    scene.play(Write(note))
    scene.wait(2)
