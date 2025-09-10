import cv2 as cv
from tkinter import *
from PIL import Image, ImageTk

#ask function
def ASK():
    print("ASK")

#send function        
def SEND():
    print("SEND")
    
#delete function
def DELETE():
    print("DELETE")

root = Tk()
root.title("AURA")
root.geometry("800x800")
root.resizable(False, False)
root.config(bg="#1e1e1e")

# Frame
frame = LabelFrame(
    root,             
    padx=40,         
    pady=10,          
    borderwidth=3,   
    relief="raised", 
)     
frame.config(bg="#E9EFF4")
frame.grid(row = 0 ,  column= 1 ,  padx= 220 ,  pady =  10)

# Label
label = Label(
    frame,
    text="AURA",
    font=("Arial", 24, "bold"),     
    bg="#FBF7F7"      
)
label.pack(pady=8)

# Load image
cv_img = cv.imread(r"C:\Users\HP\OneDrive\Music\Documents\AURA.img.jpg")
cv_img = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)  

# Resize
pil_img = Image.fromarray(cv_img).resize((300, 300))

# Convert to ImageTk
img_tk = ImageTk.PhotoImage(pil_img)

# Image label
image_label = Label(frame, image=img_tk, bg="#FBF7F7")
image_label.image = img_tk  
image_label.pack(pady=10)

# Text widget
text = Text(root, font=("Courier 12 bold"), bg="#FBF7F7")
text.place(x=220, y=420, width=388, height=100)

# Entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=220, y=550, width=388, height=40)

# Button function
Button1 = Button(root, text="  ASK  ", font=("Arial", 14), bg="#393B39", pady= 20, padx =20, borderwidth= 3,relief = SOLID,command=ASK, fg="white")
Button1.place(x=220, y=620)

Button2 = Button(root, text=" SEND ", font=("Arial", 14), bg="#393B39", pady= 20, padx =20, borderwidth= 3,relief = SOLID,command=SEND, fg="white")
Button2.place(x=348, y=620)

Button3 = Button(root, text="DELETE", font=("Arial", 14), bg="#393B39", pady= 20, padx =20, borderwidth= 3,relief = SOLID,command=DELETE, fg="white")
Button3.place(x=482, y=620)

# Start the GUI loop
root.mainloop()
