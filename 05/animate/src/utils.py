from manim import WHITE
from manim import Indicate
from manim import *
from src.state_manager import *

# --- 样式常量 ---

# ... (omitted)

# --- 模板类 ---

class BaseScene(Scene):
    """基础场景类，包含通用设置"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cast = {}

    def construct(self):
        # 可以在这里添加所有场景通用的初始化代码
        pass

    def register_cast(self, name, mobject):
        """
        Register a mobject as a named actor for state preservation.
        """
        self.cast[name] = mobject
        return mobject

    def load_state(self, source_scene_name):
        """
        Loads state from a previous scene and applies it to registered cast members.
        Must be called AFTER registering cast members.
        """
        state_data = load_scene_state(source_scene_name)
        if not state_data:
            print(f"Warning: No state found for {source_scene_name}")
            return

        for name, mobject in self.cast.items():
            if name in state_data:
                apply_state(mobject, state_data[name])
                
    def save_state(self, current_scene_name):
        """
        Saves current state of all registered cast members.
        """
        save_scene_state(current_scene_name, self.cast)

# 字体配置 (请确保系统安装了支持中文的字体，如黑体、思源黑体等)
# 如果渲染时中文显示为方框，请修改这里的字体名称
DEFAULT_FONT = "PingFang SC"  # 或 "Source Han Sans SC", "PingFang SC"

# 颜色主题
COLOR_STATIC = GREY_B      # 静态知识/冻结状态
COLOR_DYNAMIC = BLUE       # 动态系统/活跃状态
COLOR_HIGHLIGHT = GOLD     # 高亮/强调
COLOR_ERROR = RED_C        # 错误/谬误
COLOR_CORRECT = GREEN      # 正确/通过

# --- 通用工具函数 ---

def create_text(text_content, font_size=48, color=WHITE):
    """创建居中的中文文本对象"""
    t = Text(text_content, font=DEFAULT_FONT, font_size=font_size)
    t.set_color(color)
    return t

def create_title(text_content):
    """创建标题文本"""
    return create_text(text_content, font_size=60).to_edge(UP)

def create_concept_node(label, position=ORIGIN, color=BLUE, radius=0.6):
    """创建概念节点 (圆圈+文字)"""
    circle = Circle(radius=radius, color=color).move_to(position)
    text = Text(label, font=DEFAULT_FONT, font_size=24).move_to(position)
    text.set_color(WHITE)
    return VGroup(circle, text)

class LightingUnit(VGroup):
    """
    A persistent object representing a 2x2 grid of lights (squares).
    Supports a custom lighting sequence and state-based animation.
    """
    def __init__(self, size=2.0, sequence=[0, 1, 3, 2], labels=["A", "B", "C", "D"], show_labels=True, buff=0.1, **kwargs):
        super().__init__(**kwargs)
        # Calculate square side length so that 2*sq_side + buff = size
        sq_side = (size - buff) / 2
        self.sqs = VGroup(*[Square(side_length=sq_side).set_stroke(WHITE, width=2) for _ in range(4)])
        self.sqs.arrange_in_grid(2, 2, buff=buff)
        self.add(self.sqs)
        
        self.lbls = None
        if show_labels and labels:
            self.lbls = VGroup(*[
                Text(l, font=DEFAULT_FONT, font_size=sq_side * 0.8 * 36).move_to(s.get_center()) 
                for l, s in zip(labels, self.sqs)
            ])
            self.add(self.lbls)
            
        self.sequence = sequence  # e.g., [0, 1, 3, 2] for A->B->D->C
        self.current_step = -1    # -1 means all lights off
        
    def to_next_state(self, color=BLUE, opacity=1.0):
        """
        Advances the sequence and returns a list of animations.
        """
        self.current_step = (self.current_step + 1) % len(self.sequence)
        active_idx = self.sequence[self.current_step]
        
        animations = []
        for i, sq in enumerate(self.sqs):
            if i == active_idx:
                animations.append(sq.animate.set_fill(color, opacity=opacity).set_stroke(WHITE, opacity=1))
            else:
                animations.append(sq.animate.set_fill(opacity=0).set_stroke(GREY, opacity=0.3))
        return animations

    def get_frozen_state_anims(self):
        """Returns animations to set the unit to a frozen (grey/dimmed) state."""
        self.current_step = -1
        return [
            self.sqs.animate.set_fill(GREY, opacity=0.1).set_stroke(GREY, opacity=0.3)
        ]

class ReasoningMachine(VGroup):
    """
    A logical inference machine object.
    Layout (top to bottom): Major Premise (Box), Minor Premise (Small Box), Gear, Conclusion (Small Box).
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # 1. Boxes
        self.box_major = RoundedRectangle(width=5, height=1.5, corner_radius=0.1, color=WHITE)
        self.box_minor = RoundedRectangle(width=3, height=1.0, corner_radius=0.1, color=WHITE)
        self.box_conclusion = RoundedRectangle(width=3, height=1.0, corner_radius=0.1, color=WHITE)
        
        # 2. Gear Construction
        radius = 0.5
        teeth_num = 8
        gear_body = Circle(radius=radius, color=WHITE, fill_opacity=0.1)
        teeth = VGroup(*[
            Rectangle(width=radius/2, height=radius/4, color=WHITE, fill_opacity=1)
            .shift(UP * radius)
            .rotate(i * 2 * PI / teeth_num, about_point=ORIGIN)
            for i in range(teeth_num)
        ])
        self.gear = VGroup(gear_body, teeth)
        
        # 3. Layout Arrangement
        self.box_major.move_to(UP * 2.5)
        self.box_minor.next_to(self.box_major, DOWN, buff=0.4)
        self.gear.next_to(self.box_minor, DOWN, buff=0.4)
        self.box_conclusion.next_to(self.gear, DOWN, buff=0.4)
        
        self.add(self.box_major, self.box_minor, self.gear, self.box_conclusion)
        
        # Track slot content
        self.slots = {"major": None, "minor": None, "conclusion": None}
        self.content = VGroup() # For easy global FadeOut in clean()
        self.add(self.content)

    def get_reasoning_steps(self, major_obj, minor_obj, conclusion_obj, is_correct=True):
        """
        Calculates and returns a list of animation 'steps'.
        Handles FadeOut/FadeIn transitions only for changed content.
        """
        steps = []
        fade_outs = []
        fade_ins = []
        
        new_items = {"major": major_obj, "minor": minor_obj, "conclusion": conclusion_obj}
        
        for key in ["major", "minor", "conclusion"]:
            old = self.slots[key]
            new = new_items[key]
            
            if old is not None and old is not new:
                # Content changed, need to replace
                fade_outs.append(FadeOut(old))
                self.content.remove(old)
                
            if new is not None:
                box = getattr(self, f"box_{key}")
                new.move_to(box.get_center())
                if new is not old:
                    # New content or changed content
                    fade_ins.append(FadeIn(new, shift=DOWN*0.2 if key != "conclusion" else DOWN*0.3))
                    if new not in self.content:
                        self.content.add(new)
                self.slots[key] = new

        if fade_outs:
            steps.append(fade_outs)
        
        if fade_ins:
            steps.append(fade_ins)
        self.box_conclusion.set_stroke(WHITE, opacity=1)
        
        # Step 2: Gear Rotates
        steps.append([
            Rotate(self.gear, angle=-2*PI, run_time=1.5, rate_func=linear),
            Indicate(self.box_conclusion, color=WHITE)
        ])
        
        # Step 3: Feedback
        if is_correct:
            # fb = Text("正确️", color=GREEN).scale(1.5).move_to(self.box_conclusion.get_center())
            # steps.append([FadeIn(fb, scale=1.5, run_time=0.3)])
            steps.append([self.box_conclusion.animate.set_stroke(GREEN, opacity=1)])
            # steps.append([FadeOut(fb, run_time=0.3)])
        else:
            # fb = Text("错误", color=RED).scale(1.5).move_to(self.box_conclusion.get_center())
            # steps.append([FadeIn(fb, scale=1.5, run_time=0.3)])
            steps.append([self.box_conclusion.animate.set_stroke(RED, opacity=1)])
            # steps.append([FadeOut(fb, run_time=0.3)])
            
        return steps

    def get_clean_anim(self):
        """
        Returns the animation to clean the machine's contents and resets slot tracking.
        """
        anim = FadeOut(self.content)
        self.slots = {"major": None, "minor": None, "conclusion": None}
        self.content.remove(*self.content)
        return anim
