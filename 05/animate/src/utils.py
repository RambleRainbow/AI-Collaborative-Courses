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
    def __init__(self, size=2.0, sequence=[0, 1, 3, 2], labels=["A", "B", "C", "D"], show_labels=True, **kwargs):
        super().__init__(**kwargs)
        self.sqs = VGroup(*[Square(side_length=size/2.1).set_stroke(WHITE, width=2) for _ in range(4)])
        self.sqs.arrange_in_grid(2, 2, buff=0.05)
        self.add(self.sqs)
        
        self.lbls = None
        if show_labels and labels:
            self.lbls = VGroup(*[
                Text(l, font=DEFAULT_FONT, font_size=size*18).move_to(s.get_center()) 
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


