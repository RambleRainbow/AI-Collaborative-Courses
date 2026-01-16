from manim import *
from src.utils import *

def action(scene, cast):
    # Transition from Scene 1
    scene.play(FadeOut(cast["fallacy_intro"]))
    
    net = cast["static_fallacy_net"]
    node_p = net[0]
    node_q = net[1]
    arrow = net[2]
    q_true = net[3]
    p_true_wrong = net[4]
    cross = net[5]
    
    # 1. Show P -> Q
    scene.play(Create(node_p), Create(node_q), Create(arrow))
    scene.wait(1)
    
    # 2. Assert Q is true
    scene.play(Write(q_true))
    scene.play(node_q[0].animate.set_fill(BLUE, opacity=1))
    scene.wait(1)
    
    # 3. Incorrect inference to P
    scene.play(Write(p_true_wrong))
    scene.play(FadeIn(cross, scale=1.5))
    scene.play(Flash(p_true_wrong, color=RED))
    
    scene.wait(2)
    
    # Cleanup for next scene
    scene.play(FadeOut(net))
