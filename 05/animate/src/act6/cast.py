from manim import *
from src.utils import *

def get_act6_cast():
    cast = {}
    
    # --- 1. Scene 1: Knowledge Levels ---
    obj_layer = RoundedRectangle(width=8, height=2, color=BLUE_E, fill_opacity=0.1)
    meta_layer = RoundedRectangle(width=8, height=2, color=GOLD_E, fill_opacity=0.1).next_to(obj_layer, UP, buff=1)
    
    obj_lbl = Text("对象层: P, Q, 发烧, 雨...", font=DEFAULT_FONT, font_size=24, color=BLUE).move_to(obj_layer.get_center())
    meta_lbl = Text("元层: 性质, 约束, 规则...", font=DEFAULT_FONT, font_size=24, color=GOLD).move_to(meta_layer.get_center())
    
    cast["layers"] = VGroup(obj_layer, meta_layer, obj_lbl, meta_lbl)

    # --- 2. Scene 3: Meta-Knowledge Essence ---
    # {P->Q} as an object, and a lens looking at its structure
    obj_pq = Text("P -> Q", font=DEFAULT_FONT, font_size=32).shift(LEFT * 2)
    meta_rule = Text("结构约束: 槽位匹配", font=DEFAULT_FONT, font_size=32, color=GOLD).shift(RIGHT * 2)
    arrow_obs = Arrow(meta_rule.get_left(), obj_pq.get_right(), color=GOLD)
    
    cast["meta_essence"] = VGroup(obj_pq, meta_rule, arrow_obs)

    # --- 6. Finale: Summary ---
    final_msg = VGroup(
        Text("知识不是符号，而是机制", font=DEFAULT_FONT, font_size=36),
        Text("理解不是记忆，而是同构", font=DEFAULT_FONT, font_size=36, color=BLUE),
        Text("应用不是匹配，而是约束识别", font=DEFAULT_FONT, font_size=36, color=GOLD)
    ).arrange(DOWN, buff=1).center()
    
    cast["final_msg"] = final_msg
    
    return cast
