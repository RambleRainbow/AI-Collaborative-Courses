from manim import *
from src.utils import *

def action(scene, cast):
    msg = cast["final_msg"]
    
    for line in msg:
        scene.play(Write(line))
        scene.wait(1)
        
    scene.wait(3)
    scene.play(FadeOut(msg))
    
    fin = Text("FIN", font=DEFAULT_FONT, font_size=72).center()
    scene.play(FadeIn(fin, scale=2))
    scene.play(Flash(fin, color=GOLD))
    scene.wait(3)
