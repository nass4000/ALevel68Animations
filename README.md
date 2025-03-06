# Thai A-Level Tutorials with Manim

This project uses Manim (Mathematical Animation Engine) to create educational animations for Thai A-Level test preparation in Physics, Mathematics, and Chemistry.

## Project Structure

```
ALevel68Animations/
├── requirements.txt       # Project dependencies
├── README.md             # This file
├── examples/             # Example animations
├── utils.py              # Utility functions and reusable components
├── assets/               # Images, fonts, etc.
├── physics/              # Physics animations
│   └── projectile_motion.py  # Projectile motion simulations
├── mathematics/          # Mathematics animations
│   └── calculus_derivatives.py  # Calculus animations
└── chemistry/            # Chemistry animations
    └── atomic_structure.py  # Atomic structure visualizations
```

## Features

- Educational animations tailored for Thai A-Level curriculum
- No LaTeX dependency required - all mathematical formulas use Manim's Text objects
- Consistent styling with reusable components
- Thai language support

## Installation

1. Clone this repository:
```bash
git clone https://github.com/nass4000/ALevel68Animations.git
cd ALevel68Animations
```

2. Set up a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Animations

To render an animation:

```bash
manim -pql physics/projectile_motion.py ExampleScene
```

Or use the provided batch file on Windows:
```bash
run_manim.bat physics/projectile_motion.py ExampleScene
```

Parameters:
- `-p`: Preview the animation once it's rendered
- `-l`: Use low quality (faster)
- `-ql`: Use medium quality
- `-qh`: Use high quality (slower)

## Project Notes

- All animations use Text objects instead of MathTex, eliminating the need for a LaTeX installation
- The project includes TitleBlock and other reusable components in utils.py
- Manim version used: v0.17.3

## Contributing

Feel free to add new animations or improve existing ones!

## License

MIT
