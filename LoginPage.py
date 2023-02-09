from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry,Button, PhotoImage,StringVar,messagebox as mg


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(rf"{OUTPUT_PATH}\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

status = False
def submissionFunc():
    global status
    if username.get()=="admin" and passw.get()=="admin":
        status= True
        window.destroy()
    else:
        status=False
        mg.showwarning("User Error","Please Enter a Valid Username and Password.")


window = Tk()
username = StringVar()
passw =  StringVar()
window.geometry("1000x700")
window.configure(bg = "#363740")
canvas = Canvas(
    window,
    bg = "#363740",
    height = 700,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    506.0,
    386.0,
    anchor="nw",
    text="Password",
    fill="#4A4F6C",
    font=("Mulish Regular", 14 * -1)
)

canvas.create_rectangle(
    310.0,
    59.0,
    690.0,
    641.0,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("Lgbutton_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= submissionFunc,
    relief="flat"
)
button_1.place(
    x=342.0,
    y=501.0,
    width=316.0,
    height=48.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("Lgentry_1.png"))
entry_bg_1 = canvas.create_image(
    500.0,
    368.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FCFDFE",
    fg="#000716",
    highlightthickness=0,
    textvariable=passw
)
entry_1.place(
    x=350.0,
    y=347.0,
    width=300.0,
    height=40.0
)

canvas.create_text(
    358.0,
    358.0,
    anchor="nw",
    text="Username",
    fill="#4A4F6C",
    font=("Mulish Regular", 14 * -1)
)

canvas.create_text(
    342.0,
    325.0,
    anchor="nw",
    text="Username",
    fill="#9FA2B4",
    font=("Mulish Bold", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("Lgentry_2.png"))
entry_bg_2 = canvas.create_image(
    500.0,
    456.0,
    image=entry_image_2,

)
entry_2 = Entry(
    bd=0,
    bg="#FCFDFE",
    fg="#000716",
    highlightthickness=0,
    textvariable=username
)
entry_2.place(
    x=350.0,
    y=428.0,
    width=300.0,
    height=50.0
)

canvas.create_text(
    342.0,
    413.0,
    anchor="nw",
    text="PASSWORD",
    fill="#9FA2B4",
    font=("Mulish Bold", 12 * -1)
)

canvas.create_text(
    358.0,
    446.0,
    anchor="nw",
    text="Password",
    fill="#4A4F6C",
    font=("Mulish Regular", 14 * -1)
)

canvas.create_text(
    342.0,
    257.0,
    anchor="nw",
    text="Enter your Username and password below",
    fill="#9FA2B4",
    font=("Mulish Regular", 14 * -1)
)

canvas.create_text(
    342.0,
    159.0,
    anchor="nw",
    text="Admin Access",
    fill="#A4A6B3",
    font=("Mulish Bold", 19 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("Lgimage_1.png"))
image_1 = canvas.create_image(
    500.0,
    123.0,
    image=image_image_1
)

canvas.create_text(
    342.0,
    215.0,
    anchor="nw",
    text="Log In to Account",
    fill="#252733",
    font=("Mulish Bold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
