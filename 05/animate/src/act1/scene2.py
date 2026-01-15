from manim import *

def action(scene, cast):
    # 1. 引用 Cast
    text_if = cast["text_if"]
    text_p = cast["text_p"]
    text_comma = cast["text_comma"]
    text_then = cast["text_then"]
    text_q = cast["text_q"]
    
    # 2. 动画逻辑: 隐藏连接词，分离命题
    scene.play(
        FadeOut(text_if),
        FadeOut(text_comma),
        FadeOut(text_then),
        run_time=1
    )
    
    # 移动命题
    scene.play(
        text_p.animate.move_to(LEFT * 3),
        text_q.animate.move_to(RIGHT * 3),
        run_time=2
    )
    
    # 3. 引入结构元素
    arrow = cast["arrow"]
    box_p = cast["box_p"]
    box_q = cast["box_q"]
    label_p = cast["label_p"]
    label_q = cast["label_q"]
    label_rel = cast["label_rel"]
    
    # update positions based on where text_p/q ended up
    # Note: text_p/q keys are referencing the same objects modified above
    
    # Re-align structural elements to the *current* position of text objects
    box_p.move_to(text_p)
    box_q.move_to(text_q)
    
    arrow.next_to(text_p, RIGHT)
    # Dynamic stretch for arrow?
    # Let's just put it between them
    arrow.put_start_and_end_on(text_p.get_right() + RIGHT*0.5, text_q.get_left() - RIGHT*0.5)
    
    label_p.next_to(box_p, UP)
    label_q.next_to(box_q, UP)
    label_rel.next_to(arrow, UP)
    
    scene.play(Create(arrow), run_time=1)
    
    scene.play(
        Create(box_p),
        Create(box_q),
        Write(label_p),
        Write(label_q),
        Write(label_rel),
        run_time=2
    )
    scene.wait(2)