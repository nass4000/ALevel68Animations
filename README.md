# Thai A-Level Tutorials with Manim

This project uses Manim (Mathematical Animation Engine) to create educational animations for Thai A-Level test preparation in Physics, Mathematics, and Chemistry.

## Project Structure

```
ALevel68Animations/
├── requirements.txt       # Project dependencies
├── README.md             # This file
├── examples/             # Example animations
├── assets/               # Images, fonts, etc.
├── physics/              # Physics animations
├── mathematics/          # Mathematics animations
└── chemistry/            # Chemistry animations
```

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
manim -pql physics/example_scene.py ExampleScene
```

Parameters:
- `-p`: Preview the animation once it's rendered
- `-l`: Use low quality (faster)
- `-ql`: Use medium quality
- `-qh`: Use high quality (slower)

## Contributing

Feel free to add new animations or improve existing ones!

## License

MIT
