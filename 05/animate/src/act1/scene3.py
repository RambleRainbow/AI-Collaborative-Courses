from manim import FadeOut
from manim import *
from src.utils import *
from src.act1.cast import *

class Act1Scene3(BaseScene):
    def construct(self):
        # 1. 加载并恢复状态
        self.cast = get_act1_cast()
        self.load_state("act1_scene2")
        
        # 2. 场景初始化
        # 添加 Scene 2 遗留的可见元素
        self.add(
            self.cast["text_p"],
            self.cast["text_q"],
            self.cast["arrow"],
            self.cast["box_p"],
            self.cast["box_q"],
            self.cast["label_p"],
            self.cast["label_q"],
            self.cast["label_rel"]
        )
        self.wait(1)

        # 3. 动画: 聚焦左侧
        # 引用便捷变量
        text_p = self.cast["text_p"]
        box_p = self.cast["box_p"]
        label_p = self.cast["label_p"]
        
        # 4. 引入概念图 (已在 Cast 中定义)
        concept_sky = self.cast["concept_sky"]
        concept_rain = self.cast["concept_rain"]
        line = self.cast["line_left"]
        line_label = self.cast["line_label_left"]
        
        # --- 动态对齐修正 (Dynamic Alignment) ---
        # 确保概念图组在水平方向上与 text_p 完全对齐 (Center Align X)
        # text_p 此时保持在原地 (Scene 3逻辑)
        concept_group = VGroup(concept_sky, concept_rain, line, line_label)
        target_x = text_p.get_center()[0]
        concept_group.set_x(target_x)
        
        # 确保标签为白色 (Defensive programming)
        line_label.set_color(WHITE)
        
        # 5. 文字溶解，概念浮现
        self.play(
            FadeOut(text_p),
            FadeOut(box_p),
            FadeOut(label_p),
            run_time=2
        )
        
        self.play(
            FadeIn(concept_sky),
            FadeIn(concept_rain),
            Create(line),
            Write(line_label),
            run_time=2
        )
        
        self.wait(5)
        
        self.save_state("act1_scene3")
