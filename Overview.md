# EA1

## Package/Library Ovierview

### 1.Selected Package/Library
   The selected package/library is __Tkinter__.

### 2.What is Tkinter?
   Tkinter is a standard GUI(Graphical User Interface) toolkit in Python. It provides
   a fast and easy way to create desktop applications with graphical interfaces.

#### Purpose:
   Tkinter serves the purpose of creating graphical user interfaces for Python
   applications. It allows developers to create window, dialogs, buttons, menus, and
   other GUI elements to build interactive applications.
   
#### Using:
   To use Tkinter, we need to import it into our Python script using __import tkinter__.
Then, we can create GUI elements like windows, frames, buttons, labels, and canvas using
various Tkinter classes and methods.

 __Example:__
```python
import tkinter as Tkinter

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
#### Output:
   Try these code.

   
## References
  1. https://docs.python.org/3/library/tkinter.html
  2. https://www.tutorialspoint.com/python/python_gui_programming.htm

