from manim import *
from src.utils import *

def action(scene, cast):
    ont = cast["ont_system"]
    
    label = Text("推理系统的结构", font=DEFAULT_FONT, font_size=36, color=BLUE).to_edge(UP)
    scene.play(Write(label))
    
    # Reveal nodes
    scene.play(Create(ont[0]), Create(ont[1])) # Major, Minor
    scene.wait(0.5)
    scene.play(Create(ont[4]), Create(ont[5]), Create(ont[2])) # Arrows to Rule, Rule
    scene.wait(0.5)
    scene.play(Create(ont[6]), Create(ont[3])) # Arrow to Conclusion, Conclusion
    
    # Identify as a unit
    frame = SurroundingRectangle(ont, color=GOLD, buff=0.5)
    unit_lbl = Text("推理单元", font=DEFAULT_FONT, color=GOLD, font_size=32).next_to(frame, UP)
    
    scene.play(Create(frame), Write(unit_lbl))
    scene.wait(2)
    
    # Cleanup
    scene.play(FadeOut(ont), FadeOut(frame), FadeOut(unit_lbl), FadeOut(label))
