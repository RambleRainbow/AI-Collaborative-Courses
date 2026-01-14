from manim import *
from src.utils import *

class Act3Scene1(BaseScene):
    def construct(self):
        # 画面中心: 一个新的知识以文字出现
        text = create_text("如果A亮，那么B会亮")
        
        self.play(Write(text))
        self.wait(1)
        
        # 旁白备注: "让我们用一个简化的例子来理解"
        note = Text("简化的例子", font=DEFAULT_FONT, font_size=32, color=GREY).to_edge(DOWN)
        self.play(Write(note))
        self.wait(3)
