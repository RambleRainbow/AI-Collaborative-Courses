from manim import *
from src.utils import *

def action(scene, cast):
    val_atmos = cast["val_atmos"]
    val_surface = cast["val_surface"]
    val_soil = cast["val_soil"]
    val_rain = cast["val_rain"]
    val_store = cast["val_store"]
    val_evap = cast["val_evap"]
    time_label = cast["time_label"]
    
    scene.add(time_label)
    
    # Helper to create updated text object at same position
    def get_update(mob, new_val_str, color=None):
        if color is None:
            color = mob.get_color()
        return Text(str(new_val_str), font=DEFAULT_FONT, font_size=mob.font_size, color=color).move_to(mob)

    # Initial State (t=0): 1000 / 500 / 200
    
    # t=1: Constant flows (Evap 10, Store 5)
    t1_atmos = get_update(val_atmos, "1010")
    t1_surface = get_update(val_surface, "495")
    t1_soil = get_update(val_soil, "195")
    t1_label = Text("t = 1", font_size=40).to_corner(UL)
    
    scene.play(
        Transform(time_label, t1_label),
        Transform(val_atmos, t1_atmos),
        Transform(val_surface, t1_surface),
        Transform(val_soil, t1_soil),
        run_time=2
    )
    
    # t=2: Rain Starts! (Rain 50)
    t2_rain = get_update(val_rain, "50")
    t2_atmos = get_update(val_atmos, "970")   # 1010 - 50 + 10
    t2_surface = get_update(val_surface, "540") # 495 + 50 - 5
    t2_soil = get_update(val_soil, "190")      # 195 + 5 - 10
    t2_label = Text("t = 2 (下雨)", font_size=40, color=BLUE).to_corner(UL)
    
    scene.play(
        Transform(time_label, t2_label),
        Transform(val_rain, t2_rain),
        Transform(val_atmos, t2_atmos),
        Transform(val_surface, t2_surface),
        Transform(val_soil, t2_soil),
        
        # Visualize Arrow thickening
        cast["arrow_rain"].animate.set_stroke(width=8),
        run_time=2
    )
    
    # t=3: Rain Continues
    t3_atmos = get_update(val_atmos, "930")    # 970 - 50 + 10
    t3_surface = get_update(val_surface, "585")  # 540 + 50 - 5
    t3_soil = get_update(val_soil, "185")       # 190 + 5 - 10
    t3_label = Text("t = 3", font_size=40).to_corner(UL)
    
    scene.play(
        Transform(time_label, t3_label),
        Transform(val_atmos, t3_atmos),
        Transform(val_surface, t3_surface),
        Transform(val_soil, t3_soil),
        run_time=2
    )
    
    scene.wait(2)
