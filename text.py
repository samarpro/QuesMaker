# import firebase_admin
# from firebase_admin import credentials,auth

# cred = credentials.Certificate("E:/QuesMaker/assets/frame0/databs-ea159-firebase-adminsdk-6dt2q-4ca5f78a73.json")
# firebase_admin.initialize_app(cred)
# print(auth.get_user_by_email("bishnuad99@gmail.com"))

import tkinter as tk
from time import sleep

def task():
    # The window will stay open until this function call ends.
    sleep(2) # Replace this with the code you want to run
    root.destroy()

root = tk.Tk()
root.title("Example")

label = tk.Label(root, text="Waiting for task to finish.")
label.pack()

root.after(200, task)
root.mainloop()

print("Main loop is now over and we can do other stuff.")