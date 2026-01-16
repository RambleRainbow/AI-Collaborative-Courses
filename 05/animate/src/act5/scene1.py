from manim import *
from src.utils import *

def action(scene, cast):
    logic_dir = cast["logic_dir"]
    sub_text = Text("(原因 -> 结果)", font=DEFAULT_FONT, font_size=24, color=GREY).to_edge(DOWN)
    
    # 1. Forward
    scene.play(FadeIn(logic_dir[0]), Write(sub_text))
    scene.wait(1)
    
    # 2. Reverse
    rev_sub = Text("现实挑战: (结果 -> 原因?)", font=DEFAULT_FONT, font_size=24, color=RED).to_edge(DOWN)
    scene.play(
        FadeIn(logic_dir[1]),
        Transform(sub_text, rev_sub)
    )
    scene.wait(2)
    
    # Cleanup
    scene.play(FadeOut(logic_dir), FadeOut(sub_text))
