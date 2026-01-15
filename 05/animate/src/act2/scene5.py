from manim import *

def action(scene, cast):
    # Freezes at t=2 state basically
    
    highlight_box = cast["highlight_box"] # Surrounds Rain flow structure
    static_group = cast["static_group"] # The Act 1 map
    group_system = cast["system_group"] # The System Dynamics model
    
    # Dim everything else?
    # Create a full screen dark rect excluding the highlight region is hard.
    # Instead, simple Highlight rect creation
    
    # scene.play(Create(highlight_box))
    
    # Bring static knowledge back to prominent position (if it was hidden/small)
    # Move System slightly left, Static slightly right?
    
    # For now, just show connection
    # Static group is currently in UL corner scale 0.4 (from Scene 2)
    
    scene.play(
        static_group.animate.move_to(LEFT*4), # restore size
        group_system.animate.scale(0.4).move_to(RIGHT*4), # shrink system
        run_time=2
    )
    
    # Connection text
    conn = DoubleArrow(group_system.get_left(), static_group.get_right(), color=GOLD)
    txt = Text("等价", color=GOLD, font_size=32).next_to(conn, UP)
    
    scene.play(GrowArrow(conn), Write(txt))
    scene.wait(3)
