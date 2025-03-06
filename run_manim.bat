@echo off
setlocal

REM Set paths for portable environment
set PATH=%~dp0ffmpeg\bin;%PATH%
set TEXMF=%~dp0miktex\texmfs

REM Create a .manim.cfg file if it doesn't exist
if not exist "%~dp0.manim.cfg" (
    echo [CLI] > "%~dp0.manim.cfg"
    echo tex_template = basic >> "%~dp0.manim.cfg"
)

REM Activate the virtual environment and run manim
call .venv\Scripts\activate.bat
if "%1"=="" (
    echo Usage: run_manim.bat [scene_file] [scene_class] [quality]
    echo Example: run_manim.bat examples/example_scene.py BasicExample -ql
) else (
    if "%3"=="" (
        .venv\Scripts\python -m manim -pql %1 %2
    ) else (
        .venv\Scripts\python -m manim -p %3 %1 %2
    )
)

endlocal
