from manim import *
from src.utils import *

class Act3Scene2(BaseScene):
    def construct(self):
        # 快速拆解
        t_a = create_concept_node("A", LEFT*3)
        t_b = create_concept_node("B", RIGHT*3)
        arrow = Arrow(t_a.get_right(), t_b.get_left(), color=GOLD)
        label = Text("(导致)", font=DEFAULT_FONT, font_size=24, color=GOLD).next_to(arrow, UP)
        
        network = VGroup(t_a, t_b, arrow, label).move_to(ORIGIN)
        
        self.add(network)
        self.wait(1)
        
        # 画面冻结
        self.play(network.animate.set_color(COLOR_STATIC))
        note = Text("静态知识：A亮 导致 B亮", font=DEFAULT_FONT, color=COLOR_STATIC).to_edge(DOWN)
        self.play(Write(note))
        self.wait(3)
