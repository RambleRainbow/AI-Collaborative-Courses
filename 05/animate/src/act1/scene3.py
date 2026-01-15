from manim import *
from src.utils import *
from src.act1.cast import *

class Act1Scene3(BaseScene):
    def construct(self):
        # 1. 加载并恢复状态
        self.cast = get_act1_cast()
        self.load_state("act1_scene2")
        
        # 2. 场景初始化
        # 添加 Scene 2 遗留的可见元素
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

        # 4. 引入概念图 (已在 Cast 中定义)
        concept_sky = self.cast["concept_sky"]
        concept_rain = self.cast["concept_rain"]
        line = self.cast["line_left"]
        line_label = self.cast["line_label_left"]
        
        # self.play(
        #     text_p.animate.set_opacity(0.2).scale(0.5).to_edge(DOWN),
        #     FadeOut(box_p),
        #     run_time=2
        # )
        
        # 脚本图示:
        #       ⭕️ 天空
        #        |
        #     (发生)
        #        |
        #       ⭕️ 下雨
        
        # concept_sky = create_concept_node("天空", UP*1.5)
        # concept_rain = create_concept_node("下雨", DOWN*1.5)
        
        # line = DashedLine(concept_sky.get_bottom(), concept_rain.get_top(), color=BLUE_A)
        # line_label = Text("(发生)", font=DEFAULT_FONT, font_size=20, color=BLUE_A).next_to(line, RIGHT)
        
        # 动画
        # self.play(
        #     text_p.animate.set_opacity(0.2).scale(0.5).to_edge(DOWN), # 变透明并移到底部作为备注
        #     FadeOut(box_p),
        #     run_time=2
        # )
        
        self.play(
            FadeIn(concept_sky),
            FadeIn(concept_rain),
            Create(line),
            Write(line_label),
            run_time=2
        )
        
        self.wait(5)
