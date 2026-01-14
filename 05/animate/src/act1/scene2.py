from manim import *
from src.utils import *

class Act1Scene2(BaseScene):
    def construct(self):
        # 初始状态 (接上个场景)
        text_str = "如果天下雨，那么地会湿"
        # 手动构建各部分以便拆分
        # "如果"(0,1) "天下雨"(2,3,4) "，"(5) "那么"(6,7) "地会湿"(8,9,10)
        # 这里的索引取决于中文字符。
        # 更简单的方法是创建三个Text对象
        
        part1 = create_text("如果", font_size=40).shift(LEFT*3)
        part_p = create_text("天下雨").next_to(part1, RIGHT)
        part_comma = create_text("，", font_size=40).next_to(part_p, RIGHT)
        part2 = create_text("那么", font_size=40).next_to(part_comma, RIGHT)
        part_q = create_text("地会湿").next_to(part2, RIGHT)
        
        full_sentence = VGroup(part1, part_p, part_comma, part2, part_q)
        full_sentence.move_to(ORIGIN)
        
        self.add(full_sentence)
        self.wait(1)
        
        # 动作: 句子开始断裂
        # 文字分裂成两个发光的片段
        
        # 隐藏连接词
        self.play(
            FadeOut(part1),
            FadeOut(part_comma),
            FadeOut(part2),
            run_time=1
        )
        
        # 移动命题
        target_p = part_p.generate_target()
        target_p.move_to(LEFT * 3)
        
        target_q = part_q.generate_target()
        target_q.move_to(RIGHT * 3)
        
        # 箭头
        arrow = Arrow(LEFT, RIGHT, color=GOLD)
        arrow.next_to(target_p, RIGHT)
        # 调整箭头长度使其连接两个命题
        arrow.put_start_and_end_on(target_p.get_right() + RIGHT*0.5, target_q.get_left() - RIGHT*0.5)
        
        # 边框
        box_p = SurroundingRectangle(target_p, color=BLUE, buff=0.2)
        box_q = SurroundingRectangle(target_q, color=BLUE, buff=0.2)
        
        # 标注
        label_p = Text("前件命题", font=DEFAULT_FONT, font_size=24, color=GREY).next_to(box_p, UP)
        label_q = Text("后件命题", font=DEFAULT_FONT, font_size=24, color=GREY).next_to(box_q, UP)
        label_rel = Text("条件关系", font=DEFAULT_FONT, font_size=24, color=GOLD).next_to(arrow, UP)
        
        self.play(
            MoveToTarget(part_p),
            MoveToTarget(part_q),
            Create(arrow),
            run_time=2
        )
        
        self.play(
            Create(box_p),
            Create(box_q),
            Write(label_p),
            Write(label_q),
            Write(label_rel),
            run_time=2
        )
        
        self.wait(5)
