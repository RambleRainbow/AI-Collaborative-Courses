from manim import *
from src.utils import *
import random

def get_act3_cast():
    cast = {}
    
    # --- 1. Introduction (Scene 1-2) ---
    intro_txt = create_text("a,b,d,c，4个灯依次亮起")
    intro_note = Text("简化的例子", font=DEFAULT_FONT, font_size=32, color=GREY).to_edge(DOWN)
    cast["intro_txt"] = intro_txt
    cast["intro_note"] = intro_note
    
    # Simple Net (A -> B -> D -> C)
    node_a = create_concept_node("A", LEFT * 4.5)
    node_b = create_concept_node("B", LEFT * 1.5)
    node_d = create_concept_node("D", RIGHT * 1.5)
    node_c = create_concept_node("C", RIGHT * 4.5)
    
    arrow_ab = Arrow(node_a.get_right(), node_b.get_left(), color=GOLD)
    arrow_bd = Arrow(node_b.get_right(), node_d.get_left(), color=GOLD)
    arrow_dc = Arrow(node_d.get_right(), node_c.get_left(), color=GOLD)
    
    label_lead = Text("(导致)", font=DEFAULT_FONT, font_size=24, color=GOLD)
    l1 = label_lead.copy().next_to(arrow_ab, UP)
    l2 = label_lead.copy().next_to(arrow_bd, UP)
    l3 = label_lead.copy().next_to(arrow_dc, UP)
    
    simp_net = VGroup(node_a, node_b, node_d, node_c, arrow_ab, arrow_bd, arrow_dc, l1, l2, l3)
    cast["simp_net"] = simp_net
    cast["node_a"] = node_a
    cast["node_b"] = node_b
    cast["node_d"] = node_d
    cast["node_c"] = node_c
    
    # --- 2. 4-Square Unit (Scene 3) ---
    # Using the new abstracted object
    unit_s3 = LightingUnit(size=4.0, sequence=[0, 1, 3, 2], labels=["A", "B", "C", "D"])
    frame_4 = SurroundingRectangle(unit_s3, color=GOLD, buff=0.3)
    frame_lbl_4 = Text("单元", font=DEFAULT_FONT, color=GOLD).next_to(frame_4, UP)
    
    cast["unit_s3"] = unit_s3
    cast["frame_4"] = frame_4
    cast["frame_lbl_4"] = frame_lbl_4

    # --- 3. 16-Unit Nested Matrix (Scene 4-5) ---
    # 4x4 grid of 2x2 units.
    units_16 = VGroup()
    correct_seq = [0, 1, 3, 2]
    target_unit_idx = 5 
    
    for i in range(16):
        if i == target_unit_idx:
            seq = correct_seq
        else:
            seq = [0, 1, 2, 3]
            random.shuffle(seq)
        
        # Nested units are smaller and have no labels initially
        unit = LightingUnit(size=1.2, sequence=seq, show_labels=False)
        units_16.add(unit)
    
    units_16.arrange_in_grid(4, 4, buff=0.5).scale(0.9).shift(LEFT*1)
    
    target_unit = units_16[target_unit_idx]
    frame_16 = SurroundingRectangle(target_unit, color=GOLD, buff=0.1)
    label_16 = Text("单元识别", font=DEFAULT_FONT, color=GOLD, font_size=32).next_to(frame_16, UP)
    filter_lbl = Text("过滤噪音", font=DEFAULT_FONT, color=WHITE).to_edge(DOWN)
    
    cast["units_16"] = units_16
    cast["frame_16"] = frame_16
    cast["label_16"] = label_16
    cast["filter_lbl"] = filter_lbl
    cast["target_unit_idx"] = target_unit_idx
    
    # --- 4. Comparison (Scene 6) ---
    comp_left_t = Text("A亮 -> B亮", font=DEFAULT_FONT, color=COLOR_STATIC).shift(LEFT*4)
    comp_left_lbl = Text("静态描述", font=DEFAULT_FONT, font_size=24).next_to(comp_left_t, DOWN)
    
    comp_right_loop = Circle(radius=1.5, color=COLOR_DYNAMIC).shift(RIGHT*4)
    comp_right_dots = VGroup(*[Dot(point=comp_right_loop.point_from_proportion(i/4), color=WHITE) for i in range(4)])
    comp_right_lbl = Text("循环机制", font=DEFAULT_FONT, font_size=24).next_to(comp_right_loop, DOWN)
    
    comp_arrow = DoubleArrow(comp_left_t.get_right(), comp_right_loop.get_left(), color=GOLD)
    comp_insight = Text("片面观察 vs 完整机制", font=DEFAULT_FONT, font_size=36, color=YELLOW).to_edge(DOWN)
    
    cast["comp_left"] = VGroup(comp_left_t, comp_left_lbl)
    cast["comp_right"] = VGroup(comp_right_loop, comp_right_dots, comp_right_lbl)
    cast["comp_arrow"] = comp_arrow
    cast["comp_insight"] = comp_insight

    # --- 5. Scene 7 Texts ---
    t1 = Text("只记静态: 看到A -> 期待B", font=DEFAULT_FONT, font_size=32).shift(UP*1)
    t2 = Text("实际机制: A -> B -> D -> C", font=DEFAULT_FONT, font_size=32)
    t3 = Text("如果在D处看到A(误判), 期待B? 错!", font=DEFAULT_FONT, font_size=32, color=RED).shift(DOWN*1)
    
    cast["s7_t1"] = t1
    cast["s7_t2"] = t2
    cast["s7_t3"] = t3
    
    # --- 6. Summary (Scene 8) ---
    summ_lines = VGroup(
        Text("真实世界 = 复杂动态", font=DEFAULT_FONT),
        Text("单元机制 = 可识别的规律", font=DEFAULT_FONT),
        Text("语言知识 = 机制的简化描述", font=DEFAULT_FONT),
        Text("应用 = 识别 + 理解 + 时序", font=DEFAULT_FONT, color=GOLD)
    ).arrange(DOWN, buff=0.5)
    
    cast["summ_lines"] = summ_lines
    
    return cast
