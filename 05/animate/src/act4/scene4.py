from manim import *
from src.utils import *

def action(scene, cast):
    machine = cast["machine"]
    
    title = Text("正确推理演示 (肯定前件)", font=DEFAULT_FONT, font_size=36, color=GREEN).to_edge(UP)
    cast["title_act4"] = title
    scene.play(Create(machine), Write(title))
    scene.wait(1)
    
    # 1. Prepare Content
    major = cast["mp_major"]
    minor = cast["mp_minor"]
    conclusion = cast["mp_conclusion"]
    
    # 2. Get Steps from Machine
    steps = machine.get_reasoning_steps(major, minor, conclusion, is_correct=True)
    
    # Sequence the steps
    for step in steps:
        scene.play(*step)
        scene.wait(0.5)
        
    scene.wait(2)
    
    # Clean machine content for next scene
    scene.play(machine.get_clean_anim())
    # Note: Machine itself stays on screen
