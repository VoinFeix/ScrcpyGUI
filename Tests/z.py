# Source - https://stackoverflow.com/a
# Posted by furas, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-05, License - CC BY-SA 4.0

import tkinter as tk
import time
import random
import threading
import queue


def bubble_sort(canvas, data, q):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                #draw_data(canvas, data)
                q.put(data)  # <-- send data to main thread
                time.sleep(0.5)  # <-- freezes the UI
    q.put('end')  # <-- send info to main thread

def draw_data(canvas, q):
    global thread

    if q.not_empty:
        data = q.get()
        if data == 'end':
            thread = None  # <-- set None so it can be run again
            return

        canvas.delete("all")
        for i, val in enumerate(data):
            canvas.create_rectangle(i*20, 200-val, (i+1)*20, 200, fill="blue")

    # repeat after 100ms
    root.after(100, draw_data, canvas, q)

def start_sort():
    global thread

    if thread is None:
        q = queue.Queue()
        data = [random.randint(0,100) for _ in range(20)]
        thread = threading.Thread(target=bubble_sort, args=(canvas, data, q) )
        thread.start()
        root.after(0, draw_data, canvas, q)
    else:
        print("thread is already running")

# -----

thread = None  # <-- used as information if thread is running or not

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=200)
canvas.pack()

btn = tk.Button(root, text="Start", command=start_sort)
btn.pack()

root.mainloop()
