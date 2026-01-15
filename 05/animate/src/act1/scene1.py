from manim import *

def action(scene, cast):
    # 1. 引用 Cast
    text_if = cast["text_if"]
    text_p = cast["text_p"]
    text_comma = cast["text_comma"]
    text_then = cast["text_then"]
    text_q = cast["text_q"]
    
    # 2. 动画逻辑: 呈现整句句子
    # Scene 1 treat them as a group effectively
    group = VGroup(text_if, text_p, text_comma, text_then, text_q)
    
    # 确保位置正确 (初始位置 already defined in cast implicitly via create)
    # 剧中显示
    
    scene.play(Write(group), run_time=2)
    scene.wait(2)
    
    # 确保状态为实心文字 (Fix for write animation artifacts)
    group.set_fill(opacity=1)
    group.set_stroke(width=0)
    
    scene.wait(2)
