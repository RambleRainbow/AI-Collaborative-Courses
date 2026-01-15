from manim import *

def action(scene, cast):
    static_group = cast["static_group"]
    system_group = cast["system_group"]
    
    # 1. Transform / Zoom Out
    # Static group shrinks and moves to sidebar or just fades out to reveal bigger truth
    # Script says: "Lens zooms out... static map is small part"
    
    # Let's keep static group small in corner
    scene.play(
        static_group.animate.scale(0.4).to_corner(UL).set_opacity(0.5),
        run_time=2
    )
    
    # 2. Show System
    # System group is defined in cast with fixed positions (Up/Down)
    scene.play(FadeIn(system_group), run_time=2)
