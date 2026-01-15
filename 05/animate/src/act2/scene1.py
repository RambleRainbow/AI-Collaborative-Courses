from manim import *

def action(scene, cast):
    # 1. Show the static concept map (from Act 1)
    static_group = cast["static_group"]
    
    # Ensure it's centered initially
    static_group.move_to(ORIGIN)
    
    scene.play(FadeIn(static_group), run_time=1)
    scene.wait(1)
    
    # 2. "Freeze" effect
    # Turn grey
    scene.play(
        static_group.animate.set_color(GREY),
        run_time=2
    )
    
    # 3. Question
    q_mark = cast["q_mark"]
    q_mark.next_to(static_group, UP)
    
    scene.play(Write(q_mark))
    
    # 4. Questions text
    q1 = Text("雨从哪里来？", font="PingFang SC", font_size=32).next_to(static_group, DOWN, buff=0.5)
    q2 = Text("水去哪里了？", font="PingFang SC", font_size=32).next_to(q1, DOWN)
    
    scene.play(FadeIn(q1), FadeIn(q2))
    scene.wait(2)
    
    # Cleanup for next scene (fade out qs)
    scene.play(FadeOut(q_mark), FadeOut(q1), FadeOut(q2))
