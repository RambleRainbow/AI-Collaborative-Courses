
from manim import *
from src.utils import *
from src.act1.cast import *

class Act1Scene2(BaseScene):
    def construct(self):
        # 1. 加载并恢复状态
        self.cast = get_act1_cast()
        self.load_state("act1_scene1")
        
        # 2. 场景初始化: 添加可见部分
        # Scene 1 结束时，所有文字都是可见的，所以我们要把它们 add 到场景中
        # 即使位置已经被 load_state 更新，我们需要把对象本身 add 进去
        text_parts = [
            self.cast["text_if"],
            self.cast["text_p"],
            self.cast["text_comma"],
            self.cast["text_then"],
            self.cast["text_q"]
        ]

        # self.play(Write(VGroup(*text_parts)), run_time=2)
        self.add(*text_parts)
        self.wait(1)
        
        # 3. 动画逻辑
        part_p = self.cast["text_p"]
        part_q = self.cast["text_q"]
        
        # 动作: 隐藏连接词
        self.play(
            FadeOut(self.cast["text_if"]),
            FadeOut(self.cast["text_comma"]),
            FadeOut(self.cast["text_then"]),
            run_time=1
        )
        
        # 移动命题
        self.play(
            part_p.animate.move_to(LEFT * 3),
            part_q.animate.move_to(RIGHT * 3),
            run_time=2
        )
        
        # 获取新元素 (已在 get_act1_cast 中定义)
        arrow = self.cast["arrow"]
        box_p = self.cast["box_p"]
        box_q = self.cast["box_q"]
        label_p = self.cast["label_p"]
        label_q = self.cast["label_q"]
        label_rel = self.cast["label_rel"]
        
        # 此时 arrow 等的位置是默认的 (在 cast.py 中定义的)
        # 恰好 cast.py 中的定义就是基于 part_p/q 默认相对位置
        # 但 part_p/q 上一步刚刚移动了。
        # Arrow/Boxes 的 .next_to 关系是**定义时**计算的，不会自动跟随。
        # 所以我们需要**重新定位**这些结构元素以匹配当前 part_p/q 的新位置。
        
        arrow.next_to(part_p, RIGHT)
        arrow.put_start_and_end_on(part_p.get_right() + RIGHT*0.5, part_q.get_left() - RIGHT*0.5)
        
        box_p.move_to(part_p)
        box_q.move_to(part_q)
        
        label_p.next_to(box_p, UP)
        label_q.next_to(box_q, UP)
        label_rel.next_to(arrow, UP)
        
        self.play(Create(arrow), run_time=1)
        
        self.play(
            Create(box_p),
            Create(box_q),
            Write(label_p),
            Write(label_q),
            Write(label_rel),
            run_time=2
        )
        
        self.wait(2)
        
        # --- 状态修复 (Fix State Artifacts) ---
        # 1. Arrow: 确保 Tip 可见 (VGroup 默认读取 Line 的 fill=0，会导致 Tip 变透明)
        arrow.set_fill(opacity=1)
        
        # 2. Labels: 确保颜色正确 (修复 Write 动画可能的颜色残留)
        label_p.set_color(GREY)
        label_q.set_color(GREY)
        label_rel.set_color(GOLD)
        
        # 4. 保存状态
        self.save_state("act1_scene2")
