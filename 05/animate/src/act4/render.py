from manim import *
from src.utils import *
from src.act4.cast import get_act4_cast
import src.act4.scene1 as s1
import src.act4.scene2 as s2
import src.act4.scene3 as s3
import src.act4.scene4 as s4
import src.act4.scene5 as s5
import src.act4.scene6 as s6
import src.act4.scene7 as s7
import src.act4.scene8 as s8

class Act4(BaseScene):
    def construct(self):
        # Initialize base (debug label)
        super().construct()
        self.set_act(4)
        
        # 0. Initialize Cast
        self.cast = get_act4_cast()
        
        # 1. Scene 1: Fallacy Intro
        self.next_section(name="Scene 1")
        s1.action(self, self.cast)
        
        # 2. Scene 2: Static Disassembly
        self.next_section(name="Scene 2")
        s2.action(self, self.cast)
        
        # 3. Scene 3: Ontological Structure
        self.next_section(name="Scene 3")
        s3.action(self, self.cast)
        
        # 4. Scene 4: Correct Reasoning (MP)
        self.next_section(name="Scene 4")
        s4.action(self, self.cast)
        
        # 5. Scene 5: Fallacy (AC)
        self.next_section(name="Scene 5")
        s5.action(self, self.cast)
        
        # 6. Scene 6: Comparison
        self.next_section(name="Scene 6")
        s6.action(self, self.cast)
        
        # 7. Scene 7: Real App
        self.next_section(name="Scene 7")
        s7.action(self, self.cast)
        
        # 8. Scene 8: Summary
        self.next_section(name="Scene 8")
        s8.action(self, self.cast)
