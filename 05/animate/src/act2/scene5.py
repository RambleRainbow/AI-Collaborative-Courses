from manim import *

def action(scene, cast):
    # Freezes at t=2 state basically
    
    highlight_box = cast["highlight_box"] # Surrounds Rain flow structure
    static_group = cast["static_group"] # The Act 1 map
    
    # Dim everything else?
    # Create a full screen dark rect excluding the highlight region is hard.
    # Instead, simple Highlight rect creation
    
    scene.play(Create(highlight_box))
    
    # Bring static knowledge back to prominent position (if it was hidden/small)
    # Move System slightly left, Static slightly right?
    
    # For now, just show connection
    # Static group is currently in UL corner scale 0.4 (from Scene 2)
    
    scene.play(
        static_group.animate.scale(2.5).move_to(RIGHT*3), # restore size
        run_time=2
    )
    
    # Connection text
    conn = DoubleArrow(highlight_box.get_right(), static_group.get_left(), color=GOLD)
    txt = Text("等价", color=GOLD).next_to(conn, UP)
    
    scene.play(GrowArrow(conn), Write(txt))
    scene.wait(3)
