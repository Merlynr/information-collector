# import thread
from socket import *
from tkinter import *
from tkinter import ttk

import hashlib
import time

import json, hashlib, sys
import gevent
from gevent import monkey

monkey.patch_all()
from gevent.queue import Queue

import threading

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
            print(zurl)
            print(response)
            if response.status_code == 200:
                res.append(zurl + "\n")
                huanhang = "\n"
                list = huanhang.join(res)
                txt = list

    text.insert('insert', txt)
    print("扫描完成")


def fun2(self, url, portStart, portEnd):
    '''
    通过命令行查询开放的端口再演示
    netstat -a -n
    Args:
        self:
        url:
        portStart:
        portEnd:

    Returns:

    '''
    self.Label1 = Label(self, text='开放的端口号 ：').grid(row=2, column=0)

    text = Text(self, height=45)
    text.grid(row=4, column=1, columnspan=49)
    txt = "无端口开放"

    host = url.get()
    target_ip = gethostbyname(host)

    opened_ports = []

    for port in range(int(portStart.get()), int(portEnd.get())):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(port)
            opened_ports.append(port)
            txt = opened_ports

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
        txt = "注册商为：" + res.xpath('string(//div[@class="block ball"]/span[1])') + "\n"
        txt = txt + '联系邮箱为：' + res.xpath('string(//div[@class="fr WhLeList-right block ball lh24"]/span[1])') + "\n"
        txt = txt + '创建时间为：' + res.xpath('string(//div[@class="fr WhLeList-right"]/span[1])') + "\n"
        txt = txt + '联系电话为：' + res.xpath('string(//ul[@id="sh_info"]/li[4]/div[2]/span[1])') + "\n"
        txt = txt + '过期时间为：' + res.xpath('string(//ul[@id="sh_info"]/li[6]/div[2]/span[1])') + "\n"
        txt = txt + '域名服务器为：' + res.xpath('string(//ul[@id="sh_info"]/li[7]/div[2]/span[1])') + "\n"
        txt = txt + '查询完毕'
    else:
        txt = "查询失败"

    text.insert('insert', txt)

def fun5(self,url,uName,type):
    self.Label1 = Label(self, text='RESULT ：').grid(row=2, column=0)

    text = Text(self, height=45)
    text.grid(row=4, column=1, columnspan=49)
    txt = "该链接无效"
    a=url.get()
    b=a[:-1]
    URL=b.strip("/")

    uName=uName.get()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        print('查询成功！')
        if (type.get() == 'post'):
            f = open("D:\WorkSpace\Work\college\zhouhaoran\information-collector\data\mm\\test.txt", 'r')
            lines = f.readlines()
            i = 0
            res=[]
            for line in lines:
                paylode = {uName: line.replace("\n","")}
                g = requests.post(URL, data=paylode)
                i=i+1
                data={
                    'index':i,
                    'password':line.replace("\n",""),
                    'res':len(g.content.decode())
                }
                res.append(data)
                print(data)
            f.close()
            res.sort(key=func6)
            resx=str(res)
            text.insert('insert', resx.replace('}, {', '\n'))
        if (type.get() == 'get'):
            f = open("D:\WorkSpace\Work\college\zhouhaoran\information-collector\data\mm\weakly.txt", 'r')
            lines = f.readlines()
            i = 0
            res=[]
            for line in lines:
                paylode = {uName: line.replace("\n", "")}
                g = requests.get(URL, data=paylode)
                i = i + 1
                data = {
                    'index': i,
                    'password': line.replace("\n", ""),
                    'res': len(g.content.decode())
                }
                res.append(data)
                print(data)
            f.close()
            res.sort(key=func6)
            resx = str(res)
            text.insert('insert', resx.replace('}, {', '\n'))
    else:
        text.insert('insert', "无效URL")

def func6(elem):
    return elem['res']


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
        self.Label = Label(self, text='端口扫描:').grid(row=1, column=0, padx=20, pady=50)
        value = StringVar()
        url = Entry(self, width=20, textvariable=value)
        url.grid(row=1, column=1, padx=0, pady=0)
        # port1 = StringVar()
        # port2 = StringVar()
        # portStart = Entry(self, width=5, textvariable=port1).grid(row=1, column=3)
        # portEnd = Entry(self, width=5, textvariable=port2).grid(row=1, column=4)
        port1 = StringVar()
        start = Entry(self, width=5, textvariable=port1)
        start.grid(row=1, column=3, padx=0, pady=0)
        port2 = StringVar()
        end = Entry(self, width=5, textvariable=port2)
        end.grid(row=1, column=4, padx=0, pady=0)
        self.Button = Button(self, text='扫描', width=15, command=lambda: fun2(self, url, start, end)).grid(row=1,
                                                                                                                  column=5,
                                                                                                                  sticky=W,
                                                                                                                  padx=10,
                                                                                                                  pady=5)
CMS="暂无数据"

class gwhatweb(object):
    def __init__(self, url):
        self.tasks = Queue()
        self.url = url.get().rstrip("/")
        fp = open('D:\\WorkSpace\\Work\\college\\zhouhaoran\\information-collector\\data\\resource\\data.json',"r", encoding='UTF-8')
        webdata = json.load(fp, encoding="utf-8")
        for i in webdata:
            self.tasks.put(i)
        fp.close()
        global CMS
        CMS="webdata total:%d" % len(webdata)+"\n"
        print("webdata total:%d" % len(webdata))
        self.whatweb(1000)

    def fun3(self,url):
        global CMS
        self.tasks = Queue()
        self.url = url.get().rstrip("/")
        fp = open('D:\\WorkSpace\\Work\\college\\zhouhaoran\\information-collector\\data\\resource\\data.json', "r",
                  encoding='UTF-8')
        webdata = json.load(fp, encoding="utf-8")
        for i in webdata:
            self.tasks.put(i)
        fp.close()
        print("webdata total:%d" % len(webdata))
        self.whatweb(1000)

    def _GetMd5(self, body):
        m2 = hashlib.md5()
        m2.update(body.encode("utf8"))
        return m2.hexdigest()

    def _clearQueue(self):
        while not self.tasks.empty():
            self.tasks.get()

    def _worker(self):
        global CMS
        data = self.tasks.get()
        test_url = self.url + data["url"]
        rtext = ''
        try:
            r = requests.get(test_url, timeout=10)
            if (r.status_code != 200):
                return
            rtext = r.text
            if rtext is None:
                return
        except:
            rtext = ''

        if data["re"]:
            if (rtext.find(data["re"]) != -1):
                result = data["name"]
                print("CMS:%s Judge:%s re:%s" % (result, test_url, data["re"]))
                CMS = CMS + "CMS:%s Judge:%s re:%s" % (result, test_url, data["re"])+"\n"
                self._clearQueue()
                return True
        else:
            md5 = self._GetMd5(rtext)
            if (md5 == data["md5"]):
                result = data["name"]
                print("CMS:%s Judge:%s md5:%s" % (result, test_url, data["md5"]))
                CMS = CMS + "CMS:%s Judge:%s md5:%s" % (result, test_url, data["md5"])+"\n"

                self._clearQueue()
                return True

    def _boss(self):
        while not self.tasks.empty():
            self._worker()

    def whatweb(self, maxsize=100):
        global CMS
        start = time.perf_counter()
        allr = [gevent.spawn(self._boss) for i in range(maxsize)]
        gevent.joinall(allr)
        end = time.perf_counter()
        CMS = CMS + "cost: %f s" % (end - start) + "\n"
        print("cost: %f s" % (end - start))

def Refresher():
    Draw()


class findOutNetworkType(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.Label = Label(self, text='请输入CMS域名:').grid(row=1, column=0, padx=20, pady=50)
        value = StringVar()
        url = Entry(self, width=20, textvariable=value)
        url.grid(row=1, column=1, padx=0, pady=0)
        self.Button = Button(self, text='查询CMS类型', width=15, command=lambda: gwhatweb(url)).grid(row=1, column=3,
                                                                                                    sticky=W,
                                                                                                    padx=10, pady=5)

        self.Label1 = Label(self, text='RESULT ：').grid(row=2, column=0)
        text = Text(self, height=45)
        text.grid(row=4, column=1, columnspan=49)
        # TODO 轮询器实时渲染
        # TODO 轮询器实时渲染
        # threading.Timer(1).start()
        text.insert('insert',CMS)
        def insertText():
            text.delete('1.0','end')
            text.insert('insert',CMS)
            text.after(2000,insertText)

        text.after(2000,insertText)



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
        self.Label = Label(self, text='请输入域名:').grid(row=1, column=0, padx=20, pady=50)
        value = StringVar()
        url = Entry(self, textvariable=value)
        url.grid(row=1, column=1, padx=0, pady=0)
        self.Label = Label(self, text='请输入用户名:').grid(row=1, column=2, padx=20, pady=50)
        value2 = StringVar()
        uName = Entry(self, textvariable=value2)
        uName.grid(row=1, column=3, padx=0, pady=0)
        type = StringVar()
        numberChosen = ttk.Combobox(self, width=12, textvariable=type)
        numberChosen['values'] = ('post', 'get')  # 设置下拉列表的值
        numberChosen.grid(column=4, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
        numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        self.Button = Button(self, text='破解', width=10, command=lambda: fun5(self, url,uName, type)).grid(row=1, column=5,
                                                                                                    sticky=W,
                                                                                                    padx=10, pady=5)

LOG_LINE_NUM = 0
class test(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.init_data_label = Label(self, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self, text="日志")
        self.log_label.grid(row=12, column=0)
        # 文本框
        self.init_data_Text = Text(self, width=67, height=35)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self, width=70, height=49)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 按钮
        self.str_trans_to_md5_button = Button(self, text="字符串转MD5", bg="lightblue", width=10,
                                              command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)

    # # 功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        # print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                # print(myMd5_Digest)
                # 输出到界面
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)

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
