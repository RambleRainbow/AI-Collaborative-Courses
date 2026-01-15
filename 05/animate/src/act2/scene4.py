from manim import *
from src.utils import *

def action(scene, cast):
    # 获取锚点（这些矩形框在场景中是持久的，位置不会变）
    rect_atmos = cast["stock_atmos_rect"]
    rect_surface = cast["stock_surface_rect"]
    rect_soil = cast["stock_soil_rect"]
    
    # 获取需要持续更新的对象
    val_atmos = cast["val_atmos"]
    val_surface = cast["val_surface"]
    val_soil = cast["val_soil"]
    val_rain = cast["val_rain"]
    time_label = cast["time_label"]
    
    if time_label not in scene.mobjects:
        scene.add(time_label)

    # 助手函数：创建目标 Text 对象用于 Transform
    def get_target(val_str, anchor, color=WHITE, font_size=32):
        return create_text(str(val_str), font_size=font_size, color=color).move_to(anchor.get_center())

    # --- t=1: 常规流动 ---
    scene.play(
        Transform(time_label, create_text("t = 1", font_size=40).to_corner(UL)),
        Transform(val_atmos, get_target("1010", rect_atmos)),
        Transform(val_surface, get_target("495", rect_surface)),
        Transform(val_soil, get_target("195", rect_soil)),
        MoveAlongPath(cast["rain_dots"][0], cast["arrow_rain"]),
        MoveAlongPath(cast["store_dots"][0], cast["arrow_store"]),
        MoveAlongPath(cast["evap_dots"][0], cast["arrow_evap"]),
        run_time=2
    )
    
    # --- t=2: 开始降雨 ---
    scene.play(
        Transform(time_label, create_text("t = 2 (下雨)", font_size=40, color=BLUE).to_corner(UL)),
        Transform(val_rain, get_target("50", cast["arrow_rain"], color=BLUE, font_size=18).next_to(cast["label_rain"], UP, buff=0.05)),
        Transform(val_atmos, get_target("970", rect_atmos)),
        Transform(val_surface, get_target("540", rect_surface)),
        Transform(val_soil, get_target("190", rect_soil)),
        MoveAlongPath(cast["rain_dots"][0], cast["arrow_rain"]),
        MoveAlongPath(cast["store_dots"][0], cast["arrow_store"]),
        MoveAlongPath(cast["evap_dots"][0], cast["arrow_evap"]),
        cast["arrow_rain"].animate.set_stroke(width=10),
        run_time=2
    )
    
    # --- t=3: 降雨持续 ---
    scene.play(
        Transform(time_label, create_text("t = 3", font_size=40).to_corner(UL)),
        Transform(val_atmos, get_target("930", rect_atmos)),
        Transform(val_surface, get_target("585", rect_surface)),
        Transform(val_soil, get_target("185", rect_soil)),
        MoveAlongPath(cast["rain_dots"][0], cast["arrow_rain"]),
        MoveAlongPath(cast["store_dots"][0], cast["arrow_store"]),
        MoveAlongPath(cast["evap_dots"][0], cast["arrow_evap"]),
        run_time=2
    )
