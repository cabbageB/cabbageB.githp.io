from tkinter import *
from tkinter import messagebox

import informationsView


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.createWidget()

    def Login(self):
        user_name = self.var1.get()
        password = self.var2.get()
        if user_name != "12212990903" or password != "20040923":
            messagebox.showerror(title="error", message="账号或密码错误")
        else:
            self.master.destroy()
            self.openStudentInformation()

    def exit(self):
        self.master.destroy()

    def createWidget(self):
        self.label1 = Label(self.master, text="学生信息管理系统", font="Arial", width=16, height=2, bg="white",
                            fg="red")
        self.label1.place(x=180, y=0)
        self.user_name_label = Label(self.master, text="账号:", width=4, height=2, font="微软雅黑")
        self.user_name_label.place(x=100, y=60)
        self.password_label = Label(self.master, text="密码:", width=4, height=2, font="微软雅黑")
        self.password_label.place(x=100, y=110)
        self.var1 = StringVar()
        self.user_name_entry = Entry(self.master, width=25, textvariable=self.var1, bg="white", fg="black",
                                     font="Calibri")
        self.var2 = StringVar()
        self.password_entry = Entry(self.master, width=25, textvariable=self.var2, bg="white", fg="black", show="*",
                                    font="Calibri")
        self.user_name_entry.place(x=150, y=77)
        self.password_entry.place(x=150, y=127)
        self.login_button = Button(self.master, text="登录", font="黑体", bg="white", fg="black", width=5, height=1,
                                   command=self.Login)
        self.login_button.place(x=160, y=190)
        self.exit_button = Button(self.master, text="退出", font="黑体", bg='white', fg='black', width=5, height=1
                                  , command=exit)
        self.exit_button.place(x=320, y=190)

    def openStudentInformation(self):
        informationsView.showInfo()


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x300+500+300")
    root.title("奋斗")
    app = Application(master=root)
    app.mainloop()
