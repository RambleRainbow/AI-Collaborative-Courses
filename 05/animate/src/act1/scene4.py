from manim import *
from src.utils import *
from src.act1.cast import *

class Act1Scene4(BaseScene):
    def construct(self):
        # 1. 加载并恢复状态
        self.cast = get_act1_cast()
        self.load_state("act1_scene2")
        
        # 2. 场景初始化 (继承 Scene 2)
        self.add(
            self.cast["text_p"],
            self.cast["text_q"],
            self.cast["arrow"],
            self.cast["box_p"],
            self.cast["box_q"],
            self.cast["label_p"],
            self.cast["label_q"],
            self.cast["label_rel"]
        )
        self.wait(1)

        # 3. 动画: 聚焦右侧
        part_q = self.cast["text_q"]
        box_q = self.cast["box_q"]
        
        self.play(
            FadeOut(self.cast["text_p"]),
            FadeOut(self.cast["arrow"]),
            FadeOut(self.cast["box_p"]),
            FadeOut(self.cast["label_p"]),
            FadeOut(self.cast["label_q"]),
            FadeOut(self.cast["label_rel"]),
            part_q.animate.move_to(ORIGIN),
            box_q.animate.move_to(ORIGIN),
            run_time=2
        )
        
        # 4. 引入概念图
        concept_ground = self.cast["concept_ground"]
        concept_wet = self.cast["concept_wet"]
        line = self.cast["line_right"]
        line_label = self.cast["line_label_right"]
        
        self.play(
            part_q.animate.set_opacity(0.2).scale(0.5).to_edge(DOWN),
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
        self.save_state("act1_scene4")
        
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
