from manim import *
from src.utils import *

def action(scene, cast):
    ui = cast["strat_ui"]
    sys_icon = cast["sys_icon"]
    static_line = cast["static_line"]
    
    scene.play(Write(ui[-1])) # Title
    scene.play(Create(ui[0]), Create(ui[1]), Write(ui[2]), Write(ui[3]))
    
    # Left: Mechanism
    scene.play(Create(sys_icon))
    # Run a few steps of the mechanism to show it's "live"
    for _ in range(4):
        scene.play(*sys_icon.to_next_state(), run_time=0.4)
    
    # Right: Static test list
    scene.play(Write(static_line))
    # Add a red X to one of them to show failure
    wrong_mark = Text("❌", color=RED).scale(0.8).next_to(static_line, RIGHT)
    scene.play(Write(wrong_mark))
    
    scene.wait(2)
    scene.play(FadeOut(ui), FadeOut(sys_icon), FadeOut(static_line), FadeOut(wrong_mark))
