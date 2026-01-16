from manim import *
from src.utils import *

def action(scene, cast):
    machine = cast["machine"]
    
    # Update title
    old_title = cast["title_act4"]
    new_title = Text("错误推理演示 (肯定后件)", font=DEFAULT_FONT, font_size=36, color=RED).to_edge(UP)
    
    scene.play(Transform(old_title, new_title))
    scene.wait(1)
    
    # 1. Prepare Content
    major = cast["fa_major"]
    minor = cast["fa_minor"]
    conclusion = cast["fa_conclusion"]
    
    # 2. Get Steps from Machine
    steps = machine.get_reasoning_steps(major, minor, conclusion, is_correct=False)
    
    # Sequence the steps
    for step in steps:
        scene.play(*step)
        scene.wait(0.5)
        
    scene.wait(2)
    
    # Cleanup
    scene.play(FadeOut(machine), FadeOut(old_title))
