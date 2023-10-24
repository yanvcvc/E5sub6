#!usr/bin/env python
# -*- coding: utf-8 -*-
# author: ***
# date: 2020/06/10
from tkinter import *
import tkinter as tk
import random
import time
from threading import Thread
root = Tk()
root.geometry('620x660')
root.title('摇骰子')
sigpic = PhotoImage(file='signature.png')
shake_cup = PhotoImage(file='touzi/box.png')
crown = PhotoImage(file='touzi/win.png')
readystate = 3
playing = False
used_name = set()
result_dict = dict()
remain = 3
esv_A = StringVar()
esv_B = StringVar()
esv_C = StringVar()
pi_list = list()
for i in range(1, 7):
pi = PhotoImage(file=r'touzi/t%s.png' % i)
pi_list.append(pi)
def set_name(cw, ew, nw):
global readystate
entryV = ew.get()
if entryV:
if entryV in used_name:
default = nw['text']
nw.config(text="名称已存在！")
cw.config(state=tk.DISABLED)
font_shake(nw, default)
cw.config(state=tk.ACTIVE)
else:
used_name.add(entryV)
nw.config(text=entryV)
ew.config(state=tk.DISABLED)
cw.config(state=tk.DISABLED)
readystate -= 1
if readystate == 0:
for i in "ABC":
eval('play_btn_%s.config(state=tk.ACTIVE, text="第一次机会")' % i)
def throw_touzi(pw, rw, nw):
global playing
global remain
if pw['text']=="第一次机会":
playing = True
pbStack.remove(pw)
for widget in pbStack:
widget.config(state=tk.DISABLED)
pw.config(state=tk.DISABLED, text='第二次机会')
elif pw['text']=="第二次机会":
pw.config(state=tk.DISABLED, text='第三次机会')
else:
playing = False
remain -= 1
pw.config(state=tk.DISABLED, text='play')
thread = Thread(target=change_img, args=[pw, rw, nw])
thread.start()
def change_img(pw, rw, nw):
result_number = random.randint(1, 6)
ranum_list = list()
times = 5
while times:
ranum = random.randint(1, 6)
if ranum not in ranum_list:
ranum_list.append(ranum)
times = times - 1
for i in ranum_list:
time.sleep(0.3)
throw_label.config(image=pi_list[i-1])
time.sleep(0.3)
throw_label.config(image=pi_list[result_number-1])
time.sleep(0.5)
if rw['text'] == "结果":
rw['text'] = str(result_number)
else:
rw['text'] = str(rw['text']) + "+%s" % result_number
time.sleep(0.5)
rw['text'] = eval(rw['text'])
if pw['text'] != "play":
pw.config(state=tk.ACTIVE)
if playing == False:
result_dict[nw['text']] = rw['text']
for widget in pbStack:
widget.config(state=tk.ACTIVE)
if not remain:
result_list = sorted(result_dict.items(), reverse=True, key=lambda rt: rt[1])
if result_list[0][1] == result_list[1][1]:
if result_list[1][1] == result_list[2][1]:
throw_winner['text'] = "   平局 <<"
else:
winner = result_list[0][0] + ", " + result_list[1][0]
throw_winner['text'] = "Winner: %s" % winner
else:
winner = result_list[0][0]
throw_winner['text'] = "Winner: %s" % winner
throw_label['image'] = crown
reset_btn.config(state=tk.ACTIVE, text='重新开始', relief='raised')
def font_shake(nw, default):
nw.config(foreground='red')
for i in range(5):
if i%2 == 0:
time.sleep(0.05)
nw.config(anchor='n')
else:
time.sleep(0.05)
nw.config(anchor='s')
root.update()
nw.config(anchor='c')
root.update()
time.sleep(0.5)
nw.config(text=default, foreground='black')
def restart():
global readystate, used_name, result_dict, remain, pbStack
throw_label['image'] = shake_cup
readystate = 3
used_name = set()
result_dict = dict()
remain = 3
pbStack = {play_btn_A, play_btn_B, play_btn_C}
reset_btn.config(state=tk.DISABLED, relief='flat', text='')
for i in "ABC":
eval('name_%s.config(text="player %s")' % (i, i))
eval('entry_%s.config(state=tk.NORMAL)' % i)
eval('esv_%s.set("")' % i)
eval('confirm_btn_%s.config(state=tk.ACTIVE)' % i)
eval('result_%s.config(text="结果")' % i)
throw_winner['text'] = ""
box_frame_A = Frame(root)
box_frame_A.grid(column=1, ipadx=3)
name_A = Label(box_frame_A, text='player A', height=2)
name_A.pack()
signature_A = Label(box_frame_A, image=sigpic)
signature_A.pack()
play_btn_A = Button(box_frame_A, text='play', command=lambda : throw_touzi(play_btn_A, result_A, name_A))
play_btn_A.pack(side=BOTTOM, pady=3)
result_A = Label(box_frame_A, text='结果')
result_A.pack(side=BOTTOM)
entry_A = Entry(box_frame_A, textvariable=esv_A)
entry_A.pack(side=LEFT, padx=5)
confirm_btn_A = Button(box_frame_A, text='确定', command=lambda : set_name(confirm_btn_A, entry_A, name_A))
confirm_btn_A.pack(side=LEFT)
center_frame = Frame(root)
center_frame.grid(row=1, column=1, pady=20)
throw_label = Label(center_frame, image=shake_cup)
throw_label.pack()
throw_winner = Label(center_frame)
throw_winner.pack()
reset_btn = Button(center_frame, state=tk.DISABLED, relief='flat', command=restart)
reset_btn.pack()
box_frame_B = Frame(root)
box_frame_B.grid(row=3, padx=10)
name_B = Label(box_frame_B, text='player B', height=2)
name_B.pack()
signature_B = Label(box_frame_B, image=sigpic)
signature_B.pack()
play_btn_B = Button(box_frame_B, text='play', command=lambda : throw_touzi(play_btn_B, result_B, name_B))
play_btn_B.pack(side=BOTTOM)
result_B = Label(box_frame_B, text='结果')
result_B.pack(side=BOTTOM)
entry_B = Entry(box_frame_B, textvariable=esv_B)
entry_B.pack(side=LEFT, padx=5)
confirm_btn_B = Button(box_frame_B, text='确定', command=lambda : set_name(confirm_btn_B, entry_B, name_B))
confirm_btn_B.pack(side=LEFT)
box_frame_C = Frame(root)
box_frame_C.grid(row=3, column=2, padx=10)
name_C = Label(box_frame_C, text='player C', height=2)
name_C.pack()
signature_C = Label(box_frame_C, image=sigpic)
signature_C.pack()
play_btn_C = Button(box_frame_C, text='play', command=lambda : throw_touzi(play_btn_C, result_C, name_C))
play_btn_C.pack(side=BOTTOM)
result_C = Label(box_frame_C, text='结果')
result_C.pack(side=BOTTOM)
entry_C = Entry(box_frame_C, textvariable=esv_C)
entry_C.pack(side=LEFT, padx=5)
confirm_btn_C = Button(box_frame_C, text='确定', command=lambda : set_name(confirm_btn_C, entry_C, name_C))
confirm_btn_C.pack(side=LEFT)
if __name__ == '__main__':
pbStack = {play_btn_A, play_btn_B, play_btn_C}
for i in "ABC":
eval('play_btn_%s.config(state=tk.DISABLED)' % i)
root.mainloop()
