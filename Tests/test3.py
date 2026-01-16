import tkinter as tk

root = tk.Tk()
root.geometry('400x400')

frame1 = tk.Frame(root, relief="groove", borderwidth=3)
frame1.grid(row=0, column=0, padx=10, pady=10)

tk.Button(frame1, text='Button', relief='raised', bd=3).pack(pady=5)
tk.Button(frame1, text='Button', relief='raised', bd=3).pack(pady=5)
tk.Button(frame1, text='Button', relief='raised', bd=3).pack(pady=5)

frame2 = tk.Frame(root, relief='ridge', borderwidth=3)
frame2.grid(row=0, column=1, padx=10, pady=10)

frame3 = tk.Frame(root, relief='groove', borderwidth=2)
frame3.grid(row=1, column=0, padx=10, pady=10)

# Frame 2 → horizontal shelf
tk.Button(frame2, text='Button', relief='raised', bd=3).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame2, text='Button', relief='raised', bd=3).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame2, text='Button', relief='raised', bd=3).grid(row=0, column=2, padx=5, pady=5)

# Frame 3 → vertical shelf
tk.Button(frame3, text='Button', relief='raised', bd=3).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame3, text='Button', relief='raised', bd=3).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame3, text='Button', relief='raised', bd=3).grid(row=2, column=0, padx=5, pady=5)

for i in range(3):
    frame2.grid_rowconfigure(i, weight=1)
    frame2.grid_columnconfigure(i, weight=1)

















root.mainloop()
