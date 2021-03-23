#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox  # 要使用messagebox先要导入模块

window = tk.Tk()

window.title('Message!!!')

window.geometry('500x300')  # 这里的乘是小x


def hit_me(type, msg):
    messageType: {
        "success": tkinter.messagebox.show(title='操作成功'),
        "info": tkinter.messagebox.showinfo(title='Hi', message=msg),  # 提示信息对话窗
        "warn": tkinter.messagebox.showwarning(title='Hi', message=msg),  # 提出警告对话窗
        "error": tkinter.messagebox.showerror(title='Hi', message=msg)  # 提出错误对话窗
    }
    return messageType.get(type)

#使用方法
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()

window.mainloop()
