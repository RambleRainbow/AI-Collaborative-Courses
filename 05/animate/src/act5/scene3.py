from manim import *
from src.utils import *

def action(scene, cast):
    net = cast["fan_in_net"]
    ps = net[0]
    arrows = net[1]
    node_q = net[2]
    
    label = Text("原因 A? B? C? ... -> 结果 Q", font=DEFAULT_FONT, font_size=32).to_edge(UP)
    scene.play(Write(label))
    
    # Show Q first
    scene.play(Create(node_q))
    scene.wait(1)
    
    # Causes pop out
    for p, arr in zip(ps, arrows):
        scene.play(Create(p), Create(arr), run_time=0.4)
    
    scene.wait(1)
    
    # Highlight uncertainty
    q_mark = Text("?", color=RED).scale(2).next_to(node_q, RIGHT)
    scene.play(Write(q_mark))
    scene.play(Indicate(q_mark))
    
    scene.wait(2)
    scene.play(FadeOut(net), FadeOut(label), FadeOut(q_mark))
