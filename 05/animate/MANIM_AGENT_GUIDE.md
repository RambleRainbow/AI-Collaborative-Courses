# Manim 动画项目智能体开发手册 (Gemini Agent Guide)

这份手册旨在指导智能体（如 Gemini）和用户快速启动并高效协作进行 Manim 动画项目开发。它沉淀了我们从“试错”到“最佳实践”的核心经验。

---

## 1. 核心架构模式 (Architecture Patterns)

### ❌ 避免做法
*   **不要尝试自动状态持久化**：不要试图编写通用的 `StateManager` 来自动保存/恢复 Mobject 的所有属性。Manim 的底层状态（VMobject, Updater, Animation）过于复杂，自动序列化极不稳定。
*   **不要过度拆分文件**：不要为每个小场景创建独立的类（`class Scene1(Scene)`），导致上下文割裂且难以连续播放。

### ✅ 推荐做法：Stateful Pipeline (有状态流水线)
采用 **"One Render, Multiple Scripts"** 模式。

1.  **统一渲染入口 (`render.py`)**：
    每个 Act 只有一个 `ActX(Scene)` 类。它负责初始化 Cast，并按顺序调用各个 Scene 脚本。
    ```python
    class Act1(BaseScene):
        def construct(self):
            super().construct()
            self.cast = get_act1_cast() # 初始化演员
            
            s1.action(self, self.cast) # 场景 1
            self.next_section()
            s2.action(self, self.cast) # 场景 2
            # ...
    ```

2.  **Cast 系统 (`cast.py`)**：
    **显式**地预定义核心对象。Scene 之间通过传递 `cast` 字典来共享对象引用。
    ```python
    def get_act1_cast():
        return {
            "main_circle": Circle(color=RED),
            "title": Text("Title"),
            # ...
        }
    ```

3.  **函数式场景 (`sceneX.py`)**：
    场景脚本只包含**动作 (Action)**，不包含对象定义。
    ```python
    def action(scene, cast):
        circle = cast["main_circle"]
        scene.play(circle.animate.shift(RIGHT)) # 只负责动
    ```

---

## 2. 调试与反馈机制 (Debugging & Feedback)

### ✅ A::S::P 调试水印 (HUD)
这是最高效的沟通工具。智能体应优先为 `BaseScene` 实现此功能。

*   **实现**：
    *   在 `BaseScene.play()` 中自动增加计数器。
    *   在屏幕右上角显示 `Act::Scene::PlayCount` (例如 `A1::S2::P5`)。
    *   支持通过环境变量 (`ANIMATE_DEBUG=0`) 关闭，方便最终渲染。
*   **用法**：
    *   用户只需截图或告知坐标：“**A4::S3::P8** 文字重叠”。
    *   智能体可直接定位到 `scene3.py` 的第 8 个 `play` 调用附近。

### ✅ 截图驱动迭代
*   **用户**：截图并圈出问题。
*   **智能体**：根据视觉反馈微调坐标 (`.shift()`, `.next_to()`)，而不是盲目猜测布局。

---

## 3. 组件封装策略 (Component Design)

### ✅ 行为封装 (Behavior Encapsulation)
对于复杂的复用对象（如“推理机”、“流程图”），不要只封装**外观**，要封装**动作**。

*   **推荐接口**：
    ```python
    class ReasoningMachine(VGroup):
        def __init__(self):
            # ... 定义外观 ...

        def get_reasoning_steps(self, input, output):
            # ... 返回一串动画对象 (AnimationGroup) ...
            return [FadeIn(input), Rotate(self.gear), FadeIn(output)]
            
        def get_clean_anim(self):
            # ... 返回清理自身的动画 ...
            return FadeOut(self.content)
    ```
*   **优势**：Scene 脚本只需调用 `machine.get_reasoning_steps()`，无需关心内部复杂的动画时序。

---

## 4. 坐标与布局 (Layout Strategy)

### ✅ 显式坐标系
*   **核心组件**：在组件内部建立稳定的相对坐标系（例如 `self.box` 在 `ORIGIN`，`self.label` 在 `UP*2`）。
*   **场景布局**：
    *   避免过度依赖 `.next_to()` 链（容易积累误差）。
    *   对于关键帧，使用明确的 `.move_to()` 或 `.shift()` 进行绝对定位修正。
    *   例如：`machine.shift(UP * 0.5)` 比 `machine.next_to(text, UP)` 更不容易受文本长度变化影响。

---

## 5. 智能体提示词 (Agent System Prompt)

在配置 AI 辅助 Manim 开发时，建议包含以下规则：

> **Role**: Manim Animation Specialist
>
> **Constraint Checklist & Confidence Score**:
> 1. Use the **Stateful Pipeline** pattern (One render class per Act, functional scenes).
> 2. Implement **HUD Debug Overlay** (A::S::P) immediately.
> 3. Use **Cast System** for object sharing; do NOT use global state managers.
> 4. Encapsulate complex animations in Component methods (`get_anim_steps`).
> 5. When user reports a visual bug (e.g., "A3::S2::P4 overlap"), find the corresponding `play()` call and adjust coordinates.
> 6. Always include a clean-up step (`FadeOut`) at the end of a scene function unless the object persists intentionally.
>
> **Workflow**:
> 1. Define `cast.py` -> 2. Implement `render.py` -> 3. Implement `sceneX.py` sequentially.

---

遵循此手册，您可以跳过“状态丢失”、“调试困难”和“代码臃肿”的坑，直接进入高效的动画生产流程。
