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
    # 4x4 grid of 2x2 units. Total 8x8 squares.
    # To make the grid uniform, buff_internal must equal buff_external.
    gap = 0.1
    unit_size = 1.0 # arbitrary, but will affect total size
    # Total width of 4 units + 3 external gaps = 4 * unit_size + 3 * gap
    
    units_16 = VGroup()
    correct_seq = [0, 1, 3, 2]
    target_unit_idx = 5 
    
    for i in range(16):
        if i == target_unit_idx:
            seq = correct_seq
        else:
            seq = [0, 1, 2, 3]
            random.shuffle(seq)
        
        # Internal buff set to 'gap'
        unit = LightingUnit(size=unit_size, sequence=seq, show_labels=False, buff=gap)
        units_16.add(unit)
    
    # External buff set to 'gap'
    units_16.arrange_in_grid(4, 4, buff=gap).scale(1) # Center it
    
    target_unit = units_16[target_unit_idx]
    frame_16 = SurroundingRectangle(target_unit, color=GOLD, buff=0.1)
    
    cast["units_16"] = units_16
    cast["frame_16"] = frame_16
    cast["target_unit_idx"] = target_unit_idx
    
    # --- 4. Comparison (Scene 6) ---
    # Left (Static Description)
    comp_left_t = Text("A,B,D,C依次亮", font=DEFAULT_FONT, color=COLOR_STATIC).shift(LEFT*4)
    comp_left_lbl = Text("静态描述", font=DEFAULT_FONT, font_size=24).next_to(comp_left_t, DOWN)

    # Right (Loop Mechanism) - Using our abstracted LightingUnit
    comp_unit = LightingUnit(size=3.0, sequence=[0, 1, 3, 2], labels=["A", "B", "C", "D"]).shift(RIGHT*4)
    comp_right_lbl = Text("循环机制", font=DEFAULT_FONT, font_size=24).next_to(comp_unit, DOWN)
    
    comp_arrow = DoubleArrow(comp_left_t.get_right(), comp_unit.get_left(), color=GOLD)
    comp_insight = Text("片面观察 vs 完整机制", font=DEFAULT_FONT, font_size=36, color=YELLOW).to_edge(DOWN)
    
    cast["comp_left"] = VGroup(comp_left_t, comp_left_lbl)
    cast["comp_right"] = VGroup(comp_unit, comp_right_lbl)
    cast["comp_unit"] = comp_unit
    cast["comp_arrow"] = comp_arrow
    cast["comp_insight"] = comp_insight

    return cast
