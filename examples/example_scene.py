from manim import *

class BasicExample(Scene):
    def construct(self):
        # Create a title for the animation
        title = Text("Thai A-Level Tutorial", font_size=36)
        title.to_edge(UP)
        
        # Create a subtitle
        subtitle = Text("Basic Manim Example", font_size=24)
        subtitle.next_to(title, DOWN)
        
        # Display the title and subtitle
        self.play(Write(title), run_time=1)
        self.play(FadeIn(subtitle), run_time=0.5)
        self.wait(1)
        
        # Create and display a text equation instead of MathTex
        eq = Text("E = mc²", font_size=48)
        self.play(Write(eq))
        self.wait(1)
        
        # Transform to another text equation
        eq2 = Text("E² = (mc²)² + (pc)²", font_size=48)
        self.play(Transform(eq, eq2))
        self.wait(1)
        
        # Create a circle and a square
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=GREEN)
        
        # Position them
        circle.shift(LEFT * 2.5)
        square.shift(RIGHT * 2.5)
        
        # Display them
        self.play(Create(circle), Create(square), run_time=1)
        self.wait(1)
        
        # Animate them
        self.play(
            circle.animate.scale(0.5),
            square.animate.rotate(PI/4),
            run_time=1
        )
        self.wait(1)
        
        # Add text to explain
        explanation = Text("This is just the beginning!", font_size=24)
        explanation.next_to(eq, DOWN, buff=1)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        self.wait(1)
