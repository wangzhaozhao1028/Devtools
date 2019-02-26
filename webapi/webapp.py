#coding=utf-8

from flask import Flask
from flask import render_template
from flask import request
#demo 实现网盘功能

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html',name='wang')

@app.route('/upload', methods=['GET','POST'])
def upload():
	file = request.files.get("file")
	if not file:
		return u"上传文件"
	file.save('static/%s' %file.filename)
	return 'http://127.0.0.1:5000/static/%s' %file.filename

if __name__ == '__main__':
	app.run(debug=True)