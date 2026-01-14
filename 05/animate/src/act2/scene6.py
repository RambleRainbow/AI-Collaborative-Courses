from manim import *
from src.utils import *

class Act2Scene6(BaseScene):
    def construct(self):
        # 分屏
        line = Line(UP*4, DOWN*4)
        
        # 左侧: 静态知识
        left_title = Text("静态知识观", font=DEFAULT_FONT).move_to(UP*3 + LEFT*3.5)
        left_content = Text("孤立命题\n固化箭头", font=DEFAULT_FONT, font_size=32).next_to(left_title, DOWN, buff=1)
        left_tag = Text("片面的、死的", font=DEFAULT_FONT, color=GREY).next_to(left_content, DOWN)
        
        # 右侧: 动态系统
        right_title = Text("系统动态观", font=DEFAULT_FONT).move_to(UP*3 + RIGHT*3.5)
        right_content = Text("循环系统\n流量变化", font=DEFAULT_FONT, font_size=32).next_to(right_title, DOWN, buff=1)
        right_tag = Text("完整的、活的", font=DEFAULT_FONT, color=GOLD).next_to(right_content, DOWN)
        
        self.play(Create(line))
        self.play(Write(left_title), Write(left_content), Write(left_tag))
        self.play(Write(right_title), Write(right_content), Write(right_tag))
        
        # 总结
        summary = Text("系统 = 动态运作机制\n知识 = 某时刻的关系描述", font=DEFAULT_FONT, color=YELLOW).to_edge(DOWN)
        self.play(Write(summary))
        
        self.wait(5)
