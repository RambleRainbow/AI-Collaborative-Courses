from manim import *
from src.utils import *

class Act2Scene5(BaseScene):
    def construct(self):
        # 暂停在 t=2 时刻
        # 提取片段: Rain -> Ground Increasing
        
        text_event = Text("降雨流 > 0  --->  地表水量增加", font=DEFAULT_FONT).move_to(ORIGIN)
        
        # 静态知识浮现
        static_k = Text("如果天下雨，那么地会湿", font=DEFAULT_FONT, color=COLOR_STATIC).next_to(text_event, UP, buff=1)
        
        self.play(Write(text_event))
        self.play(FadeIn(static_k))
        
        # 连接
        lines = Lines(static_k.get_bottom(), text_event.get_top(), color=GOLD)
        self.play(Create(lines))
        
        label = Text("系统在 t=2 时刻的局部状态关系", font=DEFAULT_FONT, font_size=24, color=YELLOW).next_to(lines, RIGHT)
        self.play(Write(label))
        
        self.wait(4)
