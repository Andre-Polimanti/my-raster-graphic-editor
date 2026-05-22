# My Raster Graphic Editor
This project contains a Desktop App that represents my introdution to graphic computation, my goal is to present an app that enables the user to draw in a 2D Canvas with basic functionalities, such as Lines, Curves, Simple Geometric Shapes, etc.

## Memory Architecture
In this application, the FrontBuffer object acts as "permanent" memory that stores the edited Canvas, while the BackBuffer acts as a temporary one, that carries the current editing action, being cleared at each edit commmit or abortion.

## Data Processing Brief Overview
The flow of data starts at the BackBuffer object, if the edit is committed, it goes to the FrontBuffer, by the use of BackBuffer's commit() method. From there, it is passed to OpenGL buffers with the use of the function glDrawPixels(). If the edit is aborted, the edit data is cleared at the start object(BackBuffer), by it's clear() method, not being passed any further.


A feature presented in this project is the Live Tool Preview, that enables the view of a Draw Tool while in the process of using it, we can see it in real time, accompaning the mouse awaiting it's commit or abortion. This is achieved by rendering the BackBuffer(Temporary Memory) over the FrontBuffer(Canvas), since the BackBuffer's background is transparent, contrary to the FrontBuffer.

## Controls
### Keyboard
- P: Abort current edit
- Q: Reset the entire Canvas back to it's background color
- ESC: Close application