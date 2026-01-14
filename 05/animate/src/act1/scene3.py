from manim import *
from src.utils import *

class Act1Scene3(BaseScene):
    def construct(self):
        # 聚焦: 「天下雨」
        # 重现上个场景的左半部分
        p_text = create_text("天下雨").move_to(ORIGIN)
        box_p = SurroundingRectangle(p_text, color=BLUE, buff=0.2)
        
        self.add(p_text, box_p)
        self.wait(1)
        
        # 动作: 命题内部开始发光，文字溶解
        # 浮现两个概念节点
        
        concept_sky = create_concept_node("天空", UP*1.5 + LEFT*0.5)
        concept_rain = create_concept_node("下雨", DOWN*1.5 + LEFT*0.5) # 原脚本是垂直分布
        # 脚本图示:
        #       ⭕️ 天空
        #        |
        #     (发生)
        #        |
        #       ⭕️ 下雨
        
        concept_sky = create_concept_node("天空", UP*1.5)
        concept_rain = create_concept_node("下雨", DOWN*1.5)
        
        line = DashedLine(concept_sky.get_bottom(), concept_rain.get_top(), color=BLUE_A)
        line_label = Text("(发生)", font=DEFAULT_FONT, font_size=20, color=BLUE_A).next_to(line, RIGHT)
        
        # 动画
        self.play(
            p_text.animate.set_opacity(0.2).scale(0.5).to_edge(DOWN), # 变透明并移到底部作为备注
            FadeOut(box_p),
            run_time=2
        )
        
        self.play(
            FadeIn(concept_sky),
            FadeIn(concept_rain),
            Create(line),
            Write(line_label),
            run_time=2
        )
        
        self.wait(5)
