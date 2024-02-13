# EA1

## Package/Library Ovierview

### 1.Selected Package/Library
   The selected package/library is __Tkinter__.

### 2.What is Tkinter?
   Tkinter is a standard GUI(Graphical User Interface) toolkit in Python. It provides
a fast and easy way to create desktop applications with graphical interfaces[1].

#### Purpose:
   Tkinter serves the purpose of creating graphical user interfaces for Python
applications. It allows developers to create window, dialogs, buttons, menus, and
other GUI elements to build interactive applications.
   
#### Using:
   To use Tkinter, we need to import it into our Python script using __import tkinter__.
Then, we can create GUI elements like windows, frames, buttons, labels, and canvas using
various Tkinter classes and methods.

 

### 3.Functionalities of Tkinter:
   + Creating windows and frames
   + Adding buttons, labels, text entry widgets, and other GUI elements
   + Handling user events like button clicks and key presses
   + Drawing graphics with the Canvas widgets
   + Building menu bars and context menus
   + Organizing widgets using layout managers like grid, pack, and place
   
 __Example:__
 
```python
import tkinter as tk

root = tk.Tk()
root.title("Example")

# Creating a label
label = tk.Label(root, text="Hello World")
label.pack()

# Creating a button
button = tk.Button(root, text="Click Here")
button.pack()

root.mainloop()
```
 __Output:__
 
![sample_image](sample_image.png)

### 4.Create Date
   Tkinter has been part of Python's standard library since the early versions of Python.
It has been actively developed and maintained over the years[3].

### 5.Why Tkinter?
   Tkinter is selected because it is a built-in library, making it readily available for
all Python installations without the need for additional installations. Additionally,
Tkinter provides a simple and easy-to-use interface for creating GUI applications,
making it suitable for beginners.

### 6.Influence on Learning
   Learning Tkinter has provided insights into GUI development in Python and enhanced
understanding of event-driven programming concepts. It has expanded my skills in building
interactive applications and provided a foundation for exploring other GUI libraries.

### 7.Overall Experience
   Tkinter offers a smooth learning curve and comprehensive documentation, making it easy
to get started with GUI development in Python. I would recommend Tkinter to beginners
and anyone who looking for a simple solution for creating desktop applications.
   Personally, I would continue using Tkinter for projects requiring simple to moderate
complexity GUIs due to its reliability and ease of use. However, for more advanced and
feature-rich applications, exploring other GUI libraries might be necessary. 
   
## References:
  [1] https://docs.python.org/3/library/tkinter.html
  [2] https://www.tutorialspoint.com/python/python_gui_programming.htm
  [3] https://subscription.packtpub.com/book/programming/9781788835886/1/ch01lvl1sec10/introducing-tkinter-and-tk

