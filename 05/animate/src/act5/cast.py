from manim import *
from src.utils import *

def get_act5_cast():
    cast = {}
    
    # --- 1. Scene 1: Forward vs Reverse ---
    fwd_label = Text("原因 (P) -> 结果 (Q)", font=DEFAULT_FONT, font_size=32)
    fwd_arrow = Arrow(LEFT, RIGHT, color=BLUE).next_to(fwd_label, DOWN)
    fwd_group = VGroup(fwd_label, fwd_arrow).shift(LEFT * 3 + UP * 1)
    
    rev_label = Text("结果 (Q) -> 原因 (?)", font=DEFAULT_FONT, font_size=32)
    rev_arrow = Arrow(RIGHT, LEFT, color=RED).next_to(rev_label, DOWN)
    rev_group = VGroup(rev_label, rev_arrow).shift(RIGHT * 3 + UP * 1)
    
    cast["logic_dir"] = VGroup(fwd_group, rev_group)

    # --- 2. Scene 2: Real Examples ---
    # Medical
    med_icon = VGroup(
        Circle(radius=0.5, color=WHITE),
        Line(UP*0.3, DOWN*0.3), Line(LEFT*0.3, RIGHT*0.3)
    ).set_color(RED)
    med_txt = Text("医疗诊断: 发烧(Q) -> 病因(P?)", font=DEFAULT_FONT, font_size=24)
    med_group = VGroup(med_icon, med_txt).arrange(RIGHT).shift(UP * 2)
    
    # IT
    it_icon = Square(side_length=0.8, color=GREY).add(Text("!", color=RED).scale(0.8))
    it_txt = Text("系统崩溃: 报错(Q) -> 模块(P?)", font=DEFAULT_FONT, font_size=24)
    it_group = VGroup(it_icon, it_txt).arrange(RIGHT).shift(ORIGIN)
    
    # Business
    biz_icon = VGroup(Line(ORIGIN, UR), Line(UR, UR+RIGHT*0.5+UP*0.2)).set_color(GREEN)
    biz_txt = Text("商业分析: 销量(Q) -> 因素(P?)", font=DEFAULT_FONT, font_size=24)
    biz_group = VGroup(biz_icon, biz_txt).arrange(RIGHT).shift(DOWN * 2)
    
    cast["real_examples"] = VGroup(med_group, it_group, biz_group)

    # --- 3. Scene 3 & 4: Many P -> One Q ---
    # Shifted down and scaled to fit within screen bounds
    node_q = create_concept_node("Q (结果)", DOWN * 0.5, color=GOLD)
    ps = VGroup()
    arrows = VGroup()
    radius = 2.5  # Reduced from 4 to fit screen
    for i in range(5):
        angle = PI - (i * PI / 4)
        pos = node_q.get_center() + radius * np.array([np.cos(angle), np.sin(angle), 0])
        p = create_concept_node(f"P{i+1}", pos, color=BLUE)
        # Arrow points toward center with buff to stop at node edge
        arr = Arrow(p.get_center(), node_q.get_center(), buff=0.5, color=GREY_C)
        ps.add(p)
        arrows.add(arr)
    
    cast["fan_in_net"] = VGroup(ps, arrows, node_q)

    # --- 5. Scene 5: Strategy Comparison ---
    strat_title = create_title("应对策略")
    strat_left = RoundedRectangle(width=5.5, height=4.5, color=BLUE_E).shift(LEFT*3.5 + DOWN*0.5)
    strat_right = RoundedRectangle(width=5.5, height=4.5, color=GREY_E).shift(RIGHT*3.5 + DOWN*0.5)
    
    label_sys = Text("系统机制策略", font=DEFAULT_FONT, font_size=28, color=BLUE).next_to(strat_left, UP)
    label_static = Text("静态穷举策略", font=DEFAULT_FONT, font_size=28, color=GREY).next_to(strat_right, UP)
    
    cast["strat_ui"] = VGroup(strat_left, strat_right, label_sys, label_static, strat_title)
    
    # Items for strategies
    sys_icon = LightingUnit(size=1.5).move_to(strat_left.get_center())
    static_line = Text("P1? P2? P3?...", font=DEFAULT_FONT, font_size=24).move_to(strat_right.get_center())
    
    cast["sys_icon"] = sys_icon
    cast["static_line"] = static_line

    # --- 6. Scene 7: Summary ---
    summary_act5 = VGroup(
        Text("现实挑战: 结果已知，诱因难寻", font=DEFAULT_FONT),
        Text("机制作用: 锁定单元，缩小搜索空间", font=DEFAULT_FONT, color=BLUE),
        Text("知识不仅是关联，更是过滤噪音的漏斗", font=DEFAULT_FONT, color=GOLD)
    ).arrange(DOWN, buff=0.8).center()
    
    cast["summary_act5"] = summary_act5
    
    return cast
