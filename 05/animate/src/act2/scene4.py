from manim import *
from src.utils import *

class Act2Scene4(BaseScene):
    def construct(self):
        # 重建场景3的元素 (为了简单直接复制构建逻辑，实际应用应封装)
        stock_sky = Ellipse(width=4, height=2, color=BLUE_A, fill_opacity=0.3).to_edge(UP)
        val_sky = DecimalNumber(1000).move_to(stock_sky)
        
        stock_ground = Rectangle(width=6, height=2, color=BROWN, fill_opacity=0.5).to_edge(DOWN)
        val_ground = DecimalNumber(500).move_to(stock_ground)
        
        self.add(stock_sky, val_sky, stock_ground, val_ground)
        
        # 时间轴
        time_label = Text("t = 0", font=DEFAULT_FONT, font_size=36).to_corner(UL)
        self.add(time_label)
        
        # t=0 -> t=1 (蒸发)
        # 假设 rain=0, evap=10
        # Sky: 1000 -> 1010, Ground: 500 -> 490
        
        self.play(
            time_label.animate.become(Text("t = 1", font=DEFAULT_FONT, font_size=36).to_corner(UL)),
            val_sky.animate.set_value(1010),
            val_ground.animate.set_value(490),
            run_time=2
        )
        
        # t=1 -> t=2 (下雨事件发生)
        # Sky: 1010 -> 960 (rain=50), Ground: 490 -> 540
        # 视觉效果: 雨滴出现
        
        rain_drops = VGroup(*[Dot(color=BLUE) for _ in range(10)])
        rain_drops.arrange_in_grid(5, 2).move_to(UP*0.5)
        
        self.play(
            time_label.animate.become(Text("t = 2 (下雨)", font=DEFAULT_FONT, font_size=36, color=BLUE).to_corner(UL)),
            FadeIn(rain_drops),
            rain_drops.animate.shift(DOWN*2), # 下落动画
            val_sky.animate.set_value(960),
            val_ground.animate.set_value(540),
            run_time=2
        )
        
        # t=2 -> t=3 (地湿)
        self.play(
            time_label.animate.become(Text("t = 3 (地湿)", font=DEFAULT_FONT, font_size=36, color=BROWN).to_corner(UL)),
            FadeOut(rain_drops),
            val_sky.animate.set_value(910),
            val_ground.animate.set_value(590),
            run_time=2
        )
        
        self.wait(2)
