from manim import *
from src.utils import *

class Act1Scene1(BaseScene):
    def construct(self):
        # 旁白: "语言是知识的表层形式"
        
        # 画面中心: 一句完整的话以文字形式出现
        text_str = "如果天下雨，那么地会湿"
        text = create_text(text_str)
        
        # 动画: 文字是平面的、黑色的、静态的 (在黑色背景上显示为白色以便可见，或遵循脚本"黑色"如果背景是白的。
        # 这里manim默认背景是黑，所以文字用白色。脚本说"黑色"可能是指打印在纸上的感觉，但在视频里通常反色。
        # 暂时保持白色文字。
        
        self.play(Write(text), run_time=2)
        self.wait(2)
        
        # 特征: 线性排列，像一条"符号链"
        # 感觉: 封闭的、不可分解的整体
        
        # 持续几秒
        self.wait(6)
