from manim import *

def action(scene, cast):
    # Split screen setup
    
    line = cast["split_line"]
    l_static = cast["label_static"]
    l_dynamic = cast["label_dynamic"]
    
    # Organize layout
    # Left: Static Group (Static Knowledge)
    # Right: System Group (Dynamic Truth)
    
    static_group = cast["static_group"]
    system_group = cast["system_group"]
    
    scene.play(
        Create(line),
        Write(l_static),
        Write(l_dynamic),
        
        static_group.animate.move_to(LEFT * 4),
        system_group.animate.move_to(RIGHT * 4),
        
        # Cleanup previous annotations
        FadeOut(cast["time_label"]),
        
        run_time=2
    )
    
    # Final caption
    caption = Text("知识只是系统的快照", color=YELLOW, font_size=40).to_edge(DOWN)
    scene.play(Write(caption))
    
    scene.wait(3)
