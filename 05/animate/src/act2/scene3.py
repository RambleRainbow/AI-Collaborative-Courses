from manim import FadeOut
from manim import *

def action(scene, cast):
    # Animate all three flows with moving dots from cast
    
    rain_dots = cast["rain_dots"]
    store_dots = cast["store_dots"]
    evap_dots = cast["evap_dots"]

    # Show dots and animate along markers
    scene.play(
        rain_dots[0].animate.set_fill(opacity=1),
        store_dots[0].animate.set_fill(opacity=1),
        evap_dots[0].animate.set_fill(opacity=1),
        run_time=0.1
    )
    
    scene.play(
        MoveAlongPath(rain_dots[0], cast["arrow_rain"]),
        MoveAlongPath(store_dots[0], cast["arrow_store"]),
        MoveAlongPath(evap_dots[0], cast["arrow_evap"]),
        run_time=1.8,
        rate_func=linear
    )

    scene.play(
        FadeOut(rain_dots[0]),
        FadeOut(store_dots[0]),
        FadeOut(evap_dots[0]),
        run_time=0.1
    )
    