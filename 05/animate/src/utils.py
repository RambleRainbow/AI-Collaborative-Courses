from manim import *

# --- 样式常量 ---

# 字体配置 (请确保系统安装了支持中文的字体，如黑体、思源黑体等)
# 如果渲染时中文显示为方框，请修改这里的字体名称
DEFAULT_FONT = "SimHei"  # 或 "Source Han Sans SC", "PingFang SC"

# 颜色主题
COLOR_STATIC = GREY_B      # 静态知识/冻结状态
COLOR_DYNAMIC = BLUE       # 动态系统/活跃状态
COLOR_HIGHLIGHT = GOLD     # 高亮/强调
COLOR_ERROR = RED_C        # 错误/谬误
COLOR_CORRECT = GREEN      # 正确/通过

# --- 通用工具函数 ---

def create_text(text_content, font_size=48, color=WHITE):
    """创建居中的中文文本对象"""
    return Text(text_content, font=DEFAULT_FONT, font_size=font_size, color=color)

def create_title(text_content):
    """创建标题文本"""
    return create_text(text_content, font_size=60).to_edge(UP)

def create_concept_node(label, position=ORIGIN, color=BLUE_E, radius=0.6):
    """创建概念节点 (圆圈+文字)"""
    circle = Circle(radius=radius, color=color).move_to(position)
    text = Text(label, font=DEFAULT_FONT, font_size=24).move_to(position)
    return VGroup(circle, text)

# --- 模板类 ---

class BaseScene(Scene):
    """基础场景类，包含通用设置"""
    def construct(self):
        # 可以在这里添加所有场景通用的初始化代码
        pass
