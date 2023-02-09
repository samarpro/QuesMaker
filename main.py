from docx import Document
from pathlib import Path
from os import getcwd
from win32api import GetSystemMetrics
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, filedialog, END
from tkinter import messagebox as mg
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(rf"{OUTPUT_PATH}\assets\frame0")

outPathSendable = getcwd()
inPathSendable = ""

def pathSelect(no):
    """
    function to validate path and assign value to variable which are used by another function = onClickSub()
    """
    # path is the variable name which takes path from the dialogBox
    global path, outPathSendable, inPathSendable
    # default path of output folder which changes when user specifically chooses the path
    path = outPathSendable = getcwd()
    # output_path stores the value of both the input and output direcotry which later can't be used since the earlier value gets over written
    if no == 1:
        try:
            path = filedialog.askopenfile().name
            # lenght of the path string
            LenPath = len(path)-1
            # converting text to lowercase for validation and checking wheather the input file is input is or not
            if (path[LenPath:LenPath-4:-1].lower() != "xcod" and path[LenPath:LenPath-3:-1].lower() != "cod"):
                mg.showerror("File Selection Error",
                             "The file you selected is not a word file.")
                return
            entry_1.delete(0, END)
            entry_1.insert(0, path)
            inPathSendable = path

        except:
            mg.showerror("Error", "Input File is not selected.")
            entry_1.insert(0, "")

    else:
        path = filedialog.askdirectory()
        entry_2.delete(0, END)
        entry_2.insert(0, path)
        outPathSendable = path


def onClickSub():
    global inPathSendable
    if (inPathSendable == "" and TempInpLoc.get()==""):
        mg.showerror("Directory Path Error",
                     "Path of the file must be provided.")
        return
    else:
        inPathSendable=TempInpLoc.get()
    try:
        window.destroy()
    except:

        mg.showerror("Directory Path Error",
                     "Path of the file must be provided")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Getting width and height of the screen
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
window = Tk()
window.title("DeQuestify")
TempInpLoc = StringVar()
# TempOutLoc = StringVar()
window.geometry(f"1000x{height-90}+{(width//2)-500}+5")
window.configure(bg="#FFFFFF")
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=733,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("Inimage_1.png"))
image_1 = canvas.create_image(
    500.0,
    366.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("Inimage_2.png"))
image_2 = canvas.create_image(
    310.0,
    318.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("Inimage_3.png"))
image_3 = canvas.create_image(
    689.0,
    339.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("Inimage_4.png"))
image_4 = canvas.create_image(
    378.0,
    392.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("Inimage_5.png"))
image_5 = canvas.create_image(
    42.0,
    36.0,
    image=image_image_5
)

canvas.create_text(
    561.0,
    128.0,
    anchor="nw",
    text="Enter",
    fill="#000000",
    font=("Inter ExtraBold", 36 * -1)
)

canvas.create_text(
    561.0,
    174.0,
    anchor="nw",
    text="Details",
    fill="#000000",
    font=("Inter ExtraBold", 36 * -1)
)

canvas.create_text(
    561.0,
    242.0,
    anchor="nw",
    text="Input File Directory",
    fill="#0A779A",
    font=("Inter ExtraBold", 19 * -1)
)

canvas.create_text(
    561.0,
    318.0,
    anchor="nw",
    text="Output File Directory",
    fill="#0A779A",
    font=("Inter ExtraBold", 19 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("Inbutton_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=onClickSub,
    relief="flat"
)
button_1.place(
    x=605.0,
    y=417.0,
    width=168.619384765625,
    height=51.0
)
path_picker_img = PhotoImage(file=ASSETS_PATH / "path_picker.png")
path_picker_button = Button(
    image=path_picker_img,
    text='',
    compound='center',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pathSelect(1),
    relief='flat')
path_picker_button.place(
    x=840, y=275,
    width=24,
    height=22)

path_picker_img2 = PhotoImage(file=ASSETS_PATH / "path_picker.png")
path_picker_button2 = Button(
    image=path_picker_img2,
    text='',
    compound='center',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pathSelect(2),
    relief='flat')
path_picker_button2.place(
    x=840, y=356,
    width=24,
    height=22)
entry_image_1 = PhotoImage(
    file=relative_to_assets("Inentry_1.png"))
entry_bg_1 = canvas.create_image(
    693.5,
    286.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=TempInpLoc
)
entry_1.place(
    x=565.0,
    y=270.8,
    width=258.0,
    height=29.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("Inentry_2.png"))
entry_bg_2 = canvas.create_image(
    693.5,
    365.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
)
entry_2.place(
    x=565.0,
    y=351.8,
    width=258.0,
    height=29.0
)

canvas.create_text(
    115.0,
    120.0,
    anchor="nw",
    text="Student, Sharpen",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 33 * -1)
)

canvas.create_text(
    116.0,
    154.0,
    anchor="nw",
    text="Their Skills and ",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 33 * -1)
)

canvas.create_text(
    115.0,
    190.0,
    anchor="nw",
    text="Boost Their ",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 33 * -1)
)

canvas.create_text(
    115.0,
    225.0,
    anchor="nw",
    text="Capability!",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 33 * -1)
)

canvas.create_text(
    116.0,
    87.0,
    anchor="nw",
    text="Unleash Your ",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 33 * -1)
)
window.resizable(False, False)
window.mainloop()