from manim import *
import numpy as np

def action(scene, cast):
    # Focus is on system_group
    
    # Simple flow animation: dots moving down (Rain) and up (Evap)
    
    # Rain Drops
    start_rain = cast["arrow_rain"].get_start()
    end_rain = cast["arrow_rain"].get_end()
    
    rain_drops = VGroup(*[Dot(radius=0.08, color=BLUE) for _ in range(5)])
    
    # Evap Bubbles
    # Curved arrow path is harder to trace exactly without path object, 
    # but we can approximate or just move up on the right side
    evap_bubbles = VGroup(*[Circle(radius=0.08, color=BLUE_B, stroke_width=1) for _ in range(5)])
    
    # Helper to animate flow
    def update_rain(mob, alpha):
        # Linear interpolation
        mob.move_to(start_rain * (1-alpha) + end_rain * alpha)
        mob.set_opacity(1 - (alpha-0.8)*5 if alpha > 0.8 else 1) # Fade at end
        
    # Animate 
    scene.play(
        MoveAlongPath(rain_drops[0], Line(start_rain, end_rain)),
        rate_func=linear,
        run_time=2
    )
    
    # Loop visuals (symbolic)
    # Ideally we use value trackers next scene
    
    scene.wait(2)
