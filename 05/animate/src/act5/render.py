from manim import *
from src.utils import *
from src.act5.cast import get_act5_cast
import src.act5.scene1 as s1
import src.act5.scene2 as s2
import src.act5.scene3 as s3
import src.act5.scene4 as s4
import src.act5.scene5 as s5
import src.act5.scene6 as s6

class Act5(BaseScene):
    def construct(self):
        # 0. Initialize Cast
        self.cast = get_act5_cast()
        
        # 1. Scene 1: Contrast
        self.next_section(name="Scene 1")
        s1.action(self, self.cast)
        
        # 2. Scene 2: Real Examples
        self.next_section(name="Scene 2")
        s2.action(self, self.cast)
        
        # 3. Scene 3: One Q, many Ps
        self.next_section(name="Scene 3")
        s3.action(self, self.cast)
        
        # 4. Scene 4: Strategy
        self.next_section(name="Scene 4")
        s4.action(self, self.cast)
        
        # 5. Scene 5: Medical Detail
        self.next_section(name="Scene 5")
        s5.action(self, self.cast)
        
        # 6. Scene 6: Summary
        self.next_section(name="Scene 6")
        s6.action(self, self.cast)
