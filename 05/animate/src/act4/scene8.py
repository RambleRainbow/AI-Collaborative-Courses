from manim import *
from src.utils import *

def action(scene, cast):
    # 1. Get Machines and Labels
    m_cat = cast["machine_cat"]
    m_dis = cast["machine_dis"]
    m_hyp = cast["machine_hyp"]
    labels = cast["syl_labels"]
    
    title = Text("三大推理形式 (多种有效模式)", font=DEFAULT_FONT, font_size=32).to_edge(UP)
    scene.play(Write(title))
    
    # 2. Create all three machines at once
    scene.play(
        Create(m_cat), Create(m_dis), Create(m_hyp),
        *[Write(lbl) for lbl in labels]
    )
    scene.wait(1)
    
    # 3. Define inference rounds - each machine runs 2 forms
    rounds = [
        ("cat1", "dis1", "hyp1"),  # Round 1: Barbara, ¬P⊢Q, MP
        ("cat2", "dis2", "hyp2"),  # Round 2: Celarent, ¬Q⊢P, MT
    ]
    
    for round_idx, (cat_key, dis_key, hyp_key) in enumerate(rounds):
        # Sub-titles for each round
        if round_idx == 0:
            sub = Text("形式 1", font=DEFAULT_FONT, font_size=24, color=GREY).next_to(title, DOWN, buff=0.2)
        else:
            sub = Text("形式 2", font=DEFAULT_FONT, font_size=24, color=GREY).next_to(title, DOWN, buff=0.2)
        scene.play(Write(sub))
        
        # Get content tuples
        cat_content = cast[cat_key]
        dis_content = cast[dis_key]
        hyp_content = cast[hyp_key]
        
        # Get animation steps
        steps_cat = m_cat.get_reasoning_steps(*cat_content, is_correct=True)
        steps_dis = m_dis.get_reasoning_steps(*dis_content, is_correct=True)
        steps_hyp = m_hyp.get_reasoning_steps(*hyp_content, is_correct=True)
        
        # Play in parallel
        all_steps = [steps_cat, steps_dis, steps_hyp]
        max_steps = max(len(s) for s in all_steps)
        
        for i in range(max_steps):
            anims = []
            for steps in all_steps:
                if i < len(steps):
                    anims.extend(steps[i])
            scene.play(*anims)
            scene.wait(0.2)
        
        scene.wait(1)
        scene.play(FadeOut(sub))
    
    scene.wait(2)
    
    # Cleanup - FadeOut all content using machine's clean method
    scene.play(
        m_cat.get_clean_anim(),
        m_dis.get_clean_anim(),
        m_hyp.get_clean_anim()
    )
    scene.play(
        FadeOut(m_cat), FadeOut(m_dis), FadeOut(m_hyp),
        FadeOut(labels), FadeOut(title)
    )
