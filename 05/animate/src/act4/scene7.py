from manim import *
from src.utils import *

def action(scene, cast):
    machine = cast["machine"].scale(1).center() # Re-center machine
    scene.play(FadeIn(machine))
    
    # Text objects for this scene
    major = Text("下雨 -> 地湿", font=DEFAULT_FONT, font_size=32)
    minor = Text("地湿了", font=DEFAULT_FONT, font_size=32, color=GOLD)
    conc = Text("下雨了?", font=DEFAULT_FONT, font_size=32, color=RED)
    
    steps = machine.get_reasoning_steps(major, minor, conc, is_correct=False)
    
    for step in steps:
        scene.play(*step)
        scene.wait(1)
        
    scene.wait(1)
    
    msg = Text("由于 Q (地湿) 不匹配前件 P (下雨)\n不能得出 P 必成立", font=DEFAULT_FONT, font_size=28, color=RED).to_edge(DOWN)
    scene.play(Write(msg))
    scene.wait(2)
    
    # Cleanup
    scene.play(FadeOut(machine), FadeOut(msg), FadeOut(major), FadeOut(minor), FadeOut(conc))
