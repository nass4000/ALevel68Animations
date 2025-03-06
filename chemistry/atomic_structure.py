from manim import *
import numpy as np
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import TitleBlock, create_step_by_step, highlight_area

class AtomicStructure(Scene):
    def construct(self):
        # Create title for the animation
        title_block = TitleBlock(
            self,
            "โครงสร้างอะตอม",  # Atomic Structure
            "พื้นฐานทางเคมี",  # Chemistry Basics
            "chemistry"
        )
        title_block.play()
        self.wait(1)
        
        # Introduction text
        intro = Text("อะตอมประกอบด้วยโปรตอน นิวตรอน และอิเล็กตรอน", font_size=24)  # Atoms consist of protons, neutrons, and electrons
        intro.next_to(title_block.title, DOWN, buff=1)
        
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        
        # Create a simple Bohr model of an atom (Helium)
        # Nucleus
        nucleus = Circle(radius=0.5, color=RED, fill_opacity=0.8)
        
        # Labels for protons and neutrons
        nucleus_label = Text("นิวเคลียส", font_size=20).next_to(nucleus, DOWN, buff=0.2)  # Nucleus
        proton_text = Text("โปรตอน: 2", font_size=16, color=RED).next_to(nucleus_label, DOWN, buff=0.2)  # Protons: 2
        neutron_text = Text("นิวตรอน: 2", font_size=16, color=BLUE).next_to(proton_text, DOWN, buff=0.2)  # Neutrons: 2
        
        # First electron shell (K shell)
        shell1 = Circle(radius=1.5, color=WHITE)
        
        # Electrons
        electron1 = Dot(color=BLUE)
        electron2 = Dot(color=BLUE)
        
        # Position electrons on opposite sides of the shell
        electron1.move_to(shell1.point_at_angle(0))
        electron2.move_to(shell1.point_at_angle(PI))
        
        # Electron label
        electron_text = Text("อิเล็กตรอน: 2", font_size=16, color=BLUE).next_to(neutron_text, DOWN, buff=0.2)  # Electrons: 2
        
        # Element label
        element_label = Text("ฮีเลียม (He)", font_size=24).to_edge(UP, buff=1.5)  # Helium (He)
        
        # Add all components to the scene
        self.play(
            Create(nucleus),
            Write(nucleus_label),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(
            Write(proton_text),
            Write(neutron_text),
            run_time=1
        )
        self.wait(0.5)
        
        self.play(
            Create(shell1),
            run_time=1
        )
        
        self.play(
            FadeIn(electron1),
            FadeIn(electron2),
            Write(electron_text),
            run_time=1
        )
        
        self.play(
            Write(element_label),
            run_time=1
        )
        self.wait(1)
        
        # Animate electrons orbiting the nucleus
        self.play(
            Rotating(
                electron1,
                about_point=ORIGIN,
                rate=0.5,
                run_time=4
            ),
            Rotating(
                electron2,
                about_point=ORIGIN,
                rate=0.5,
                run_time=4
            ),
            rate_func=linear
        )
        self.wait(1)
        
        # Clean up for the next section
        self.play(
            *[FadeOut(mob) for mob in [element_label, nucleus_label, proton_text, neutron_text, electron_text]],
            run_time=1
        )
        
        # Show different elements in the periodic table
        elements_title = Text("ธาตุในตารางธาตุ", font_size=32).to_edge(UP)  # Elements in the Periodic Table
        
        self.play(
            FadeOut(title_block.title, title_block.subtitle),
            Write(elements_title),
            run_time=1
        )
        
        # Atomic Structure Information
        atomic_info = VGroup(
            Text("โครงสร้างอะตอมกำหนดสมบัติของธาตุ", font_size=24),  # Atomic structure determines properties of elements
            Text("เลขอะตอม = จำนวนโปรตอน", font_size=24),  # Atomic number = number of protons
            Text("มวลอะตอม = จำนวนโปรตอน + จำนวนนิวตรอน", font_size=24)  # Atomic mass = protons + neutrons
        ).arrange(DOWN, buff=0.5).next_to(elements_title, DOWN, buff=1)
        
        for info in atomic_info:
            self.play(Write(info), run_time=1)
            self.wait(0.5)
        
        self.wait(1)
        
        # Introduction to electron configuration
        electron_config_title = Text("การจัดเรียงอิเล็กตรอน", font_size=28)  # Electron Configuration
        electron_config_title.next_to(atomic_info, DOWN, buff=1)
        
        self.play(Write(electron_config_title), run_time=1)
        
        # Example electron configurations
        config_examples = VGroup(
            Text("H: 1s¹", font_size=24),
            Text("He: 1s²", font_size=24),
            Text("Li: 1s² 2s¹", font_size=24),
            Text("Na: 1s² 2s² 2p⁶ 3s¹", font_size=24)
        ).arrange(DOWN, buff=0.3).next_to(electron_config_title, DOWN, buff=0.5)
        
        for example in config_examples:
            self.play(Write(example), run_time=0.7)
        
        self.wait(2)
        
        # Clean up
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        self.wait(1)
