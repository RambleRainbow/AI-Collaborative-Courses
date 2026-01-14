from manim import *
from src.utils import *

class Act1Scene5(BaseScene):
    def construct(self):
        # 重组: 这里需要把Scene2,3,4的元素组合起来
        # 布局:
        #      ⭕️ 天空               ⭕️ 地面
        #        |                     |
        #     (发生)              (具有状态)
        #        |                     |
        #      ⭕️ 下雨  ─────→      ⭕️ 湿
        #             (因果)
        
        # 左侧组
        c_sky = create_concept_node("天空", UP*2 + LEFT*4)
        c_rain = create_concept_node("下雨", LEFT*4)
        l_left = DashedLine(c_sky.get_bottom(), c_rain.get_top(), color=BLUE_A)
        txt_left = Text("(发生)", font=DEFAULT_FONT, font_size=20, color=BLUE_A).next_to(l_left, LEFT)
        
        group_left = VGroup(c_sky, c_rain, l_left, txt_left)
        
        # 右侧组
        c_ground = create_concept_node("地面", UP*2 + RIGHT*4)
        c_wet = create_concept_node("湿", RIGHT*4)
        l_right = DashedLine(c_ground.get_bottom(), c_wet.get_top(), color=BLUE_A)
        txt_right = Text("(具有状态)", font=DEFAULT_FONT, font_size=20, color=BLUE_A).next_to(l_right, RIGHT)
        
        group_right = VGroup(c_ground, c_wet, l_right, txt_right)
        
        # 初始：先分别显示
        self.add(group_left, group_right)
        
        # 因果箭头
        arrow = Arrow(c_rain.get_right(), c_wet.get_left(), color=GOLD)
        arrow_label = Text("(因果)", font=DEFAULT_FONT, font_size=24, color=GOLD).next_to(arrow, DOWN)
        
        self.play(
            GrowArrow(arrow),
            Write(arrow_label),
            run_time=2
        )
        
        # 标注: "知识的深层结构：概念+关系的网络"
        note = Text("知识的深层结构：概念+关系的网络", font=DEFAULT_FONT, font_size=36, color=YELLOW).to_edge(DOWN)
        self.play(Write(note))
        
        self.wait(5)
