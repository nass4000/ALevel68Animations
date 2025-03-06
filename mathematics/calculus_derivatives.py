from manim import *
import numpy as np
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import TitleBlock, create_step_by_step, highlight_area

class DerivativeIntroduction(Scene):
    def construct(self):
        # Create title for the animation
        title_block = TitleBlock(
            self,
            "อนุพันธ์และการประยุกต์ใช้",  # Derivatives and Applications
            "แคลคูลัส",  # Calculus
            "mathematics"
        )
        title_block.play()
        self.wait(1)
        
        # Create a coordinate system
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-1, 9],
            axis_config={"include_tip": True}
        )
        
        # Add labels - using Text instead of MathTex
        x_label = Text("x", font_size=24).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("y", font_size=24).next_to(axes.y_axis, LEFT, buff=0.2)
        
        # Create a graph of f(x) = x²
        graph = axes.plot(lambda x: x**2, color=BLUE)
        graph_label = Text("f(x) = x²", font_size=24).next_to(graph, UR, buff=0.5)
        
        # Display the coordinate system and graph
        self.play(
            FadeIn(axes, x_label, y_label),
            run_time=1
        )
        self.play(
            Create(graph),
            Write(graph_label),
            run_time=2
        )
        self.wait(1)
        
        # Explanation text
        derivative_def = Text("อนุพันธ์คือความชันของเส้นสัมผัสที่จุดใดๆบนกราฟ", font_size=24)
        derivative_def.to_edge(UP, buff=1.5)
        
        self.play(
            Write(derivative_def),
            run_time=1
        )
        self.wait(1)
        
        # Choose a point on the graph
        x_point = 2
        point = Dot(axes.c2p(x_point, x_point**2), color=RED)
        point_label = Text(f"({x_point}, {x_point**2})", font_size=24).next_to(point, UP)
        
        self.play(
            FadeIn(point),
            Write(point_label),
            run_time=1
        )
        
        # Create the tangent line at x = 2
        tangent_slope = 2 * x_point  # Derivative of x² is 2x
        
        def tangent_line(x):
            return tangent_slope * (x - x_point) + x_point**2
        
        tangent = axes.plot(tangent_line, x_range=[0, 4], color=GREEN)
        tangent_label = Text("เส้นสัมผัส", font_size=24).next_to(tangent, UR, buff=0.5)  # Tangent Line
        
        self.play(
            Create(tangent),
            Write(tangent_label),
            run_time=1
        )
        self.wait(1)
        
        # Show the derivative formula using Text instead of MathTex
        derivative_eq = Text(
            "f'(x) = lim[h→0] [f(x+h) - f(x)]/h", font_size=28
        )
        derivative_eq.to_edge(DOWN, buff=1)
        
        self.play(
            Write(derivative_eq),
            run_time=2
        )
        self.wait(1)
        
        # Show the derivative of x²
        derivative_result = Text(
            "f'(x) = 2x", font_size=28
        )
        derivative_result.next_to(derivative_eq, UP)
        
        self.play(
            Write(derivative_result),
            run_time=1
        )
        self.wait(1)
        
        # Highlight the slope at x = 2
        slope_eq = Text(
            f"f'({x_point}) = {2*x_point}", font_size=28
        )
        slope_eq.next_to(derivative_result, UP)
        
        self.play(
            Write(slope_eq),
            run_time=1
        )
        self.wait(1)
        
        # Applications of derivatives
        self.play(
            FadeOut(derivative_def, point_label, tangent_label, 
                    derivative_eq, derivative_result, slope_eq),
            run_time=1
        )
        
        applications_title = Text("การประยุกต์ใช้อนุพันธ์", font_size=32)  # Applications of Derivatives
        applications_title.to_edge(UP)
        
        self.play(
            FadeOut(title_block.title, title_block.subtitle),
            Write(applications_title),
            run_time=1
        )
        
        # Create a list of applications
        applications = [
            "หาค่าสูงสุด-ต่ำสุด (Optimization)",  # Finding maximum/minimum values
            "หาอัตราการเปลี่ยนแปลง (Rates of Change)",  # Finding rates of change
            "คำนวณความเร็วและความเร่ง (Velocity and Acceleration)",  # Calculating velocity and acceleration
            "ประมาณค่าด้วยเส้นสัมผัส (Linear Approximation)"  # Linear approximation
        ]
        
        # Create step-by-step applications
        app_steps = create_step_by_step(self, applications, UP * 0.5, DOWN)
        
        for step in app_steps:
            self.play(Write(step), run_time=0.7)
            self.wait(0.5)
        
        self.wait(2)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        self.wait(1)
