from cam_capture import *
from helper_fun import register_user, login_user
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os


def nav_to_login(window):
    login_frame(window)


def nav_to_register(window):
    register_frame(window)


def captureFace(ent):
    filename = os.getcwd()+'\\temp\\test_img.png'
    res = None
    res = messagebox.askquestion(
        'Click Picture', 'Press Space Bar to click picture and ESC to exit')
    if res == 'yes':
        capture_image_from_cam_into_temp()
        ent.insert(tk.END, filename)
    return True


def captureFace(ent):
    filename = os.getcwd()+'\\temp\\test_img.png'
    res = None
    res = messagebox.askquestion(
        'Click Picture', 'Press Space Bar to click picture and ESC to exit')
    if res == 'yes':
        capture_image_from_cam_into_temp()
        ent.insert(tk.END, filename)
    return True


def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.insert(tk.END, filename)  # add this


def login_frame(destroy_this_win=None):
    if destroy_this_win is not None:
        destroy_this_win.destroy()

    empty_temp_folder()
    root = tk.Tk()
    root.title("SECURE_UR_FILE")
    root.geometry("500x700")  # 300x200

    uname_label = tk.Label(root, text="Username:", font=10)
    uname_label.place(x=10, y=100)

    uname_entry = tk.Entry(root, font=10)
    uname_entry.place(x=150, y=100)

    passwd_label = tk.Label(root, text="Password (4 char):", font=10)
    passwd_label.place(x=10, y=150)

    passwd_entry = tk.Entry(root, show="*", font=10)
    passwd_entry.place(x=200, y=150)

    facepic_message = tk.Label(root, text="Face Pic:", font=10)
    facepic_message.place(x=10, y=200)

    facepic_entry = tk.Entry(root, font=10)
    facepic_entry.place(x=150, y=200)

    facepic_browse_button = tk.Button(
        root, text="Capture", font=10, command=lambda: captureFace(facepic_entry))
    facepic_browse_button.place(x=400, y=190)

    login_button = tk.Button(
        root, text="login", font=10, command=lambda: login_user(window=root,
                                                                username=uname_entry.get(),
                                                                facepic_path=facepic_entry.get(),
                                                                password=passwd_entry.get()))

    login_button.place(x=200, y=320)

    register_nav_message = tk.Label(
        root, text="New user? Register here", font=10)
    register_nav_message.place(x=10, y=450)
    register_nav_button = tk.Button(
        root, text="Go to Register Page", font=10, command=lambda: nav_to_register(window=root,))

    register_nav_button.place(x=250, y=450)

    root.mainloop()


def register_frame(destroy_this_win=None):
    if destroy_this_win is not None:
        destroy_this_win.destroy()

    empty_temp_folder()
    root = tk.Tk()
    root.title("Safe-Storage:Register")
    root.geometry("500x700")  # 300x200

    uname_label = tk.Label(root, text="Username:", font=10)
    uname_label.place(x=10, y=100)

    uname_entry = tk.Entry(root, font=10)
    uname_entry.place(x=150, y=100)

    passwd_label = tk.Label(root, text="Password (4 char):", font=10)
    passwd_label.place(x=10, y=150)

    passwd_entry = tk.Entry(root, show="*", font=10)
    passwd_entry.place(x=200, y=150)

    profilepic_message = tk.Label(root, text="Profile Pic:", font=10)
    profilepic_message.place(x=10, y=200)

    profilepic_entry = tk.Entry(root, font=10)
    profilepic_entry.place(x=150, y=200)

    profilepic_browse_button = tk.Button(
        root, text="Browse", font=10, command=lambda: browsefunc(profilepic_entry))
    profilepic_browse_button.place(x=400, y=190)
    facepic_message = tk.Label(root, text="Face Pic:", font=10)
    facepic_message.place(x=10, y=250)

    facepic_entry = tk.Entry(root, font=10)
    facepic_entry.place(x=150, y=250)

    facepic_browse_button = tk.Button(
        root, text="Capture", font=10, command=lambda: captureFace(facepic_entry))
    facepic_browse_button.place(x=400, y=240)

    register_button = tk.Button(
        root, text="register", font=10, command=lambda: register_user(window=root,
                                                                      username=uname_entry.get(),
                                                                      facepic_path=facepic_entry.get(),
                                                                      password=passwd_entry.get(),
                                                                      propic_path=profilepic_entry.get()))

    register_button.place(x=200, y=320)
    login_nav_message = tk.Label(
        root, text="Already registered? Login here", font=10)
    login_nav_message.place(x=10, y=450)
    login_nav_button = tk.Button(
        root, text="Go to Login Page", font=10, command=lambda: nav_to_login(window=root,))

    login_nav_button.place(x=300, y=450)

    root.mainloop()


login_frame()
