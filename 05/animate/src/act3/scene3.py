from manim import *
from src.utils import *

class Act3Scene3(BaseScene):
    def construct(self):
        # 4个方块
        sq_a = Square(side_length=1.5).set_stroke(WHITE)
        sq_b = Square(side_length=1.5).set_stroke(WHITE)
        sq_c = Square(side_length=1.5).set_stroke(WHITE)
        sq_d = Square(side_length=1.5).set_stroke(WHITE)
        
        # 排列
        group = VGroup(sq_a, sq_b, sq_c, sq_d).arrange(RIGHT, buff=0.5)
        
        # 标签
        lbl_a = Text("A", font=DEFAULT_FONT).next_to(sq_a, DOWN)
        lbl_b = Text("B", font=DEFAULT_FONT).next_to(sq_b, DOWN)
        lbl_c = Text("C", font=DEFAULT_FONT).next_to(sq_c, DOWN)
        lbl_d = Text("D", font=DEFAULT_FONT).next_to(sq_d, DOWN)
        
        labels = VGroup(lbl_a, lbl_b, lbl_c, lbl_d)
        
        # 金色边框
        frame = SurroundingRectangle(VGroup(group, labels), color=GOLD, buff=0.3)
        frame_label = Text("单元", font=DEFAULT_FONT, color=GOLD).next_to(frame, UP)
        
        self.add(group, labels, frame, frame_label)
        
        # 循环动画
        # A亮 -> B亮 -> C亮 -> D亮 -> A亮
        
        run_time_per_step = 1.0
        
        # t=0 A亮
        self.play(sq_a.animate.set_fill(BLUE, opacity=1), run_time=0.5)
        self.wait(run_time_per_step)
        
        # t=1 A灭 B亮 (A->B时刻)
        self.play(
            sq_a.animate.set_fill(BLUE, opacity=0),
            sq_b.animate.set_fill(BLUE, opacity=1),
            run_time=0.5
        )
        # 标注: 正是这个时刻
        note = Text("A亮 -> B亮", font=DEFAULT_FONT, color=YELLOW).to_edge(UP)
        self.play(FadeIn(note, run_time=0.2))
        self.wait(run_time_per_step)
        self.play(FadeOut(note, run_time=0.2))

        # t=2 B灭 C亮
        self.play(
            sq_b.animate.set_fill(BLUE, opacity=0),
            sq_c.animate.set_fill(BLUE, opacity=1),
            run_time=0.5
        )
        self.wait(run_time_per_step)
        
        # t=3 C灭 D亮
        self.play(
            sq_c.animate.set_fill(BLUE, opacity=0),
            sq_d.animate.set_fill(BLUE, opacity=1),
            run_time=0.5
        )
        self.wait(run_time_per_step)
        
        # t=4 D灭 A亮 (回到开始)
        self.play(
            sq_d.animate.set_fill(BLUE, opacity=0),
            sq_a.animate.set_fill(BLUE, opacity=1),
            run_time=0.5
        )
        self.wait(1)
