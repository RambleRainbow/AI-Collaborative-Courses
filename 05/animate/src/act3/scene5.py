from manim import *
from src.utils import *
import random

class Act3Scene5(BaseScene):
    # 复用Scene4的逻辑，但这里重点是降噪
    def construct(self):
        squares = VGroup()
        for i in range(16):
            sq = Square(side_length=1).set_stroke(WHITE)
            squares.add(sq)
        squares.arrange_in_grid(4, 4, buff=0.2).scale(0.8)
        
        unit_indices = [0, 1, 5, 4]
        other_indices = [i for i in range(16) if i not in unit_indices]
        
        # 初始状态：已经识别出单元
        unit_group = VGroup(*[squares[i] for i in unit_indices])
        frame = SurroundingRectangle(unit_group, color=GOLD)
        
        self.add(squares, frame)
        
        # 降噪动画
        # others透明度降低
        anims = []
        for i in other_indices:
            anims.append(squares[i].animate.set_stroke(opacity=0.3).set_fill(opacity=0.1)) # 变淡
        
        label = Text("过滤噪音", font=DEFAULT_FONT, color=WHITE).to_edge(DOWN)
        
        self.play(*anims, Write(label), run_time=2)
        
        # 继续单元循环，强调清晰度
        cycle = unit_indices
        for step in range(4):
             # 只动单元，others保持静止或微弱闪烁（这里简单起见静止）
            active_idx = cycle[step]
            u_anims = []
            for u_idx in unit_indices:
                if u_idx == active_idx:
                    u_anims.append(squares[u_idx].animate.set_fill(BLUE, opacity=1))
                else:
                    u_anims.append(squares[u_idx].animate.set_fill(BLACK, opacity=0))
            self.play(*u_anims, run_time=0.8)
            
        self.wait(1)
