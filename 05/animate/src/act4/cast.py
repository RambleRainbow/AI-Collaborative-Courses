from manim import *
from src.utils import *

def get_act4_cast():
    cast = {}
    
    # --- 1. Scene 1 & 2: Fallacy Intro & Static Disassembly ---
    fallacy_title = create_text("肯定后件谬误", font_size=40, color=RED)
    fallacy_text = VGroup(
        Text("错误推理形式：", font=DEFAULT_FONT, font_size=24),
        Text("如果P，那么Q (P → Q)", font=DEFAULT_FONT, font_size=24),
        Text("Q 为真", font=DEFAULT_FONT, font_size=24),
        Text("所以 P 为真", font=DEFAULT_FONT, font_size=24, color=RED)
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(fallacy_title, DOWN, buff=1)
    
    cast["fallacy_intro"] = VGroup(fallacy_title, fallacy_text).center()
    
    # Static Network for Scene 2
    node_p_static = create_concept_node("P", LEFT * 2 + UP * 1)
    node_q_static = create_concept_node("Q", RIGHT * 2 + UP * 1)
    arrow_pq_static = Arrow(node_p_static.get_right(), node_q_static.get_left(), color=GOLD)
    
    q_is_true = Text("Q 为真", font=DEFAULT_FONT, font_size=24).next_to(node_q_static, DOWN, buff=0.5)
    p_is_true_wrong = Text("所以 P 为真?", font=DEFAULT_FONT, font_size=24, color=RED).next_to(node_p_static, DOWN, buff=1.5)
    cross_red = Text("❌", color=RED).scale(2).move_to(p_is_true_wrong)
    
    cast["static_fallacy_net"] = VGroup(node_p_static, node_q_static, arrow_pq_static, q_is_true, p_is_true_wrong, cross_red)

    # --- 2. Scene 3: Ontological Structure ---
    # {Major Premise, Minor Premise, Rule, Conclusion}
    ont_major = create_concept_node("大前提", UP * 2.5 + LEFT * 1.5, color=GOLD)
    ont_minor = create_concept_node("小前提", UP * 2.5 + RIGHT * 1.5, color=GOLD)
    ont_rule = create_concept_node("推理规则", ORIGIN, color=BLUE)
    ont_conclusion = create_concept_node("结论", DOWN * 2.5, color=GOLD)
    
    arrow1 = Arrow(ont_major.get_bottom(), ont_rule.get_top(), buff=0.1)
    arrow2 = Arrow(ont_minor.get_bottom(), ont_rule.get_top(), buff=0.1)
    arrow3 = Arrow(ont_rule.get_bottom(), ont_conclusion.get_top(), buff=0.1)
    
    ont_system = VGroup(ont_major, ont_minor, ont_rule, ont_conclusion, arrow1, arrow2, arrow3)
    cast["ont_system"] = ont_system
    
    # --- 3. Scene 4 & 5: Reasoning Machine ---
    machine = ReasoningMachine()
    cast["machine"] = machine
    
    # Content for Machine (Modus Ponens - Correct)
    major_mp = Text("P → Q", font=DEFAULT_FONT, font_size=36)
    minor_mp = Text("P", font=DEFAULT_FONT, font_size=32)
    conclusion_mp = Text("Q", font=DEFAULT_FONT, font_size=32)
    
    cast["mp_major"] = major_mp
    cast["mp_minor"] = minor_mp
    cast["mp_conclusion"] = conclusion_mp
    
    # Content for Machine (Fallacy - Incorrect)
    major_fa = Text("P → Q", font=DEFAULT_FONT, font_size=36)
    minor_fa = Text("Q", font=DEFAULT_FONT, font_size=32)
    conclusion_fa = Text("P", font=DEFAULT_FONT, font_size=32)
    
    cast["fa_major"] = major_fa
    cast["fa_minor"] = minor_fa
    cast["fa_conclusion"] = conclusion_fa
    
    # --- 4. Scene 6: Comparison ---
    comp_title = create_title("为什么会产生谬误?")
    comp_left_box = RoundedRectangle(width=5, height=4, color=BLUE_E).shift(LEFT * 3.5 + DOWN * 0.5)
    comp_right_box = RoundedRectangle(width=5, height=4, color=GREY_E).shift(RIGHT * 3.5 + DOWN * 0.5)
    
    left_label = Text("理解系统", font=DEFAULT_FONT, font_size=24).next_to(comp_left_box, UP)
    right_label = Text("只记概念", font=DEFAULT_FONT, font_size=24).next_to(comp_right_box, UP)
    
    cast["comp_boxes"] = VGroup(comp_left_box, comp_right_box, left_label, right_label, comp_title)
    
    # --- 5. Scene 7: Real Application ---
    rain_p = Text("如果下雨 (P) -> 地会湿 (Q)", font=DEFAULT_FONT, font_size=28)
    ground_wet = Text("观测到: 地湿 (Q)", font=DEFAULT_FONT, font_size=28, color=GOLD)
    rain_conclusion = Text("结论: 下雨了 (P)?", font=DEFAULT_FONT, font_size=28, color=RED)
    
    cast["real_app_text"] = VGroup(rain_p, ground_wet, rain_conclusion).arrange(DOWN, buff=0.5).center()
    
    # --- 6. Scene 8: Summary ---
    summary_title = create_title("第四幕总结")
    summary_lines = VGroup(
        Text("谬误的本质 = 违反了结构的约束", font=DEFAULT_FONT, font_size=32),
        Text("静态知识: 告诉你 \"什么是错的\"", font=DEFAULT_FONT, font_size=32, color=GREY),
        Text("动态系统: 让你理解 \"为什么错\"", font=DEFAULT_FONT, font_size=32, color=GOLD),
        Text("理解系统才能真正应用知识", font=DEFAULT_FONT, font_size=32, color=BLUE)
    ).arrange(DOWN, buff=0.6).next_to(summary_title, DOWN, buff=1)
    
    cast["summary_act4"] = VGroup(summary_title, summary_lines)
    
    return cast
