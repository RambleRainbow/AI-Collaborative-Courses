from manim import *
from src.utils import *
from src.act1.cast import *

class Act1Scene4(BaseScene):
    def construct(self):
        # 0. 初始化 Cast
        self.cast = get_act1_cast()
        
        # 1. 注册 Cast
        text_q = self.register_cast("text_q", self.cast["text_q"])
        # ... (register others if needed for state loading, though Scene 3 state has them)
        
        # 2. 加载状态 (Scene 3 结束时: P 已经拆解)
        self.load_state("act1_scene3")
        
        # 3. 场景逻辑: 此时 P 是拆解状态 (Sky/Rain concepts visible)
        # 我们要聚焦 Q ("地会湿")
        
        # 获取 Q 相关对象
        box_q = self.cast["box_q"]
        label_q = self.cast["label_q"]  # Scene 3 中它们 FadeOut 了吗？是的。
        arrow = self.cast["arrow"] # FadeOut
        label_rel = self.cast["label_rel"] # FadeOut
        
        # 获取 Concept Objects
        concept_ground = self.cast["concept_ground"]
        concept_wet = self.cast["concept_wet"]
        line = self.cast["line_right"]
        line_label = self.cast["line_label_right"]
        
        # 4. 恢复 Q 的显示 (以便进行拆解动画)
        # 同时淡出 P 的概念图 (Sky/Rain) 以转移焦点？
        # 脚本: "聚焦 地会湿"
        # 建议: 淡出左侧概念，淡入 Q，然后拆解 Q
        
        left_concepts = VGroup(
            self.cast["concept_sky"],
            self.cast["concept_rain"],
            self.cast["line_left"],
            self.cast["line_label_left"]
        )
        
        # 确保 Q 相关的对象在场景中 (Opacity 可能为 0)
        self.add(text_q, box_q, label_q)
        
        self.play(
            FadeOut(left_concepts),
            text_q.animate.set_opacity(1), # 恢复可见
            box_q.animate.set_opacity(1),
            label_q.animate.set_opacity(1),
            run_time=2
        )
        
        # 5. 拆解 Q
        # 这里的逻辑与 Scene 3 保持一致：
        # 文字保持原地 (stationary)
        # box 只是淡出
        # 概念图动态对齐到文字位置
        
        self.play(
            # text_q.animate.set_opacity(0.2).scale(0.5).to_edge(DOWN), # Scene 3 取消了移动
            FadeOut(text_q), # 模仿 Scene 3: 文字溶解
            FadeOut(box_q),
            FadeOut(label_q),
            run_time=2
        )
        
        # --- 动态对齐修正 ---
        concept_group = VGroup(concept_ground, concept_wet, line, line_label)
        target_x = text_q.get_center()[0]
        concept_group.set_x(target_x)
        
        self.play(
            FadeIn(concept_ground),
            FadeIn(concept_wet),
            Create(line),
            Write(line_label),
            run_time=2
        )
        
        self.wait(5)
        
        self.save_state("act1_scene4")
