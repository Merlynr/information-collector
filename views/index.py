from tkinter import *
from tkinter import ttk

import requests
from lxml import etree

from data.subdomain import asp
from data.subdomain import brf
from data.subdomain import cfm
from data.subdomain import cgi
from data.subdomain import js
from data.subdomain import php


class Controller(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.pageFirst = searchChildNetWork(self)
        self.pageFirst.grid(row=0, column=1, sticky='nsew')
        self.pageSecond = searchOpenPort(self)
        self.pageSecond.grid(row=0, column=1, sticky='nsew')
        self.pageThird = findOutNetworkType(self)
        self.pageThird.grid(row=0, column=1, sticky='nsew')
        self.pageFourth = nwtWorkTool(self)
        self.pageFourth.grid(row=0, column=1, sticky='nsew')
        self.pageFifth = baoliPojie(self)
        self.pageFifth.grid(row=0, column=1, sticky='nsew')
        self.pageSixth = test(self)
        self.pageSixth.grid(row=0, column=1, sticky='nsew')
        self.pageIndex = index(self)
        self.pageIndex.grid(row=0, column=1, sticky='nsew')
        self.menu = testOverlap(self)
        self.menu.grid(row=0, column=0, sticky='nsew')

        self.menu.tkraise()  # show the testOverlap Frame now


class testOverlap(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.topButtons()

    def topButtons(self):
        self.pageFirst = Button(self, text="查询子域名", background="WHITE", height=2, width=22,
                                command=self.master.pageFirst.tkraise)
        self.pageFirst.grid(row=0, column=0)
        self.pageSecond = Button(self, text="查询开放端口", background="WHITE", height=2, width=22,
                                 command=self.master.pageSecond.tkraise)
        self.pageSecond.grid(row=1, column=0)
        self.pageThird = Button(self, text="判断网站类型", background="WHITE", height=2, width=22,
                                command=self.master.pageThird.tkraise)
        self.pageThird.grid(row=2, column=0)
        self.pageFourth = Button(self, text="站长查询工具", background="WHITE", height=2, width=22,
                                 command=self.master.pageFourth.tkraise)
        self.pageFourth.grid(row=3, column=0)
        self.pageFifth = Button(self, text="暴力破解", background="WHITE", height=2, width=22,
                                command=self.master.pageFifth.tkraise)
        self.pageFifth.grid(row=4, column=0)
        self.pageSixth = Button(self, text="MD5加解密", background="WHITE", height=2, width=22,
                                command=self.master.pageSixth.tkraise)
        self.pageSixth.grid(row=5, column=0)


def fun1(self, url, type):
    '''
    查询子域名
    Args:
        url:

    Returns:

    '''
    self.Label1 = Label(self, text='RESULT ：').grid(row=2, column=0)

    # value1 = StringVar()
    # self.Label1 = Label(self, textvariable=value1, justify='left').grid(row=3, column=1)
    # value1.set(type.get())

    text = Text(self, height=45)
    text.grid(row=4, column=1, columnspan=49)
    txt = "无结果"
    types = {
        'asp': asp, 'brf': brf, 'cfm': cfm, 'cgi': cgi, 'js': js, 'php': php
    }

    if (type.get() == "asp"):
        res = []
        for zurl in asp.asp:
            zurl = url.get() + "/" + zurl
            response = requests.get(zurl)
            print(zurl)
            print(response)
            if response.status_code == 200:
                res.append(zurl + "\n")
                huanhang = "\n"
                list = huanhang.join(res)
                txt = list

    if (type.get() == "brf"):
        res = []
        for zurl in brf.brf:
            zurl = url.get() + "/" + zurl
            response = requests.get(zurl)
            print(zurl)
            print(response)
            if response.status_code == 200:
                res.append(zurl + "\n")
                huanhang = "\n"
                list = huanhang.join(res)
                txt = list

    if (type.get() == "cfm"):
        res = []
        for zurl in cfm.cfm:
            zurl = url.get() + "/" + zurl
            response = requests.get(zurl)
            print(zurl)
            print(response)
            if response.status_code == 200:
                res.append(zurl + "\n")
                huanhang = "\n"
                list = huanhang.join(res)
                txt = list

    if (type.get() == "cgi"):
        res = []
        for zurl in cgi.cgi:
            zurl = url.get() + "/" + zurl
            response = requests.get(zurl)
            print(zurl)
            print(response)
            if response.status_code == 200:
                res.append(zurl + "\n")
                huanhang = "\n"
                list = huanhang.join(res)
                txt = list

    if (type.get() == "js"):
        res = []
        for zurl in js.js:
            zurl = url.get() + "/" + zurl
            response = requests.get(zurl)
            print(zurl)
            print(response)
            if response.status_code == 200:
                res.append(zurl + "\n")
                huanhang = "\n"
                list = huanhang.join(res)
                txt = list

    if (type.get() == "php"):
        res = []
        for zurl in php.php:
            zurl = url.get() + "/" + zurl
            response = requests.get(zurl)
            if response.status_code == 200:
                res.append(zurl + "\n")
                huanhang = "\n"
                list = huanhang.join(res)
                txt = list

    text.insert('insert', txt)


def fun4(self, url):
    self.Label1 = Label(self, text='RESULT ：').grid(row=2, column=0)

    text = Text(self, height=45)
    text.grid(row=4, column=1, columnspan=49)
    txt = "无结果"

    url = 'http://whois.chinaz.com/' + url.get()

    response = requests.get(url)

    if response.status_code == 200:
        print(url)
        res = etree.HTML(response.text)
        txt="注册商为："+res.xpath('string(//div[@class="block ball"]/span[1])')+"\n"
        txt=txt+'联系邮箱为：' +res.xpath('string(//div[@class="fr WhLeList-right block ball lh24"]/span[1])')+"\n"
        txt = txt + '创建时间为：' + res.xpath('string(//div[@class="fr WhLeList-right"]/span[1])') + "\n"
        txt = txt + '联系电话为：' + res.xpath('string(//ul[@id="sh_info"]/li[4]/div[2]/span[1])') + "\n"
        txt = txt + '过期时间为：' + res.xpath('string(//ul[@id="sh_info"]/li[6]/div[2]/span[1])') + "\n"
        txt = txt + '域名服务器为：' + res.xpath('string(//ul[@id="sh_info"]/li[7]/div[2]/span[1])') + "\n"
        txt = txt + '查询完毕'
    else:
        txt = "查询失败"

    text.insert('insert', txt)


class searchChildNetWork(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        # self.Label = Label(self, text="查询子域名", height=50, width=102, background="#B4D5FC")
        self.Label = Label(self, text='请输入域名:').grid(row=1, column=0, padx=20, pady=50)
        value = StringVar()
        url = Entry(self, textvariable=value)
        url.grid(row=1, column=1, padx=0, pady=0)
        type = StringVar()
        numberChosen = ttk.Combobox(self, width=12, textvariable=type)
        numberChosen['values'] = ('asp', 'brf', 'cfm', 'cgi', 'js', 'php')  # 设置下拉列表的值
        numberChosen.grid(column=2, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        self.Button = Button(self, text='获得', width=10, command=lambda: fun1(self, url, type)).grid(row=1, column=3,
                                                                                                    sticky=W,
                                                                                                    padx=10, pady=5)


class searchOpenPort(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.Label = Label(self, text="查询开放端口", height=50, width=102, background="#B4D5FC")
        self.Label.grid()


class findOutNetworkType(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.Label = Label(self, text="判断网站类型", height=50, width=102, background="#B4D5FC")
        self.Label.grid()


class nwtWorkTool(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.Label = Label(self, text='请输入域名:').grid(row=1, column=0, padx=20, pady=50)
        value = StringVar()
        url = Entry(self, width=20, textvariable=value)
        url.grid(row=1, column=1, padx=0, pady=0)
        self.Button = Button(self, text='通过站长工具查询', width=15, command=lambda: fun4(self, url)).grid(row=1, column=3,
                                                                                                    sticky=W,
                                                                                                    padx=10, pady=5)


class baoliPojie(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.Label = Label(self, text="暴力破解", height=50, width=102, background="#B4D5FC")
        self.Label.grid()


class test(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.Label = Label(self, text="MD5加解密", height=50, width=102, background="#B4D5FC")
        self.Label.grid()


class index(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        # photo = PhotoImage(file='../data/resource/images/index_photo.gif')
        # self.Label = Label(self, height=50, width=102, image=photo)
        self.Label = Label(self, text="首页带设计", height=50, width=102, background="#B4D5FC")
        self.Label.grid()


def main():
    root = Tk()
    root.title("信息收集扫描器")
    root.geometry('900x780')
    app = Controller(root)
    app.pack(expand=True, fill=BOTH)
    root.mainloop()


if __name__ == '__main__':
    main()
