# My Raster Graphic Editor
This project contains a Desktop App that represents my introdution to graphic computation, my goal is to present an app that enables the user to draw in a 2D Canvas with basic functionalities, such as Lines, Curves, Simple Geometric Shapes, etc.

## Introduction
In this code, the object FrontBuffer is used as "permanent" memory to save the edited Canvas, while the BackBuffer is used as a temporary one, that carries the current editing action, being cleared at each edit commit or abort.

## Code Explanation
The flow of edit data starts at the object BackBuffer, if the edit is commited, it goes to the objet FrontBuffer, by the BackBuffer.commit method use, from there, it is then passed to OpenGL buffers with the use of the function glDrawPoints(). Otherwise, if the edit is aborted, the edit data is cleared in that same object, by it's method clear, not being passed further.


It's worth mentioning that in the process of using a drawing tool, be it a line, pencil or others, we can see that very tool in real time, accompaning the mouse. This is possible by rendereing the BackBuffer(Temporary Memory) over the FrontBuffer(Canvas), since the BackBuffer background color is transparent contrary to the FrontBuffer.

## Instructions
To abort an edit, press the key "P", to close the app, press "ESC" and to reset the Canvas, press "Q".