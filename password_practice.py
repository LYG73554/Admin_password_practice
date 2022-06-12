def checkpw():
    if(pw.get() == "admin"):
        msg.set("密碼正確，歡迎登入！")
    else:
        msg.set("密碼錯誤，請重新輸入！")

import tkinter as tk

win = tk.Tk()
win.geometry("500x300")
win.title("單一登入口")
pw = tk.StringVar()
msg = tk.StringVar()

label = tk.Label(win, text = "歡迎，請輸入密碼：")
label.place(x=200,y=50)

entry = tk.Entry(win, textvariable=pw)
entry.place(x=160,y=80)

button = tk.Button(win, text="登入", command=checkpw)
button.place(x=220,y=125)

lblmsg = tk.Label(win, fg="red", textvariable=msg)
lblmsg.place(x=180,y=160)

win.mainloop()