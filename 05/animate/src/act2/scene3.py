from manim import *
from src.utils import *

class Act2Scene3(BaseScene):
    def construct(self):
        # 场景: 水循环系统 Stock-Flow
        
        # Stock 1: 大气水量 (云朵)
        # 用椭圆模拟云朵
        stock_sky = Ellipse(width=4, height=2, color=BLUE_A, fill_opacity=0.3).to_edge(UP)
        label_sky = Text("大气水量", font=DEFAULT_FONT).move_to(stock_sky)
        val_sky = DecimalNumber(1000).next_to(label_sky, DOWN)
        
        # Stock 2: 地表水量 (矩形)
        stock_ground = Rectangle(width=6, height=2, color=BROWN, fill_opacity=0.5).to_edge(DOWN)
        label_ground = Text("地表水量", font=DEFAULT_FONT).move_to(stock_ground)
        val_ground = DecimalNumber(500).next_to(label_ground, DOWN)
        
        # Flows
        # 降雨: Sky -> Ground
        arrow_rain = Arrow(stock_sky.get_bottom(), stock_ground.get_top(), color=BLUE_E, buff=0.5)
        label_rain = Text("降雨流", font=DEFAULT_FONT, font_size=24).next_to(arrow_rain, RIGHT)
        
        # 蒸发: Ground -> Sky (左侧上行虚线箭头)
        arrow_evap = DashedLine(stock_ground.get_top() + LEFT*2, stock_sky.get_bottom() + LEFT*2, color=BLUE_B).add_tip()
        label_evap = Text("蒸发流", font=DEFAULT_FONT, font_size=24).next_to(arrow_evap, LEFT)
        
        self.add(stock_sky, label_sky, val_sky)
        self.add(stock_ground, label_ground, val_ground)
        self.play(Create(arrow_rain), Write(label_rain))
        self.play(Create(arrow_evap), Write(label_evap))
        
        # 简单的动态效果: 数值波动
        self.play(
            val_sky.animate.set_value(1010),
            val_ground.animate.set_value(490),
            run_time=2
        )
        
        self.wait(2)
