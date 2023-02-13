# for infopage
# from main import inPathSendableObj, outPathSendable,inPathSendableSub,typeQ
from docx import Document
from pathlib import Path
from os import path
from win32api import GetSystemMetrics
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, IntVar, Button, PhotoImage, filedialog, END, messagebox as mg,Label
from random import sample
# completed importing stuffs.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(rf"{OUTPUT_PATH}\assets\frame0")


# temp code
outPathSendable = "OutDoc.doc"
inPathSendableObj = "C:/Users/LENOVO/OneDrive/Desktop/QuesLong..docx"
inPathSendableSub="path of subjective"
typeQ = 0
# Universally used stuffs
letters = ["A", "B", "C", "D", "E"]
InDoc = Document(inPathSendableObj)
noPara = len(InDoc.paragraphs)
noOfQuestFound = noPara//5
# getting system Metrices
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# returns a relative path of files


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# function which runs the query of selecting path


def pathSelect(no):
    # 1 equivalents to searching for a file
    # else searching for a folder
    if no == 1:
        global inPathSendableObj, outPathSendable
        try:
            # for file selection
            path = filedialog.askopenfile().name
            # this is done to change the value of Input foolder path when user decides to change the previous file
            inPathSendableObj = path
            # redefining instance of Document class
            global InDoc
            InDoc = Document(inPathSendableObj)
            # lenght of the path string
            LenPath = len(path)-1
            # converting text to lowercase for validation and checking wheather the input file is input is or not
            if (path[LenPath:LenPath-4:-1].lower() != "xcod" and path[LenPath:LenPath-3:-1].lower() != "cod"):
                mg.showerror("File Selection Error",
                             "The file you selected is not a word file.")
                return
            entry_1.delete(0, END)
            entry_1.insert(0, path)
            canvas.itemconfig(
                chanagable, text=f"Question Found: {len(InDoc.paragraphs)//5}")
            # moves the cursor to right most part
            entry_1.xview_moveto(1)

        except Exception as e:
            print(e)
            mg.showerror("Error", "Input File is not selected.")
            entry_1.insert(0, "")
    else:
        path = filedialog.askdirectory()
        outPathSendable = path
        # deletes what's already their
        entry_2.delete(0, END)
        entry_2.insert(0, path)
        entry_2.xview_moveto(1)

# this function randomizes the option in question set


def optionRandomizer(OutDoc, paraNum):
    '''This function randomizes the option ie changes the order or option so that they won't be same'''
    # creating a random list in range 1-4
    default_list = sample(range(1, 5), 4)
    # since no of option is always 4
    for index, val in enumerate(default_list):
        # text to be appended in OutDoc
        reqText = f"{letters[index]}) {InDoc.paragraphs[paraNum+val].text}"
        OutDoc.add_paragraph(reqText)


# -----------------------------------------------------------------
# function which does the main processing

def PROCESSOR(*args):
    ques_pos_list = None
    """
        Basic Parameters Structure:
        0 - input file
        1-output file
        2-no of required question
        3-no of papers required
    """
    

 # Getting no of paragraphs
    global noPara
    noPara = len(InDoc.paragraphs)
    if any(arg == "" or arg == 0 for arg in args):
        mg.showerror("Text Field Blank Error",
                     "Required Information must be provided.")
        return
    if args[2] > (noPara//5):
        mg.showerror("Question Deficit Error",
                     "Question deficiency in Input file")
        return

    # actual len of Paragraphs
    actNoPara = (noPara//5)*5
    # papNo -> No of paper required
    for papNo in range(args[3]):
        # creates new instances which creates new file
        OutDoc = Document()
        # list which acts as a template for question fetching
        ques_pos_list = sample(range(0, actNoPara, 5), args[2])
        for counter, ranNo in enumerate(ques_pos_list):
            # ranNo is the random number
            # Getting text from input file
            paraCode = InDoc.paragraphs[ranNo]
            InpQues = paraCode.text
            # copying that text into new file
            OutDoc.add_paragraph(f"{counter+1}) {InpQues}")
            # function to randomize options
            optionRandomizer(OutDoc, ranNo)
            # saves every new file as in instances
        OutDoc.save(path.join(outPathSendable, f"Doc{papNo}.doc"))
    
    mg.showinfo("Completion of Task","Successfully Created File in"+outPathSendable)
        

# creates a new window
window = Tk()

window.title("DeQuestify")
# no_of question required
NO_QUESTION = IntVar()
# no of paper required
NO_PAPER_REQUIRED = IntVar()
# sets geometry of window
window.geometry(f"1000x{height-90}+{(width//2)-500}+5")
window.configure(bg="#363740")


canvas = Canvas(
    window,
    bg="#363740",
    height=620,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    195.0,
    15.0,
    794.0,
    658.0,
    fill="#FFFFFF",
    outline="")

# Generate Button
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: PROCESSOR(
        inPathSendableObj, outPathSendable, NO_QUESTION.get(), NO_PAPER_REQUIRED.get()),
    relief="flat"
)
button_1.place(
    x=437.0,
    y=555.0,
    width=126.0,
    height=48.0
)
# //////////////////////////////////////////////////////
# entry 1 -> input file directory Objective
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    348.0,
    311.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FCFDFE",
    fg="#000716",
    highlightthickness=0,

)
entry_1.place(
    x=247.0,
    y=253.0,
    width=150.0,
    height=35.0
)
entry_1.insert(0, inPathSendableObj)
entry_1.xview_moveto(1)

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
    x=420, y=259,
    width=24,
    height=22)

canvas.create_text(
    239.0,
    265.0,
    anchor="nw",
    text="INPUT DIRECTORY (OBJECTIVE)",
    fill="#565863",
    font=("Mulish Bold", 12 * -1)
)

# entry 3 -> input file directory for Subjective Question
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_3 = canvas.create_image(
    348.0,
    311.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FCFDFE",
    fg="#000716",
    highlightthickness=0,

)
entry_3.place(
    x=247.0,
    y=293.0,
    width=150.0,
    height=35.0
)
entry_3.insert(0, inPathSendableObj)
entry_3.xview_moveto(1)



# entry_2 -> output directory
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    348.0,
    413.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FCFDFE",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=247.0,
    y=395.0,
    width=150.0,
    height=35.0
)
entry_2.insert(0, outPathSendable)
entry_2.xview_moveto(1)

path_picker_img2 = PhotoImage(file=ASSETS_PATH / "path_picker.png")
path_picker_button2 = Button(
    image=path_picker_img2,
    text='',
    compound='center',
    fg='white',
    borderwidth=0,
    highlightthickness=0,
    # executes when button is clicked
    command=lambda: pathSelect(2),
    relief='flat')
path_picker_button2.place(
    x=420, y=400,
    width=24,
    height=22)
# /////////////////////////////////////////////////////////

# entry_3->
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    628.0,
    312.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FCFDFE",
    fg="#000716",
    highlightthickness=0,
    textvariable=NO_QUESTION
)
entry_3.place(
    x=527.0,
    y=295.0,
    width=202.0,
    height=35.0
)

canvas.create_text(
    239.0,
    370.0,
    anchor="nw",
    text="OUTPUT DIRECTORY",
    fill="#44454D",
    font=("Mulish Bold", 12 * -1)
)

canvas.create_text(
    519.0,
    265.0,
    anchor="nw",
    text="REQUIRED QUESTIONS",
    fill="#44454C",
    font=("Mulish Bold", 12 * -1)
)
# canvas.create_text(
#     528.0,
#     100.0,
#     anchor="nw",
#     text="No of papers to be generated",
#     fill="#4A4F6C",
#     font=("Muli Regular", 14 * -1)
# )
# canvas.create_text(
#     28.0,
#     403.0,
#     anchor="nw",
#     text="File Path Goes Here",
#     fill="#4A4F6C",
#     font=("Muli Regular", 14 * -1)
# )

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    628.0,
    413.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FCFDFE",
    fg="#000716",
    highlightthickness=0,
    textvariable=NO_PAPER_REQUIRED
)
entry_4.place(
    x=527.0,
    y=395.0,
    width=202.0,
    height=35.0
)

canvas.create_text(
    519.0,
    370.0,
    anchor="nw",
    text="No of papers",
    fill="#44454D",
    font=("Mulish Bold", 12 * -1)
)


# Logo
canvas.create_text(
    288.0,
    80.0,
    anchor="nw",
    text="DeQuestify",
    fill="#A4A6B3",
    font=("Mulish Bold", 19 * -1)
)
# Image for logo of dequestify
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    258.0,
    90.0,
    image=image_image_1
)

# Admin Access Text--
canvas.create_text(
    410.0,
    124.0,
    anchor="nw",
    text="Admin Access",
    fill="#252733",
    font=("Mulish Bold", 24 * -1)
)
# Question Found Box-------
canvas.create_rectangle(
    407.0,
    169.0,
    575.0,
    209.0,
    fill="#00B2FF",
    outline="")
# Question found Text
chanagable = canvas.create_text(
    427.0,
    178.0,
    tags="notext",
    anchor="nw",
    text=f"Question Found :{len(InDoc.paragraphs)//5}",
    fill="#FFFFFF",
    font=("Muli SemiBold", 16 * -1)
)

window.resizable(False, False)
window.mainloop()
