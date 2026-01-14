from manim import *
from src.utils import *

class Act4Notes(Scene):
    def construct(self):
        # TODO: 第四幕 - 逻辑推理的动态机制 (310-590秒)
        # 1. 场景1: 新知识呈现 - 肯定后件谬误 (P->Q, Q, So P? Wrong!)
        # 2. 场景2: 静态结构拆解 (Static P->Q graph)
        # 3. 场景3: 推理系统的本体结构 (Premise, Rule, Conclusion Network)
        # 4. 场景4: 假言三段论的动态运行 (Correct: P matches P -> Q out)
        # 5. 场景5: 错误推理 - 肯定后件 (Wrong: Q matches P? No!)
        # 6. 场景6: 为什么会犯谬误 (Comparison)
        # 7. 场景7: 知识应用 = 识别系统+匹配结构
        # 8. 场景8: 第四幕总结
        
        t = Text("第四幕：逻辑推理的动态机制\n(待实现)", font=DEFAULT_FONT)
        self.add(t)
