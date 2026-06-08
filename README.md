# My Raster Graphic Editor
This project contains a Desktop App that represents my introduction to computer graphics, my goal is to present an app that enables the user to draw on a 2D Canvas with basic functionalities, such as Lines, Curves, Simple Geometric Shapes, etc.

## How to run this project
First, clone this repository and enter its folder
```script
git clone https://github.com/Andre-Polimanti/my-raster-graphic-editor.git
cd my-raster-graphic-editor
```
Then, create a local virtual environment and activate it, do so by running:
- On Windows
```script
python -m venv venv
venv\Scripts\activate
```
- On Ubuntu/Debian and Fedora
```script
python3 -m venv venv
source venv/bin/activate
```
Done this, you must install this project dependencies that are listed in the requirements.txt file:
- On Windows
```script
pip install -r requirements.txt
```
- On Ubuntu/Debian
```script
sudo apt update
sudo apt install python3-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev
pip install -r requirements.txt
```
- On Fedora
```script
sudo dnf install gcc python3-devel SDL2-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel freetype-devel
pip install -r requirements.txt
```
Finally, run this project by the command
```script
python src/main.py
```

## Memory Architecture
In this application, the FrontBuffer object acts as "permanent" memory that stores the edited Canvas, while the BackBuffer acts as a temporary one, that carries the current editing action, being cleared whenever an edit is committed or aborted.

## Data Processing Brief Overview
The flow of data starts at the BackBuffer object. If the edit is committed, it goes to the FrontBuffer, by the use of BackBuffer's commit() method. From there, it is passed to OpenGL buffers with the use of the function glDrawPixels(). If the edit is aborted, the edit data is cleared at the start object(BackBuffer), by its clear() method, not being passed any further.


A feature presented in this project is the Live Tool Preview, which enables the view of a Draw Tool while in the process of using it. We can see it in real time, accompanying the mouse awaiting its commit or abortion. This is achieved by rendering the BackBuffer (Temporary Memory) over the FrontBuffer (Canvas), since the BackBuffer's background is transparent, contrary to the opaque FrontBuffer.

## Controls
### Keyboard
#### General
- A: Abort current edit
- Q: Reset the entire Canvas back to its background color
- ESC: Close application
#### Tool shortcuts
- P: Select Pencil
- E: Select Eraser
- L: Select Line



- C: Select Circle
- R: Select Rectangle


- F: Filling Tool Switch

##### Tool resizing
- 1: Default size (Minimum)
- 2: Medium size
- 3: Maximum size

### Mouse
- The button with an X is for clearing the Canvas
- The button with an Circle inside is for exporting the current canvas as an image file