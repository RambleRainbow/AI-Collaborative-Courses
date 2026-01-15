from manim import *

def action(scene, cast):
    # 引用便捷变量
    text_p = cast["text_p"]
    box_p = cast["box_p"]
    label_p = cast["label_p"]
    
    # 引入概念图
    concept_sky = cast["concept_sky"]
    concept_rain = cast["concept_rain"]
    line = cast["line_left"]
    line_label = cast["line_label_left"]
    
    # 动态对齐：将概念组水平对齐到 text_p
    concept_group = VGroup(concept_sky, concept_rain, line, line_label)
    target_x = text_p.get_center()[0]
    concept_group.set_x(target_x)
    
    # 确保标签颜色
    line_label.set_color(WHITE)
    
    # 文字溶解，概念浮现
    scene.play(
        FadeOut(text_p),
        FadeOut(box_p),
        FadeOut(label_p),
        run_time=2
    )
    
    scene.play(
        FadeIn(concept_sky),
        FadeIn(concept_rain),
        Create(line),
        Write(line_label),
        run_time=2
    )
    
    scene.wait(2)
