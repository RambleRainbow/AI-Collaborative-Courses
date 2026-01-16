from manim import *
from src.utils import *

def action(scene, cast):
    boxes = cast["comp_boxes"]
    title = boxes[-1]
    
    scene.play(Write(title))
    scene.play(Create(boxes[0]), Create(boxes[1]), Write(boxes[2]), Write(boxes[3]))
    
    # Content for Left (System)
    m_left = ReasoningMachine().scale(0.5).move_to(boxes[0].get_center())
    scene.play(FadeIn(m_left))
    
    # Content for Right (Static)
    net_static = cast["static_fallacy_net"].copy().scale(0.6).move_to(boxes[1].get_center())
    # Remove some things to make it look "static/broken"
    net_static.remove(net_static[5]) # red cross
    scene.play(FadeIn(net_static))
    
    note_left = Text("把握结构约束", font=DEFAULT_FONT, font_size=20, color=GREEN).next_to(boxes[0], DOWN)
    note_right = Text("忽视结构，只看关联", font=DEFAULT_FONT, font_size=20, color=RED).next_to(boxes[1], DOWN)
    
    scene.play(Write(note_left), Write(note_right))
    scene.wait(3)
    
    # Cleanup
    scene.play(FadeOut(boxes), FadeOut(m_left), FadeOut(net_static), FadeOut(note_left), FadeOut(note_right))
