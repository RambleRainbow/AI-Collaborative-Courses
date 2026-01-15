from manim import *
from src.utils import *

def get_act2_cast():
    cast = {}
    
    # --- 1. Act 1 Concept Map (The "Static Knowledge") ---
    # Layout matching the reference image:
    #      天空 (UL)                    地面 (UR)
    #       |                            |
    #     (发生)                      (具有状态)
    #       |           蕴含             |
    #      下雨 (DL) ─────────→        湿 (DR)
    
    # Constants for layout - wider spacing
    LEFT_POS = LEFT * 3.5
    RIGHT_POS = RIGHT * 3.5
    UP_OFFSET = UP * 1.8
    DOWN_OFFSET = DOWN * 1.8
    
    # Sky/Rain Group (Left Side)
    c_sky = create_concept_node("天空", LEFT_POS + UP_OFFSET, color=BLUE)
    c_rain = create_concept_node("下雨", LEFT_POS + DOWN_OFFSET, color=BLUE)
    l_left = DashedLine(c_sky.get_bottom(), c_rain.get_top(), color=BLUE_A)
    txt_left = Text("(发生)", font=DEFAULT_FONT, font_size=20, color=WHITE).next_to(l_left, RIGHT, buff=0.15)
    
    # Ground/Wet Group (Right Side)
    c_ground = create_concept_node("地面", RIGHT_POS + UP_OFFSET, color=BLUE)
    c_wet = create_concept_node("湿", RIGHT_POS + DOWN_OFFSET, color=BLUE)
    l_right = DashedLine(c_ground.get_bottom(), c_wet.get_top(), color=BLUE_A)
    txt_right = Text("(具有状态)", font=DEFAULT_FONT, font_size=20, color=WHITE).next_to(l_right, LEFT, buff=0.15)
    
    # Implication Arrow: middle position (from txt_left right to txt_right left)
    arrow_cause = Arrow(txt_left.get_right(), txt_right.get_left(), color=GOLD, buff=0.15)
    txt_cause = Text("蕴含", font=DEFAULT_FONT, font_size=28, color=GOLD).next_to(arrow_cause, UP, buff=0.1)
    
    # Group them (static map = Act 1 final state for Act 2)
    group_static_core = VGroup(c_sky, c_rain, l_left, txt_left, c_ground, c_wet, l_right, txt_right)
    group_static = VGroup(group_static_core, arrow_cause, txt_cause)
    
    cast["static_group"] = group_static
    cast["static_core"] = group_static_core  # Without arrow, for transition
    cast["c_sky"] = c_sky
    cast["c_rain"] = c_rain
    cast["c_ground"] = c_ground
    cast["c_wet"] = c_wet
    cast["arrow_cause"] = arrow_cause
    cast["txt_cause"] = txt_cause
    
    # Question Mark for Scene 1
    q_mark = Text("?", font_size=96, color=RED).next_to(group_static, UP)
    cast["q_mark"] = q_mark
    
    
    # --- 2. System Dynamics Model (The "Dynamic Truth") ---
    # Horizontal Cycle Layout:
    # [Atmos] --Rain--> [Surface] --Store--> [Soil]
    #   ^                                     |
    #   └──────────────Evap───────────────────┘

    STOCK_WIDTH = 3.2
    STOCK_HEIGHT = 1.8
    STOCK_Y = 0

    # Stock 1: 大气水量 (Atmosphere) - LEFT
    stock_atmos_rect = Rectangle(width=STOCK_WIDTH, height=STOCK_HEIGHT, color=BLUE_A).shift(LEFT * 4.5 + UP * STOCK_Y)
    stock_atmos_label = Text("大气水量", font=DEFAULT_FONT, font_size=28).next_to(stock_atmos_rect, UP, buff=0.2)
    val_atmos = Text("1000", font=DEFAULT_FONT, font_size=32, color=WHITE).move_to(stock_atmos_rect)
    
    # Stock 2: 地表水量 (Surface) - CENTER
    stock_surface_rect = Rectangle(width=STOCK_WIDTH, height=STOCK_HEIGHT, color=ORANGE).shift(UP * STOCK_Y)
    stock_surface_label = Text("地表水量", font=DEFAULT_FONT, font_size=28).next_to(stock_surface_rect, UP, buff=0.2)
    val_surface = Text("500", font=DEFAULT_FONT, font_size=32, color=WHITE).move_to(stock_surface_rect)

    # Stock 3: 地下水量 (Soil) - RIGHT
    stock_soil_rect = Rectangle(width=STOCK_WIDTH, height=STOCK_HEIGHT, color=GREY_B).shift(RIGHT * 4.5 + UP * STOCK_Y)
    stock_soil_label = Text("地下水量", font=DEFAULT_FONT, font_size=28).next_to(stock_soil_rect, UP, buff=0.2)
    val_soil = Text("200", font=DEFAULT_FONT, font_size=32, color=WHITE).move_to(stock_soil_rect)

    # Flows (Arrows + Labels + Values)
    # Flow 1: 降雨 (Rain): Atmos -> Surface
    arrow_rain = Arrow(stock_atmos_rect.get_right(), stock_surface_rect.get_left(), color=BLUE, buff=0.1)
    label_rain = Text("降雨流", font=DEFAULT_FONT, font_size=20, color=BLUE).next_to(arrow_rain, UP, buff=0.1)
    val_rain = Text("0", font=DEFAULT_FONT, font_size=18, color=BLUE).next_to(label_rain, UP, buff=0.05)
    rain_dots = VGroup(*[Dot(radius=0.08, color=BLUE, fill_opacity=0) for _ in range(3)])

    # Flow 2: 储存 (Store): Surface -> Soil
    arrow_store = Arrow(stock_surface_rect.get_right(), stock_soil_rect.get_left(), color=GREEN_B, buff=0.1)
    label_store = Text("储存流", font=DEFAULT_FONT, font_size=20, color=GREEN_B).next_to(arrow_store, UP, buff=0.1)
    val_store = Text("5", font=DEFAULT_FONT, font_size=18, color=GREEN_B).next_to(label_store, UP, buff=0.05)
    store_dots = VGroup(*[Dot(radius=0.08, color=GREEN_B, fill_opacity=0) for _ in range(3)])

    # Flow 3: 蒸发 (Evap): Soil -> Atmos (Concave downward arc)
    arrow_evap = CurvedArrow(stock_soil_rect.get_bottom(), stock_atmos_rect.get_bottom(), angle=-PI/2, color=BLUE_B)
    label_evap = Text("蒸发流", font=DEFAULT_FONT, font_size=20, color=BLUE_B).next_to(arrow_evap, DOWN, buff=0.1)
    val_evap = Text("10", font=DEFAULT_FONT, font_size=18, color=BLUE_B).next_to(label_evap, DOWN, buff=0.05)
    evap_dots = VGroup(*[Dot(radius=0.08, color=BLUE_B, fill_opacity=0) for _ in range(3)])

    group_system = VGroup(
        stock_atmos_rect, stock_atmos_label, val_atmos,
        stock_surface_rect, stock_surface_label, val_surface,
        stock_soil_rect, stock_soil_label, val_soil,
        arrow_rain, label_rain, val_rain, rain_dots,
        arrow_store, label_store, val_store, store_dots,
        arrow_evap, label_evap, val_evap, evap_dots
    )
    
    cast["system_group"] = group_system
    # Expose trackers/values/rects for animation
    cast["stock_atmos_rect"] = stock_atmos_rect
    cast["stock_surface_rect"] = stock_surface_rect
    cast["stock_soil_rect"] = stock_soil_rect
    cast["val_atmos"] = val_atmos
    cast["val_surface"] = val_surface
    cast["val_soil"] = val_soil
    cast["val_rain"] = val_rain
    cast["val_store"] = val_store
    cast["val_evap"] = val_evap
    cast["arrow_rain"] = arrow_rain
    cast["arrow_store"] = arrow_store
    cast["arrow_evap"] = arrow_evap
    cast["rain_dots"] = rain_dots
    cast["store_dots"] = store_dots
    cast["evap_dots"] = evap_dots
    cast["label_rain"] = label_rain
    cast["label_store"] = label_store
    cast["label_evap"] = label_evap
    
    # Time Axis / Timer
    time_label = Text("t = 0", font_size=40).to_corner(UL)
    cast["time_label"] = time_label
    
    # --- 3. Comparison Elements (Scene 5/6) ---
    # Highlight box for system fragment
    highlight_box = SurroundingRectangle(VGroup(stock_atmos_rect, arrow_rain, stock_surface_rect, stock_soil_rect), color=GOLD, buff=0.2)
    cast["highlight_box"] = highlight_box
    
    # Split Screen Line
    split_line = Line(UP*4, DOWN*4)
    cast["split_line"] = split_line
    
    # Labels for Split Screen
    label_static_view = Text("静态知识 (快照)", font=DEFAULT_FONT, color=GREY).to_edge(UP).shift(LEFT*3.5)
    label_dynamic_view = Text("系统动力 (电影)", font=DEFAULT_FONT, color=BLUE).to_edge(UP).shift(RIGHT*3.5)
    cast["label_static"] = label_static_view
    cast["label_dynamic"] = label_dynamic_view
    
    return cast

