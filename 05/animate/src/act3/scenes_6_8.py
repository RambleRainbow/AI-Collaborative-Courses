from manim import *
from src.utils import *

class Act3Scene6(BaseScene):
    def construct(self):
        # 场景6: 左侧静态 右侧动态 对比
        
        # 左 (Text)
        left_t = Text("A亮 -> B亮", font=DEFAULT_FONT, color=COLOR_STATIC).shift(LEFT*4)
        left_lbl = Text("静态描述", font=DEFAULT_FONT, font_size=24).next_to(left_t, DOWN)
        
        # 右 (Loop)
        # 简化版循环图
        right_loop = Circle(radius=1.5, color=COLOR_DYNAMIC).shift(RIGHT*4)
        dots = VGroup(*[Dot(point=right_loop.point_from_proportion(i/4), color=WHITE) for i in range(4)])
        right_lbl = Text("循环机制", font=DEFAULT_FONT, font_size=24).next_to(right_loop, DOWN)
        
        self.play(FadeIn(left_t), FadeIn(left_lbl))
        self.play(Create(right_loop), FadeIn(dots), FadeIn(right_lbl))
        
        # 连接
        arrow = DoubleArrow(left_t.get_right(), right_loop.get_left(), color=GOLD)
        self.play(Create(arrow))
        
        insight = Text("片面观察 vs 完整机制", font=DEFAULT_FONT, font_size=36, color=YELLOW).to_edge(DOWN)
        self.play(Write(insight))
        self.wait(3)

class Act3Scene7(BaseScene):
    def construct(self):
        # 场景7: 为什么不能停留在静态
        # 预测例子
        t1 = Text("只记静态: 看到A -> 期待B", font=DEFAULT_FONT, font_size=32).shift(UP*1)
        t2 = Text("实际机制: A -> B -> C -> D", font=DEFAULT_FONT, font_size=32)
        t3 = Text("如果在C处看到A(误判), 期待B? 错!", font=DEFAULT_FONT, font_size=32, color=RED).shift(DOWN*1)
        
        self.play(Write(t1))
        self.wait(1)
        self.play(Write(t2))
        self.wait(1)
        self.play(Write(t3))
        self.wait(3)

class Act3Scene8(BaseScene):
    def construct(self):
        # 总结
        title = create_title("第三幕总结")
        
        lines = VGroup(
            Text("真实世界 = 复杂动态", font=DEFAULT_FONT),
            Text("单元机制 = 可识别的规律", font=DEFAULT_FONT),
            Text("语言知识 = 机制的简化描述", font=DEFAULT_FONT),
            Text("应用 = 识别 + 理解 + 时序", font=DEFAULT_FONT, color=GOLD)
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(lines), run_time=4)
        self.wait(3)
