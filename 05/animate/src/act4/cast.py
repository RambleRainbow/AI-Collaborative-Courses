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
    
    # --- 6. Scene 8: Three Syllogisms Demo (Multiple Inferences Each) ---
    # Three parallel machines, each demonstrating multiple valid forms
    machine_cat = ReasoningMachine().scale(0.55).shift(LEFT * 4.5)
    machine_dis = ReasoningMachine().scale(0.55).shift(ORIGIN)
    machine_hyp = ReasoningMachine().scale(0.55).shift(RIGHT * 4.5)
    
    cast["machine_cat"] = machine_cat
    cast["machine_dis"] = machine_dis
    cast["machine_hyp"] = machine_hyp
    
    # Labels
    lbl_cat = Text("定言三段论", font=DEFAULT_FONT, font_size=24, color=BLUE).next_to(machine_cat, UP, buff=0.3)
    lbl_dis = Text("选言三段论", font=DEFAULT_FONT, font_size=24, color=GREEN).next_to(machine_dis, UP, buff=0.3)
    lbl_hyp = Text("假言三段论", font=DEFAULT_FONT, font_size=24, color=GOLD).next_to(machine_hyp, UP, buff=0.3)
    
    cast["syl_labels"] = VGroup(lbl_cat, lbl_dis, lbl_hyp)
    
    # === Categorical Syllogism (定言三段论) - Two Forms ===
    # Form 1 (Barbara): ∀M→P, S∈M ⊢ S∈P
    cat1_major = Text("∀x(M(x) → P(x))", font=DEFAULT_FONT, font_size=18)
    cat1_minor = Text("M(s)", font=DEFAULT_FONT, font_size=18)
    cat1_conc = Text("P(s)", font=DEFAULT_FONT, font_size=18)
    cast["cat1"] = (cat1_major, cat1_minor, cat1_conc)
    
    # Form 2 (Celarent): ∀M→¬P, S∈M ⊢ S∉P
    cat2_major = Text("∀x(M(x) → ¬P(x))", font=DEFAULT_FONT, font_size=18)
    cat2_minor = Text("M(s)", font=DEFAULT_FONT, font_size=18)
    cat2_conc = Text("¬P(s)", font=DEFAULT_FONT, font_size=18)
    cast["cat2"] = (cat2_major, cat2_minor, cat2_conc)
    
    # === Disjunctive Syllogism (选言三段论) - Two Forms ===
    # Form 1: P ∨ Q, ¬P ⊢ Q
    dis1_major = Text("P ∨ Q", font=DEFAULT_FONT, font_size=18)
    dis1_minor = Text("¬P", font=DEFAULT_FONT, font_size=18)
    dis1_conc = Text("Q", font=DEFAULT_FONT, font_size=18)
    cast["dis1"] = (dis1_major, dis1_minor, dis1_conc)
    
    # Form 2: P ∨ Q, ¬Q ⊢ P
    dis2_major = Text("P ∨ Q", font=DEFAULT_FONT, font_size=18)
    dis2_minor = Text("¬Q", font=DEFAULT_FONT, font_size=18)
    dis2_conc = Text("P", font=DEFAULT_FONT, font_size=18)
    cast["dis2"] = (dis2_major, dis2_minor, dis2_conc)
    
    # === Hypothetical Syllogism (假言三段论) - Two Forms ===
    # Form 1 (Modus Ponens): P → Q, P ⊢ Q
    hyp1_major = Text("P → Q", font=DEFAULT_FONT, font_size=18)
    hyp1_minor = Text("P", font=DEFAULT_FONT, font_size=18)
    hyp1_conc = Text("Q", font=DEFAULT_FONT, font_size=18)
    cast["hyp1"] = (hyp1_major, hyp1_minor, hyp1_conc)
    
    # Form 2 (Modus Tollens): P → Q, ¬Q ⊢ ¬P
    hyp2_major = Text("P → Q", font=DEFAULT_FONT, font_size=18)
    hyp2_minor = Text("¬Q", font=DEFAULT_FONT, font_size=18)
    hyp2_conc = Text("¬P", font=DEFAULT_FONT, font_size=18)
    cast["hyp2"] = (hyp2_major, hyp2_minor, hyp2_conc)
    
    return cast
