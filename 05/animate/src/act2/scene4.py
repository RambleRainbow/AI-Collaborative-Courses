from manim import *
from src.utils import *

def action(scene, cast):
    val_atmos = cast["val_atmos"]
    val_surface = cast["val_surface"]
    val_rain = cast["val_rain"]
    val_evap = cast["val_evap"] # 10 const
    time_label = cast["time_label"]
    
    scene.add(time_label)
    
    # Helper to create updated text object at same position
    def get_update(mob, new_val_str, color=None):
        if color is None:
            color = mob.get_color()
        return Text(str(new_val_str), font=DEFAULT_FONT, font_size=mob.font_size, color=color).move_to(mob)

    # Initial State
    # Already set in cast (1000, 500, 0)
    
    # t=1
    # Evap happens: Surf -> Atmos
    t1_atmos = get_update(val_atmos, "1010")
    t1_surface = get_update(val_surface, "490")
    t1_label = Text("t = 1", font_size=40).move_to(time_label)
    
    scene.play(
        Transform(time_label, t1_label),
        Transform(val_surface, t1_surface),
        Transform(val_atmos, t1_atmos),
        run_time=2
    )
    
    # t=2: Rain Starts!
    t2_rain = get_update(val_rain, "50")
    t2_surface = get_update(val_surface, "530") # 490 + 40
    t2_atmos = get_update(val_atmos, "970") # 1010 - 40
    t2_label = Text("t = 2 (下雨)", font_size=40, color=BLUE).move_to(time_label)
    
    scene.play(
        Transform(time_label, t2_label),
        Transform(val_rain, t2_rain),
        Transform(val_surface, t2_surface),
        Transform(val_atmos, t2_atmos),
        
        # Visualize Arrow thickening
        cast["arrow_rain"].animate.set_stroke(width=8),
        run_time=2
    )
    
    # t=3: Rain Continues
    t3_surface = get_update(val_surface, "570") # 530 + 40
    t3_atmos = get_update(val_atmos, "930") # 970 - 40
    t3_label = Text("t = 3", font_size=40).move_to(time_label)
    
    scene.play(
        Transform(time_label, t3_label),
        Transform(val_surface, t3_surface),
        Transform(val_atmos, t3_atmos),
        run_time=2
    )
    
    scene.wait(2)
