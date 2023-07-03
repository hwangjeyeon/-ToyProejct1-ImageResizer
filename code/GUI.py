import tkinter
import tkinter.font

import Info
import func

window = tkinter.Tk()
window.title("Image Resizer")
window.geometry("260x240")
window.resizable(False, False)

font1 = tkinter.font.Font(family="맑은 고딕", size=13)

label1 = tkinter.Label(window, text="높이: ", font=font1)
label2 = tkinter.Label(window, text="넓이: ", font=font1)
label3 = tkinter.Label(window, text="파일: ", font=font1)


entry1 = tkinter.Entry(window)
entry2 = tkinter.Entry(window)
entry3 = tkinter.Entry(window, state="readonly")

button1 = tkinter.Button(window, width=15, text="완료", relief="raised", overrelief="raised")


message1 = tkinter.Message(window, text="저장되었습니다", width=100)
message2 = tkinter.Message(window, text="저장되었습니다", width=100)
message3 = tkinter.Message(window, text="저장되었습니다", width=100)


label1.place(x=15,y=30)
label2.place(x=15,y=80)
label3.place(x=15,y=130)
entry1.place(x=80, y=35)
entry2.place(x=80, y=85)
entry3.place(x=80, y=135)
button1.place(x=100, y=180)



entry1.bind("<Return>",func.EntryCalc1)
entry2.bind("<Return>",func.EntryCalc2)
entry3.bind("<ButtonRelease-1>",func.filesave)
button1.bind("<ButtonRelease-1>",func.buttonclick)

