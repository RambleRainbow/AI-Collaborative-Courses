from manim import *
from src.utils import *

def action(scene, cast):
    # Cleanup
    scene.play(FadeOut(cast["simp_net"]), FadeOut(cast["intro_note"]))
    
    group = cast["sqs_4"]
    labels = cast["lbls_4"]
    frame = cast["frame_4"]
    frame_label = cast["frame_lbl_4"]
    
    scene.play(Create(group), Write(labels), Create(frame), Write(frame_label))
    
    # Cycle animation: A -> B -> D -> C -> A
    # Indices: 0(A), 1(B), 2(D), 3(C)
    sq_a, sq_b, sq_d, sq_c = group
    
    # t=0 A亮
    scene.play(sq_a.animate.set_fill(BLUE, opacity=1), run_time=0.5)
    scene.wait(1)
    
    # t=1 A灭 B亮
    scene.play(
        sq_a.animate.set_fill(BLUE, opacity=0),
        sq_b.animate.set_fill(BLUE, opacity=1),
        run_time=0.5
    )
    scene.wait(1)

    # t=2 B灭 D亮
    scene.play(
        sq_b.animate.set_fill(BLUE, opacity=0),
        sq_d.animate.set_fill(BLUE, opacity=1),
        run_time=0.5
    )
    scene.wait(1)
    
    # t=3 D灭 C亮
    scene.play(
        sq_d.animate.set_fill(BLUE, opacity=0),
        sq_c.animate.set_fill(BLUE, opacity=1),
        run_time=0.5
    )
    scene.wait(1)
    
    # t=4 C灭 A亮
    scene.play(
        sq_c.animate.set_fill(BLUE, opacity=0),
        sq_a.animate.set_fill(BLUE, opacity=1),
        run_time=0.5
    )
    scene.wait(1)
