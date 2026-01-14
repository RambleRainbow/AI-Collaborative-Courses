from manim import *
from src.utils import *

class Act2Scene2(BaseScene):
    def construct(self):
        # 初始: 静态网络
        # 简单用一个方块代表刚才的网络
        static_net = Rectangle(width=6, height=4, color=COLOR_STATIC)
        label = Text("静态知识网络", font=DEFAULT_FONT, color=COLOR_STATIC).move_to(static_net)
        group = VGroup(static_net, label)
        
        self.add(group)
        self.wait(1)
        
        # 动作: 镜头拉远 (实际上是物体缩小)
        # 周围显现更大结构
        
        # 创建背景系统的大圆
        system_circle = Circle(radius=6, color=COLOR_DYNAMIC)
        system_label = Text("真实动态系统", font=DEFAULT_FONT, font_size=48, color=COLOR_DYNAMIC).next_to(system_circle, UP)
        
        self.play(
            group.animate.scale(0.2).move_to(LEFT*4), # 缩小并移动到一边
            FadeIn(system_circle),
            Write(system_label),
            run_time=3
        )
        
        note = Text("真实世界是动态运转的系统", font=DEFAULT_FONT, font_size=36).to_edge(DOWN)
        self.play(Write(note))
        
        self.wait(3)
