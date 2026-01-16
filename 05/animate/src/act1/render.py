from manim import *
from src.utils import BaseScene
from src.act1.cast import get_act1_cast
import src.act1.scene1 as s1
import src.act1.scene2 as s2
import src.act1.scene3 as s3
import src.act1.scene4 as s4

class Act1(BaseScene):
    def construct(self):
        # Initialize base (debug label)
        super().construct()
        self.set_act(1)
        
        # 0. 初始化唯一可信的 Cast
        self.cast = get_act1_cast()
        
        # 1. Scene 1: 呈现句子
        self.next_section(name="Scene 1")
        s1.action(self, self.cast)
        
        # 2. Scene 2: 结构化 (Box & Arrow)
        self.next_section(name="Scene 2")
        s2.action(self, self.cast)
        
        # 3. Scene 3: 左侧聚焦与概念拆解
        self.next_section(name="Scene 3")
        s3.action(self, self.cast)
        
        # 4. Scene 4: 右侧聚焦与概念拆解
        self.next_section(name="Scene 4")
        s4.action(self, self.cast)
