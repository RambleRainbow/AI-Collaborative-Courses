from manim import *
from src.utils import *

class Act1Scene4(BaseScene):
    def construct(self):
        # 聚焦: 「地会湿」
        # 基本同Scene3
        q_text = create_text("地会湿").move_to(ORIGIN)
        box_q = SurroundingRectangle(q_text, color=BLUE, buff=0.2)
        
        self.add(q_text, box_q)
        self.wait(1)
        
        # 概念提取
        # Graph: 地面 --(具有状态)--> 湿
        
        concept_ground = create_concept_node("地面", UP*1.5)
        concept_wet = create_concept_node("湿", DOWN*1.5)
        
        line = DashedLine(concept_ground.get_bottom(), concept_wet.get_top(), color=BLUE_A)
        line_label = Text("(具有状态)", font=DEFAULT_FONT, font_size=20, color=BLUE_A).next_to(line, RIGHT)
        
        self.play(
            q_text.animate.set_opacity(0.2).scale(0.5).to_edge(DOWN),
            FadeOut(box_q),
            run_time=2
        )
        
        self.play(
            FadeIn(concept_ground),
            FadeIn(concept_wet),
            Create(line),
            Write(line_label),
            run_time=2
        )
        
        self.wait(5)
