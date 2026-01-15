from manim import FadeOut
from manim import *

def action(scene, cast):
    # Animate all three flows with moving dots from cast
    
    rain_dot = cast["rain_dot"]
    store_dot = cast["store_dot"]
    evap_dot = cast["evap_dot"]

    # Show dots and animate along markers
    scene.play(
        rain_dot.animate.set_fill(opacity=1),
        store_dot.animate.set_fill(opacity=1),
        evap_dot.animate.set_fill(opacity=1),
        run_time=0.1
    )
    
    scene.play(
        MoveAlongPath(rain_dot, cast["arrow_rain"]),
        MoveAlongPath(store_dot, cast["arrow_store"]),
        MoveAlongPath(evap_dot, cast["arrow_evap"]),
        run_time=1.8,
        rate_func=linear
    )

    scene.play(
        FadeOut(rain_dot),
        FadeOut(store_dot),
        FadeOut(evap_dot),
        run_time=0.1
    )