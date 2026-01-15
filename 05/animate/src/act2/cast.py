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
    # Layout: Central, larger than static map initially (or static map zooms out)
    # Stock 1 (Atmosphere) - Up
    # Stock 2 (Surface) - Down
    
    stock_atmos_rect = Rectangle(width=4, height=2, color=BLUE_A).to_edge(UP, buff=1)
    stock_atmos_label = Text("大气水量", font=DEFAULT_FONT, font_size=32).next_to(stock_atmos_rect, UP, buff=0.2)
    val_atmos = Text("1000", font=DEFAULT_FONT, font_size=36, color=WHITE).move_to(stock_atmos_rect)
    
    stock_surface_rect = Rectangle(width=4, height=2, color=ORANGE).to_edge(DOWN, buff=1)
    stock_surface_label = Text("地表水量", font=DEFAULT_FONT, font_size=32).next_to(stock_surface_rect, DOWN, buff=0.2)
    val_surface = Text("500", font=DEFAULT_FONT, font_size=36, color=WHITE).move_to(stock_surface_rect)
    
    # Flows
    # Rain: Atmos -> Surface
    flow_rain_arrow = Arrow(stock_atmos_rect.get_bottom(), stock_surface_rect.get_top(), color=BLUE, buff=0.1, max_stroke_width_to_length_ratio=5)
    flow_rain_label = Text("降雨流", font=DEFAULT_FONT, font_size=24, color=BLUE).next_to(flow_rain_arrow, LEFT)
    val_rain_flow = Text("0", font=DEFAULT_FONT, font_size=24, color=BLUE).next_to(flow_rain_label, DOWN)
    
    # Evap: Surface -> Atmos (Curved or side)
    # Let's make it a curved arrow on the right
    flow_evap_arrow = CurvedArrow(stock_surface_rect.get_right(), stock_atmos_rect.get_right(), angle=PI/2, color=BLUE_B)
    flow_evap_label = Text("蒸发流", font=DEFAULT_FONT, font_size=24, color=BLUE_B).next_to(flow_evap_arrow, RIGHT)
    val_evap_flow = Text("10", font=DEFAULT_FONT, font_size=24, color=BLUE_B).next_to(flow_evap_label, DOWN)
    
    group_system = VGroup(
        stock_atmos_rect, stock_atmos_label, val_atmos,
        stock_surface_rect, stock_surface_label, val_surface,
        flow_rain_arrow, flow_rain_label, val_rain_flow,
        flow_evap_arrow, flow_evap_label, val_evap_flow
    )
    
    cast["system_group"] = group_system
    # Expose trackers/values for animation
    cast["val_atmos"] = val_atmos
    cast["val_surface"] = val_surface
    cast["val_rain"] = val_rain_flow
    cast["val_evap"] = val_evap_flow
    cast["arrow_rain"] = flow_rain_arrow
    
    # Time Axis / Timer
    time_label = Text("t = 0", font_size=40).to_corner(UL)
    cast["time_label"] = time_label
    
    # --- 3. Comparison Elements (Scene 5/6) ---
    # Highlight box for system fragment
    highlight_box = SurroundingRectangle(VGroup(stock_atmos_rect, flow_rain_arrow, stock_surface_rect), color=GOLD, buff=0.2)
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
