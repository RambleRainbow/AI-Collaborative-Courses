from manim import *
from src.utils import *
from src.act6.cast import get_act6_cast
import src.act6.scene1 as s1
import src.act6.scene2 as s2
import src.act6.scene3 as s3

class Act6(BaseScene):
    def construct(self):
        # Initialize base (debug label)
        super().construct()
        self.set_act(6)
        
        # 0. Initialize Cast
        self.cast = get_act6_cast()
        
        # 1. Scene 1: Meta Layers
        self.next_section(name="Scene 1")
        s1.action(self, self.cast)
        
        # 2. Scene 2: Meta Engine
        self.next_section(name="Scene 2")
        s2.action(self, self.cast)
        
        # 3. Scene 3: Finale
        self.next_section(name="Scene 3")
        s3.action(self, self.cast)
