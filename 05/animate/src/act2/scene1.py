from manim import *

def action(scene, cast):
    # Act 2 Scene 1: 承接 Act 1 结束状态
    # 图片显示的最终布局就是 Act 2 的起始状态
    
    # 1. 直接显示完整的静态概念图（与图片一致）
    static_group = cast["static_group"]
    scene.add(static_group)
    scene.wait(2)
    
    # 2. "冻结"效果 - 静态知识的局限性
    scene.play(
        static_group.animate.set_color(GREY),
        run_time=2
    )
    
    # 3. 问号
    q_mark = cast["q_mark"]
    scene.play(Write(q_mark))
    
    # 4. 提问
    q1 = Text("雨从哪里来？", font="PingFang SC", font_size=28).next_to(static_group, DOWN, buff=0.3)
    q2 = Text("水去哪里了？", font="PingFang SC", font_size=28).next_to(q1, RIGHT, buff=0.5)
    
    scene.play(FadeIn(q1), FadeIn(q2))
    scene.wait(2)
    
    # 清理问号和提问（为下一场做准备）
    scene.play(FadeOut(q_mark), FadeOut(q1), FadeOut(q2))
