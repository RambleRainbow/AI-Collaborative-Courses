from manim import *
from src.utils import *
import random

class Act3Scene4(BaseScene):
    def construct(self):
        # 16个方块 4x4
        squares = VGroup()
        for i in range(16):
            sq = Square(side_length=1).set_stroke(WHITE)
            squares.add(sq)
        
        squares.arrange_in_grid(4, 4, buff=0.2).scale(0.8)
        self.add(squares)
        
        # 假设左上角4个是单元(0,1,4,5) (实际上grid排列是行优先)
        # 索引 0,1,2,3 (row1)
        # 4,5,6,7 (row2)
        # ...
        # 我们用 0,1,4,5 作为 "有序单元"
        # 0->1->5->4->0 (顺时针)
        
        unit_indices = [0, 1, 5, 4] 
        other_indices = [i for i in range(16) if i not in unit_indices]
        
        # chaos phase
        # 简单模拟：随机闪烁
        # 由于Manim是预生成的，我们循环几次
        
        # 第一次：全随机
        for _ in range(3):
            anims = []
            for i in range(16):
                if random.random() > 0.5:
                    anims.append(squares[i].animate.set_fill(GREY, opacity=0.8))
                else:
                    anims.append(squares[i].animate.set_fill(BLACK, opacity=0))
            self.play(*anims, run_time=0.5)
        
        # 单元识别：显示金框
        # 计算这4个方块的边界
        unit_group = VGroup(*[squares[i] for i in unit_indices])
        frame = SurroundingRectangle(unit_group, color=GOLD)
        label = Text("单元识别", font=DEFAULT_FONT, color=GOLD).next_to(frame, UP)
        
        self.play(Create(frame), Write(label))
        
        # 有序运行
        # 循环动画
        # t=0: idx0亮, others random
        # t=1: idx1亮, others random
        # t=2: idx5亮, others random
        # t=3: idx4亮, others random
        
        cycle = unit_indices # 0, 1, 5, 4
        
        for step in range(4):
            anims = []
            
            # Unit logic
            active_idx = cycle[step]
            for u_idx in unit_indices:
                if u_idx == active_idx:
                    anims.append(squares[u_idx].animate.set_fill(BLUE, opacity=1))
                else:
                    anims.append(squares[u_idx].animate.set_fill(BLACK, opacity=0))
            
            # Chaos logic for others
            for o_idx in other_indices:
                if random.random() > 0.5:
                    anims.append(squares[o_idx].animate.set_fill(GREY, opacity=0.5))
                else:
                    anims.append(squares[o_idx].animate.set_fill(BLACK, opacity=0))
            
            self.play(*anims, run_time=0.8)
            
        self.wait(1)
