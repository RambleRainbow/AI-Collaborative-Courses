from manim import *

def action(scene, cast):
    # Scene 3 结束时: 左侧概念（Sky/Rain）可见，Q 相关元素隐藏
    
    # 引用左侧概念
    left_concepts = VGroup(
        cast["concept_sky"],
        cast["concept_rain"],
        cast["line_left"],
        cast["line_label_left"]
    )
    
    # 引用右侧元素
    text_q = cast["text_q"]
    box_q = cast["box_q"]
    label_q = cast["label_q"]
    
    # 确保 Q 属性被重置为可见 (如果之前 fadeout 了)
    # 这里的 animate 可能会有问题如果 opacity 已经是 0
    # 所以我们先 add 它们以确保存在，然后淡入
    scene.add(text_q, box_q, label_q)
    # 注意: text_q 位置在 S2 移动过，应该还在那里
    
    # 转场：左侧淡出，右侧 (Q) 恢复关注
    scene.play(
        FadeOut(left_concepts),
        text_q.animate.set_opacity(1),
        box_q.animate.set_opacity(1),
        label_q.animate.set_opacity(1),
        run_time=2
    )
    
    # 引用右侧概念
    concept_ground = cast["concept_ground"]
    concept_wet = cast["concept_wet"]
    line = cast["line_right"]
    line_label = cast["line_label_right"]
    
    # 动态对齐
    concept_group = VGroup(concept_ground, concept_wet, line, line_label)
    target_x = text_q.get_center()[0]
    concept_group.set_x(target_x)
    line_label.set_color(WHITE)
    
    # 拆解 Q
    scene.play(
        FadeOut(text_q),
        FadeOut(box_q),
        FadeOut(label_q),
        run_time=2
    )
    
    scene.play(
        FadeIn(concept_ground),
        FadeIn(concept_wet),
        Create(line),
        Write(line_label),
        run_time=2
    )
    
    scene.wait(5)
