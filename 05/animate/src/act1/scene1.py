from manim import *
from src.utils import *
from src.act1.cast import *

class Act1Scene1(BaseScene):
    def construct(self):
        # 1. 加载所有角色
        self.cast = get_act1_cast()
        
        # 组装句子 (方便动画)
        text = VGroup(
            self.cast["text_if"],
            self.cast["text_p"],
            self.cast["text_comma"],
            self.cast["text_then"],
            self.cast["text_q"]
        )
        
        # 2. 动画
        self.play(Write(text), run_time=2)
        self.wait(2)
        
        self.wait(2)
        
        # 3. 保存状态 (保存整组 Cast)
        self.save_state("act1_scene1")
