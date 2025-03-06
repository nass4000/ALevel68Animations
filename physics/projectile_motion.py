from manim import *
import numpy as np
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import TitleBlock, create_step_by_step, highlight_area

class ProjectileMotion(Scene):
    def construct(self):
        # Create title for the animation
        title_block = TitleBlock(
            self,
            "การเคลื่อนที่แบบโปรเจกไทล์",  # Projectile Motion
            "กฎการเคลื่อนที่ของนิวตัน",     # Newton's Laws of Motion
            "physics"
        )
        title_block.play()
        self.wait(1)
        
        # Introduction text
        intro = Text("การเคลื่อนที่แบบโปรเจกไทล์คือการเคลื่อนที่ในแนวโค้งภายใต้แรงโน้มถ่วง", font_size=24)
        intro.next_to(title_block.title, DOWN, buff=1)
        
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        
        # Create a ground line
        ground = Line([-6, -3, 0], [6, -3, 0], color=GREEN)
        self.play(Create(ground))
        
        # Set up axes for the projectile motion
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 4, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": False}
        )
        axes.shift(DOWN * 1.5)
        
        # Add labels - using Text instead of MathTex
        x_label = Text("x (m)", font_size=24).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = Text("y (m)", font_size=24).next_to(axes.y_axis, LEFT, buff=0.2)
        
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label)
        )
        
        # Define the projectile motion equations
        def get_projectile_point(t, v0=5, theta=PI/4, g=9.8):
            # Convert the angle to radians
            vx = v0 * np.cos(theta)
            vy = v0 * np.sin(theta)
            
            x = vx * t
            y = vy * t - 0.5 * g * t**2
            
            return axes.c2p(x, y)
        
        # Create the trajectory
        trajectory = ParametricFunction(
            lambda t: get_projectile_point(t),
            t_range=[0, 0.72],  # Time range where y ≥ 0
            color=BLUE
        )
        
        # Create a dot to track the motion
        dot = Dot(color=RED)
        dot.move_to(get_projectile_point(0))
        
        # Animate the motion
        self.play(Create(trajectory), run_time=2)
        self.play(FadeIn(dot))
        
        # Show the dot moving along the trajectory
        self.play(
            MoveAlongPath(dot, trajectory),
            rate_func=linear,
            run_time=2
        )
        self.wait(1)
        
        # Equations of motion - using Text instead of MathTex
        eq_title = Text("สมการการเคลื่อนที่", font_size=32)  # Equations of motion
        eq_title.to_edge(UP)
        
        eq_x = Text("x = v₀ cos(θ) · t", font_size=28)
        eq_y = Text("y = v₀ sin(θ) · t - ½gt²", font_size=28)
        
        eq_group = VGroup(eq_x, eq_y).arrange(DOWN, buff=0.5)
        eq_group.next_to(eq_title, DOWN, buff=0.5)
        
        self.play(
            FadeOut(title_block.title, title_block.subtitle),
            Write(eq_title),
            run_time=1
        )
        self.play(Write(eq_group), run_time=2)
        self.wait(2)
        
        # Highlight key concepts
        hor_motion = Text("การเคลื่อนที่ในแนวราบ: ความเร็วคงที่", font_size=24)  # Horizontal motion: constant velocity
        ver_motion = Text("การเคลื่อนที่ในแนวดิ่ง: ความเร่งคงที่", font_size=24)  # Vertical motion: constant acceleration
        
        motion_group = VGroup(hor_motion, ver_motion).arrange(DOWN, buff=0.5)
        motion_group.next_to(eq_group, DOWN, buff=1)
        
        self.play(Write(hor_motion))
        self.wait(1)
        self.play(Write(ver_motion))
        self.wait(2)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        self.wait(1)
