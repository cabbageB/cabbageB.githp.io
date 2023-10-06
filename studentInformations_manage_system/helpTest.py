import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import random

# root = tk.Tk()
# root.title("frameTest")
# root.geometry("680x340+400+300")
# # 不允许改变窗口大小
# root.resizable(False, False)
# # 在窗体上创建frame组件
# frame = tk.Frame(root)
# frame.place(x=0, y=10, width=650, height=280)
#
# # 在frame容器中创建滚动条
# scrollBar = tk.Scrollbar(frame)
# scrollBar.pack(side=RIGHT, fill=Y)
#
# # 在Frame容器中使用TreeView组件实现表格功能
# # Treeview组件中，6列显示表头，带垂直滚动条
# tree = ttk.Treeview(frame,
#                     columns=('c1', 'c2', 'c3', 'c4', 'c5', 'c6'),
#                     show='headings',
#                     yscrollcommand=scrollBar.set)
#
# # 设置每列宽度和对齐方式
# tree.column('c1', width=70, anchor='center')
# tree.column('c2', width=70, anchor='center')
# tree.column('c3', width=70, anchor='center')
# tree.column('c4', width=140, anchor='center')
# tree.column('c5', width=140, anchor='center')
# tree.column('c6', width=140, anchor='center')
#
# # 设置每列表头标题文本
# tree.heading('c1', text='姓名')
# tree.heading('c2', text='性别')
# tree.heading('c3', text='年龄')
# tree.heading('c4', text='学号')
# tree.heading('c5', text='电话')
# tree.heading('c6', text='家庭地址')
#
# # 左对齐，纵向填充
# tree.pack(side=LEFT, fill=Y)
#
# # Treeview组件与垂直滚动条结合
# scrollBar.config(command=tree.yview)
#
#
# # 定义并绑定Treeview组件的鼠标左键双击事件
# def treeviewClick(event):
#     selectedItem = tree.selection()[0]
#     name = tree.item(selectedItem, 'values')[0]
#     print(tree.item(selectedItem, 'values'))
#     messagebox.showinfo('报告', "你的选择是\n" + name)
#
#
# tree.bind('<Double-1>', treeviewClick)
#
#
# # 插入随机数据的按钮
# def onbtnInsertClick():
#     values = [str(random.randrange(1000)) for _ in range(6)]
#     tree.insert('', 0, values=values)
#
#
# btnInsert = tk.Button(root,
#                       text='插入随机数据',
#                       command=onbtnInsertClick)
# btnInsert.place(x=80, y=310, width=120, height=20)
#
#
# # 删除选中项的按钮
# def onbtnDeleteCLick():
#     if not tree.selection():
#         messagebox.showerror('抱歉', "你还没有选择，不能删除")
#         return
#     for item in tree.selection():
#         tree.delete(item)
#
#
# btnDelete = tk.Button(root,
#                       text="删除选中项",
#                       command=onbtnDeleteCLick)
# btnDelete.place(x=220, y=310, width=120, height=20)
#
# # 插入演示数据
# for i in range(20):
#     tree.insert('', i, values=[str(i)] * 6)
#
# # 运行程序，启动事件循环
# root.mainloop()

# stu_tuple = ('张三', '男', 32,  '121341313', '1762371725', '重庆市')
# print(f"INSERT INTO test VALUES('%s','%s',%d,'%s','%s','%s')" % stu_tuple)

# def add_student(self):
#     # 创建新窗口
#     self.add_window = tk.Toplevel(self.master)
#     self.add_window.title("新增学生")
#     self.add_window.geometry("300x200")
#
#     # 创建学生信息输入框和确定按钮等组件
#     label_name = tk.Label(self.add_window, text="姓名:")
#     label_name.pack()
#     entry_name = tk.Entry(self.add_window)
#     entry_name.pack()
#
#     label_gender = tk.Label(self.add_window, text="性别:")
#     label_gender.pack()
#     entry_gender = tk.Entry(self.add_window)
#     entry_gender.pack()
#
#     label_age = tk.Label(self.add_window, text="年龄:")
#     label_age.pack()
#     entry_age = tk.Entry(self.add_window)
#     entry_age.pack()
#
#     label_student_id = tk.Label(self.add_window, text="学号:")
#     label_student_id.pack()
#     entry_student_id = tk.Entry(self.add_window)
#     entry_student_id.pack()
#
#     label_phone = tk.Label(self.add_window, text="电话:")
#     label_phone.pack()
#     entry_phone = tk.Entry(self.add_window)
#     entry_phone.pack()
#
#     label_address = tk.Label(self.add_window, text="家庭地址:")
#     label_address.pack()
#     entry_address = tk.Entry(self.add_window)
#     entry_address.pack()
#
#     btn_confirm = tk.Button(self.add_window, text="确定", command=lambda: self.insert_student(entry_name.get(), entry_gender.get(), entry_age.get(), entry_student_id.get(), entry_phone.get(), entry_address.get()))
#     btn_confirm.pack()

# def add_student():
#     # 创建新窗口
#     root = tk.Tk()
#     add_window = tk.Toplevel(root)
#     add_window.title("新增学生")
#     add_window.geometry("300x200")
#
#     # 创建学生信息输入框和确定按钮等组件
#     label_name = tk.Label(add_window, text="姓名:", bg='pink')
#     label_name.grid(column=1, row=1)
#     entry_name = tk.Entry(add_window, width=30, bg='white', fg='black')
#     entry_name.grid(column=2, row=1)
#
#     label_gender = tk.Label(add_window, text="性别:", bg='pink')
#     label_gender.grid(column=1, row=2)
#     entry_gender = tk.Entry(add_window, width=30, bg='white', fg='black')
#     entry_gender.grid(column=2, row=2)
#
#     label_age = tk.Label(add_window, text="年龄:", bg='pink')
#     label_age.grid(column=1, row=3)
#     entry_age = tk.Entry(add_window, width=30, bg='white', fg='black')
#     entry_age.grid(column=2, row=3)
#
#     label_student_id = tk.Label(add_window, text="学号:", bg='pink')
#     label_student_id.grid(column=1, row=4)
#     entry_student_id = tk.Entry(add_window, width=30, bg='white', fg='black')
#     entry_student_id.grid(column=2, row=4)
#
#     label_phone = tk.Label(add_window, text="电话:", bg='pink')
#     label_phone.grid(column=1, row=5)
#     entry_phone = tk.Entry(add_window, width=30, bg='white', fg='black')
#     entry_phone.grid(column=2, row=5)
#
#     label_address = tk.Label(add_window, text="家庭地址:", bg='pink')
#     label_address.grid(column=1, row=6)
#     entry_address = tk.Entry(add_window, width=30, bg='white', fg='black')
#     entry_address.grid(column=2, row=6)
#
#     btn_confirm = tk.Button(add_window, text="确定", width=20, height=1,
#                             command=lambda: (print(entry_name.get(), entry_gender.get(),
#                                                    entry_age.get(), entry_student_id.get(),
#                                                    entry_phone.get(), entry_address.get()),
#                                              add_window.destroy()))
#     btn_confirm.grid(column=2, row=8)
#
#     root.mainloop()
#
#
# add_student()

# print(type((1, 2, 3, 4)))
stu_tuple = ('张三', '男', 18, '163712631', '2136187371', '北京')
name = '赵四'
print(f"UPDATE test SET `姓名` = '{stu_tuple[0]}',"
      f"`性别` = '{stu_tuple[1]}',"
      f"`年龄` = {stu_tuple[2]},"
      f"`学号` = '{stu_tuple[3]}',"
      f"`电话` = '{stu_tuple[4]}',"
      f"`家庭地址` = '{stu_tuple[5]}'"
      f" WHERE `姓名` = '{name}'")

