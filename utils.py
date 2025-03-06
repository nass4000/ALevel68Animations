from manim import *

class TitleBlock:
    """A reusable title block for Thai A-Level tutorials"""
    
    def __init__(self, scene, title_text, subtitle_text=None, subject=""):
        """
        Create a standardized title block for animations
        
        Args:
            scene: The Manim scene
            title_text: Main title of the animation
            subtitle_text: Optional subtitle
            subject: Subject area (physics, math, chemistry)
        """
        self.scene = scene
        
        # Create title with subject tag
        subject_tag = ""
        if subject.lower() == "physics":
            subject_tag = "[ฟิสิกส์] "
            color = "#3498db"  # Blue for physics
        elif subject.lower() == "mathematics" or subject.lower() == "math":
            subject_tag = "[คณิตศาสตร์] "
            color = "#e74c3c"  # Red for mathematics
        elif subject.lower() == "chemistry":
            subject_tag = "[เคมี] "
            color = "#2ecc71"  # Green for chemistry
            
        # Create the title
        self.title = Text(f"{subject_tag}{title_text}", font_size=36)
        self.title.to_edge(UP)
        
        # Create subtitle if provided
        if subtitle_text:
            self.subtitle = Text(subtitle_text, font_size=24)
            self.subtitle.next_to(self.title, DOWN)
        else:
            self.subtitle = None
            
    def play(self, animate=True):
        """Display the title block with animation"""
        if animate:
            self.scene.play(Write(self.title), run_time=1)
            if self.subtitle:
                self.scene.play(FadeIn(self.subtitle), run_time=0.5)
        else:
            self.scene.add(self.title)
            if self.subtitle:
                self.scene.add(self.subtitle)
                
    def clear(self, animate=True):
        """Remove the title block"""
        if animate:
            animations = [FadeOut(self.title)]
            if self.subtitle:
                animations.append(FadeOut(self.subtitle))
            self.scene.play(*animations, run_time=0.5)
        else:
            self.scene.remove(self.title)
            if self.subtitle:
                self.scene.remove(self.subtitle)


def create_step_by_step(scene, steps, position=ORIGIN, direction=DOWN):
    """
    Create a step-by-step animation for explanations
    
    Args:
        scene: The Manim scene
        steps: List of strings representing each step
        position: Starting position
        direction: Direction to add new steps
    """
    current_pos = position
    step_mobjects = []
    
    for i, step_text in enumerate(steps):
        step = Text(f"{i+1}. {step_text}", font_size=24)
        step.move_to(current_pos)
        step_mobjects.append(step)
        current_pos += direction * step.height * 1.2
    
    return step_mobjects


def highlight_area(scene, mobject, color=YELLOW, opacity=0.3):
    """Creates a highlight around a mobject"""
    highlight = SurroundingRectangle(mobject, color=color, fill_opacity=opacity)
    scene.play(Create(highlight))
    return highlight
