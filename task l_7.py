import cv2
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("OCV Tkinter")

imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

label = tk.Label(imageFrame)
label.grid(row=0, column=0)

cap = cv2.VideoCapture(0)

def show_frame():
    global frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    label.image = imgtk
    label.configure(image=imgtk)
    label.after(10, show_frame)

def saveimg():
    cv2.imwrite("H:/PycharmProjects/untitled3/myphoto.png", frame)
    print("Successful")

button = tk.Button(imageFrame, text="Hello", command=saveimg)
button.grid(row=1, column=0)

show_frame()
window.mainloop()
