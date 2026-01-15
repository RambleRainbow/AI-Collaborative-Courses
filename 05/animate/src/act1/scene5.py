from manim import *
from src.utils import *

def action(scene, cast):
    # Scene 4 结束时: 右侧概念 (Ground/Wet) 可见。
    # Scene 3 的左侧概念 (Sky/Rain) 之前 fadeout 了，现在需要回来。
    
    # 引用所有概念元素
    c_sky = cast["concept_sky"]
    c_rain = cast["concept_rain"]
    l_left = cast["line_left"]
    txt_left = cast["line_label_left"]
    
    c_ground = cast["concept_ground"]
    c_wet = cast["concept_wet"]
    l_right = cast["line_right"]
    txt_right = cast["line_label_right"]
    
    # 定义目标布局
    # 左侧组: UP*2 + LEFT*4
    # 右侧组: UP*2 + RIGHT*4
    # 注意: 原脚本布局较宽，这里尽量适配屏幕
    
    group_left = VGroup(c_sky, c_rain, l_left, txt_left)
    group_right = VGroup(c_ground, c_wet, l_right, txt_right)
    
    target_left_pos = LEFT * 3.5
    target_right_pos = RIGHT * 3.5
    
    # 恢复左侧显示 (FadeIn) 并同时移动两者到最终布局位置
    # 左侧此时不可见，先移到目标位置再 FadeIn? 或者直接 FadeIn
    # 更好的效果：左侧在原来的位置浮现，然后左右两组一起调整位置
    
    scene.play(FadeIn(group_left), run_time=1)
    
    scene.play(
        group_left.animate.move_to(target_left_pos),
        group_right.animate.move_to(target_right_pos),
        run_time=2
    )
    
    # 建立因果连接
    # 从 Rain (左侧下部) 到 Wet (右侧下部)
    arrow = Arrow(c_rain.get_right(), c_wet.get_left(), color=GOLD)
    arrow_label = Text("(因果)", font=DEFAULT_FONT, font_size=24, color=GOLD).next_to(arrow, DOWN)
    
    scene.play(
        GrowArrow(arrow),
        Write(arrow_label),
        run_time=2
    )
    
    # 总结标注
    note = Text("知识的深层结构：概念+关系的网络", font=DEFAULT_FONT, font_size=36, color=YELLOW).to_edge(DOWN)
    scene.play(Write(note))
    
    scene.wait(5)
