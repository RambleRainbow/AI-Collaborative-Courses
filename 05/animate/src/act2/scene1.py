from manim import *
from src.utils import *

class Act2Scene1(BaseScene):
    def construct(self):
        # 承接Act1Scene5的画面: 概念网络悬浮
        #      ⭕️ 天空               ⭕️ 地面
        #        |                     |
        #     (发生)              (具有状态)
        #        |                     |
        #      ⭕️ 下雨  ─────→      ⭕️ 湿
        #             (因果)
        
        # 快速重建网络 (实际项目中最好把构建代码封装成函数复用，这里简单起见快速重写)
        c_sky = create_concept_node("天空", UP*2 + LEFT*4)
        c_rain = create_concept_node("下雨", LEFT*4)
        l_left = DashedLine(c_sky.get_bottom(), c_rain.get_top(), color=BLUE_A)
        # ...省略部分细节，主要构建整体结构
        
        c_ground = create_concept_node("地面", UP*2 + RIGHT*4)
        c_wet = create_concept_node("湿", RIGHT*4)
        l_right = DashedLine(c_ground.get_bottom(), c_wet.get_top(), color=BLUE_A)
        
        arrow = Arrow(c_rain.get_right(), c_wet.get_left(), color=GOLD)
        
        network = VGroup(c_sky, c_rain, l_left, c_ground, c_wet, l_right, arrow)
        # 居中显示
        network.move_to(ORIGIN)
        
        self.add(network)
        self.wait(1)
        
        # 动作: 网络"冻结"，变灰白
        # Manim中可以用set_color修改颜色
        self.play(
            network.animate.set_color(COLOR_STATIC),
            run_time=2
        )
        
        # 问号出现
        q_mark = Text("?", font_size=96, color=RED).next_to(network, RIGHT)
        self.play(Write(q_mark))
        
        # 旁白备注: "但这只是某个瞬间的关系快照"
        note = Text("只是某个瞬间的关系快照", font=DEFAULT_FONT, font_size=36, color=WHITE).to_edge(DOWN)
        self.play(Write(note))
        
        self.wait(3)
