from manim import *
from src.utils import *

def action(scene, cast):
    examples = cast["real_examples"]
    
    title = create_title("现实中的逆向问题")
    scene.play(Write(title))
    
    # Reveal sequentially
    for ex in examples:
        scene.play(FadeIn(ex, shift=RIGHT * 0.5))
        scene.wait(1)
    
    scene.wait(2)
    scene.play(FadeOut(examples), FadeOut(title))
