from manim import *
from src.utils import *

def action(scene, cast):
    essence = cast["meta_essence"]
    
    # Show Reasoning Machine as the 'Engine'
    engine = ReasoningMachine().scale(0.8).shift(DOWN * 1)
    scene.play(Create(engine))
    
    # Highlight the Gear as the 'Meta Rule' executor
    rule_note = Text("元规则 (Meta-Rule): 控制运作", font=DEFAULT_FONT, font_size=28, color=GOLD).to_edge(UP)
    scene.play(Write(rule_note))
    scene.play(Circumscribe(engine.gear, color=GOLD))
    
    # Run a sample logic
    major = Text("A -> B", font=DEFAULT_FONT)
    minor = Text("A", font=DEFAULT_FONT)
    conc = Text("B", font=DEFAULT_FONT)
    
    steps = engine.get_reasoning_steps(major, minor, conc, is_correct=True)
    for step in steps:
        scene.play(*step)
    
    scene.wait(2)
    scene.play(FadeOut(engine), FadeOut(rule_note), FadeOut(major), FadeOut(minor), FadeOut(conc))
