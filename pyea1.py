from tkinter import *
from tkinter import ttk

class MovingText:
   def __init__(self, master):
      self.master = master
      self.master.title("Moving Text")
      
      self.notebook = ttk.Notebook(master)
      self.notebook.pack(fill=BOTH, expand="True")
      
      self.tab1 = Frame(self.notebook)
      self.notebook.add(self.tab1, text="Display")
      self.canvas = Canvas(self.tab1, bg="#FF6060")
      self.canvas.pack(fill=BOTH, expand="True")
      self.fps = 40
      self.setup_text()
      self.shift()
      
      self.tab2 = Frame(self.notebook)
      self.notebook.add(self.tab2, text="Text")
      self.input_tab()

   def setup_text(self):
      self.text = "Happy Valentine's Day!"
      self.text_object = self.canvas.create_text(0, -1000, text=self.text, 
                         font=("Times New Roman", 30, "bold"),
                         fill="white", tags=("text"), anchor="w")
      x1, y1, x2, y2 = self.canvas.bbox("text")
      width = x2 - x1
      height = y2 - y1
      self.canvas["width"] = width
      self.canvas["height"] = height
   
   def shift(self):
      x1, y1, x2, y2 = self.canvas.bbox("text")
      if x2 < 0 or y1 < 0:
         x1 = self.canvas.winfo_width()
         y1 = self.canvas.winfo_height() // 2
         self.canvas.coords("text", x1, y1)
      else:
         self.canvas.move("text", -2, 0)
      self.master.after(1000 // 40, self.shift)
      
   def input_tab(self):
      self.text_entry = Text(self.tab2, height=5, width=50)
      self.text_entry.pack()
      edit_button = Button(self.tab2, text="Edit", command=self.edit_text)
      edit_button.pack()
   
   def edit_text(self):
      text = self.text_entry.get("1.0", END).strip()
      self.text = text
      self.canvas.itemconfig(self.text_object, text=text)
      self.text_entry.delete("1.0", END)

if __name__ == "__main__":
   root = Tk()
   app = MovingText(root)
   root.mainloop()
