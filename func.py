import os.path
import threading
import cv2
import GUI
import tkinter
import Info
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import numpy as np




def message1_destroyer():
    #print("hi")
    #print(threading.active_count())
    Info.cnt1 = 0
    if threading.activeCount() <= 2:

        if Info.cnt2 == 0 and Info.cnt3 == 0:
            if GUI.message2:
                GUI.message2.destroy()

            if GUI.message3:
                GUI.message3.destroy()

            GUI.message1.destroy()
            GUI.window.geometry("260x240")

    else:
        pass


def message2_destroyer():
    Info.cnt2 = 0
    if threading.activeCount() <= 2:

        if Info.cnt1 == 0 and Info.cnt3 == 0:
            if GUI.message1:
                GUI.message1.destroy()

            if GUI.message3:
                GUI.message3.destroy()

            GUI.message2.destroy()
            GUI.window.geometry("260x240")

    else:
        pass
def message3_destroyer():
    Info.cnt3 = 0
    if threading.activeCount() <= 2:

        if Info.cnt1 == 0 and Info.cnt2 == 0:
            if GUI.message1:
                GUI.message1.destroy()

            if GUI.message2:
                GUI.message2.destroy()

            GUI.message3.destroy()
            GUI.window.geometry("260x240")

    else:
        pass

def EntryCalc1(event):
    try:
        Info.height = int(GUI.entry1.get())
        if Info.height > 0:
            Info.cnt1 += 1
            if Info.cnt1 == 1:
                GUI.message1 = tkinter.Message(GUI.window, text="저장되었습니다", width=100)
                GUI.window.geometry("320x240")
                GUI.message1.place(x=220, y=35)
                timer = threading.Timer(5.0, message1_destroyer)
                timer.start()
        else:
            tkinter.messagebox.showerror("오류", "양수를 입력하세요")
    except ValueError:
        tkinter.messagebox.showerror("오류", "숫자를 입력하세요")




def EntryCalc2(event):
    try:
        Info.width = int(GUI.entry2.get())
        if Info.width > 0:
            Info.cnt2 += 1
            if Info.cnt2 == 1:
                GUI.message2 = tkinter.Message(GUI.window, text="저장되었습니다", width=100)
                GUI.window.geometry("320x240")
                GUI.message2.place(x=220, y=85)
                timer = threading.Timer(5.0, message2_destroyer)
                timer.start()
        else:
            tkinter.messagebox.showerror("오류", "양수를 입력하세요")
    except ValueError:
        tkinter.messagebox.showerror("오류", "숫자를 입력하세요")



def filesave(event):
    Info.image = tkinter.filedialog.askopenfilename(initialdir='./png',title='파일선택', filetypes=(('png files','*.png'),('jpg files','*.jpg'),('all files','*.*')))
    GUI.entry3.insert(0,Info.image)
    if not len(Info.image) <= 0:
        Info.cnt3 += 1
        if Info.cnt3 == 1:
            GUI.message3 = tkinter.Message(GUI.window, text="저장되었습니다", width=100)
            GUI.window.geometry("320x240")
            GUI.message3.place(x=220, y=135)
            timer = threading.Timer(5.0, message3_destroyer)
            timer.start()

def buttonclick(evnet):

    if Info.height <= 0 or Info.width <= 0 or len(Info.image) <= 0:
        if Info.height <= 0:
               tkinter.messagebox.showerror("오류", "높이 값을 입력하세요")
        elif Info.width <= 0:
            tkinter.messagebox.showerror("오류", "넓이 값을 입력하세요")
        elif len(Info.image) <= 0:
            tkinter.messagebox.showerror("오류", "이미지를 선택하세요")

    else:
        try:
            img_array = np.fromfile(Info.image, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            old_height, old_width, channels = img.shape

            if old_height > Info.height and old_width > Info.width:
                img_resize = cv2.resize(img, dsize=(Info.width, Info.height), interpolation=cv2.INTER_AREA)
            else:
                img_resize = cv2.resize(img, dsize=(Info.width, Info.height), interpolation=cv2.INTER_LANCZOS4)





            ext = os.path.splitext(Info.image)[1]  # 이미지 확장자

            ret, encoded_img = cv2.imencode(ext, img_resize)

            if ret:
                with open(Info.image, mode='w+b') as f:
                    encoded_img.tofile(f)

            tkinter.messagebox.showinfo(title='test',message="저장되었습니다.")

        except IOError:
            tkinter.messagebox.showerror("오류", "입력한 파일은 이미지가 아닙니다.")
