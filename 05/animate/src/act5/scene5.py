from manim import *
from src.utils import *

def action(scene, cast):
    # Don't .center() as it overrides the coordinate-based layout
    machine = ReasoningMachine().shift(DOWN * 0.5)
    scene.play(FadeIn(machine))
    
    label = create_title("机制导向的诊断")
    scene.play(Write(label))
    
    # Reasoning 1: Identifying the right unit
    major = Text("系统机制: [指标X -> 细菌感染]", font=DEFAULT_FONT, font_size=28)
    minor = Text("观测到: 指标X", font=DEFAULT_FONT, font_size=28, color=GOLD)
    conc = Text("确认为: 细菌感染", font=DEFAULT_FONT, font_size=28, color=GREEN)
    
    steps = machine.get_reasoning_steps(major, minor, conc, is_correct=True)
    for step in steps:
        scene.play(*step)
        scene.wait(0.5)
        
    scene.wait(1)
    
    # Note on filtering
    filter_note = Text("(通过机制排除了病毒感染、炎症等选项)", font=DEFAULT_FONT, font_size=24, color=GREY).to_edge(DOWN)
    scene.play(Write(filter_note))
    scene.wait(2)
    
    # Cleanup
    scene.play(FadeOut(machine), FadeOut(label), FadeOut(filter_note), FadeOut(major), FadeOut(minor), FadeOut(conc))
