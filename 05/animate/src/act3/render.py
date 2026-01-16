from manim import *
from src.utils import BaseScene
from src.act3.cast import get_act3_cast
import src.act3.scene1 as s1
import src.act3.scene2 as s2
import src.act3.scene3 as s3
import src.act3.scene4 as s4
import src.act3.scene5 as s5
import src.act3.scene6 as s6

class Act3(BaseScene):
    def construct(self):
        # Initialize base (debug label)
        super().construct()
        self.set_act(3)
        
        # 0. Initialize Cast
        self.cast = get_act3_cast()
        
        # 1. Scene 1: Introduction
        self.next_section(name="Scene 1")
        s1.action(self, self.cast)
        
        # 2. Scene 2: Static Knowledge
        self.next_section(name="Scene 2")
        s2.action(self, self.cast)
        
        # 3. Scene 3: Simple Mechanism
        self.next_section(name="Scene 3")
        s3.action(self, self.cast)
        
        # 4. Scene 4: Chaos vs Unit
        self.next_section(name="Scene 4")
        s4.action(self, self.cast)
        
        # 5. Scene 5: Filter Noise
        self.next_section(name="Scene 5")
        s5.action(self, self.cast)
        
        # 6. Scene 6: Mechanism Comparison
        self.next_section(name="Scene 6")
        s6.action(self, self.cast)
