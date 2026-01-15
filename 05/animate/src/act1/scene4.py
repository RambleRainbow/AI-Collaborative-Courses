from manim import *

def action(scene, cast):
    # Scene 3 结束时: 左侧概念（Sky/Rain）可见，Q 相关元素隐藏
    
    # 引用右侧概念
    text_q = cast["text_q"]
    box_q = cast["box_q"]
    label_q = cast["label_q"]
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
    
    scene.wait(2)
