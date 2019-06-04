#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from flask import Flask, send_file, request,render_template, make_response
from woaiso.image import XImage


app = Flask(__name__)
work_dir = os.getcwd()
ALLOWED_EXTENSIONS = set(['jpg','png','gif'])
UPLOAD_FOLDER = work_dir + '/temp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


work_dir = os.getcwd()

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
      if request.method == 'POST':
            # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            ext = file.filename.rsplit('.', 1)[1].lower();
            filename = str(int(time.time() * 1000)) + '.%s' % ext
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return filename;

@app.route('/x')
def image():
    image_width = request.args.get('width')
    image_height = request.args.get('height')
    image_text = request.args.get('text')
    image_format = request.args.get('format')
    image_volume = request.args.get('volume')
    bg_color = request.args.get('bgcolor')
    text_color = request.args.get('color')
    download = request.args.get('download')
    radius = request.args.get('radius')
    padding = request.args.get('padding')
    bg_image = request.args.get('bg_image')

    print('%s %s %s %s %s %s %s %s %s %s' % (image_width, image_height, image_text, image_format,bg_color,text_color,image_volume,radius,padding,bg_image))

    out_file = XImage().create(image_width, image_height, image_text, image_format,bg_color,text_color, image_volume,radius,padding,bg_image)
    if os.path.isfile(out_file):
        extension = os.path.splitext(out_file)[-1][1:]
        if download == '1':
            response = make_response(send_file(out_file, mimetype='image/%s' % extension, cache_timeout=1), 200)
            response.headers['content-disposition'] = 'attachment; filename="%s"' % os.path.basename(out_file)
            return response
        else:
            return send_file(out_file, mimetype='image/%s' % extension, cache_timeout=1, as_attachment=False)
    else:
        return "请传入正确的信息 %s %s %s %s %s %s" % (image_width, image_height, image_text, image_format,text_color,image_volume)

def start():
    app.debug = True
    app.run(host='0.0.0.0')
