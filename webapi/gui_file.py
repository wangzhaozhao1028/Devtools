#coding=utf-8

#version: 1.0
#__author__: only

from Tkinter import *
from tkFileDialog import *
import urllib2

def upload():
	filename = askopenfilename(title = "选择文件")
	# print filename
	file = open(filename, 'rb').read()
	url = 'http://127.0.0.1:5000/upload'
	req = urllib2.Request(url)
	data = '''------WebKitFormBoundaryEyEobO4inAa8JVJL
Content-Disposition: form-data; name="file"; filename="%s"
Content-Type: image/jpeg

[file]
------WebKitFormBoundaryEyEobO4inAa8JVJL--''' %filename.split('/')[-1]
	data = bytes(data)
  	data = data.replace(bytes('[file]'),file)	#子文本替换
  	req.add_header('Content-Type','multipart/form-data; boundary=----WebKitFormBoundaryEyEobO4inAa8JVJL')
	html = urllib2.urlopen(req, data=data).read()
	print html
root = Tk()
root.title("文件分享软件")
root.geometry("300x140+900+300")
ent = Entry(root,width=40)				#布局grid / (实例)
ent.grid()	#(调用)
btn_up = Button(root,text="上 传", command=upload)
btn_up.grid()
btn_down = Button(root, text="下 载")
btn_down.grid()

mainloop()	#显示窗口

