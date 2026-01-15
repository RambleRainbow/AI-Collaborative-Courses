from manim import *
from src.utils import BaseScene
from src.act2.cast import get_act2_cast
import src.act2.scene1 as s1
import src.act2.scene2 as s2
import src.act2.scene3 as s3
import src.act2.scene4 as s4
import src.act2.scene5 as s5
import src.act2.scene6 as s6

class Act2(BaseScene):
    def construct(self):
        # 0. 初始化唯一可信的 Cast
        self.cast = get_act2_cast()
        
        # 1. Scene 1: 静态限制
        self.next_section(name="Scene 1")
        s1.action(self, self.cast)
        
        # 2. Scene 2: 系统显现
        self.next_section(name="Scene 2")
        s2.action(self, self.cast)
        
        # 3. Scene 3: 水循环结构
        self.next_section(name="Scene 3")
        s3.action(self, self.cast)
        
        # 4. Scene 4: 动态运行
        self.next_section(name="Scene 4")
        s4.action(self, self.cast)
        
        # 5. Scene 5: 静态定位
        self.next_section(name="Scene 5")
        s5.action(self, self.cast)
        
        # 6. Scene 6: 真相对比
        self.next_section(name="Scene 6")
        s6.action(self, self.cast)
