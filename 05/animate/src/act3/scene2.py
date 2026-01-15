from manim import *
from src.utils import *

def action(scene, cast):
    # Setup
    scene.play(FadeOut(cast["intro_txt"]))
    
    simp_net = cast["simp_net"]
    scene.play(FadeIn(simp_net))
    scene.wait(1)
    
    # Freeze
    scene.play(simp_net.animate.set_color(COLOR_STATIC))
    
    # Update note
    new_note = Text("A亮 导致 B亮 导致 D亮 导致 C亮", font=DEFAULT_FONT, color=COLOR_STATIC).to_edge(DOWN)
    scene.play(ReplacementTransform(cast["intro_note"], new_note))
    cast["intro_note"] = new_note
    
    scene.wait(2)
