#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, send_file, request,render_template, make_response
from woaiso.image import XImage

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['jpg','png','gif'])

work_dir = os.getcwd()

@app.route('/')
def home():
    return render_template('index.html')

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
    print('%s %s %s %s %s %s' % (image_width, image_height, image_text, image_format,bg_color,image_volume))

    out_file = XImage().create(image_width, image_height, image_text, image_format,bg_color,image_volume)
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
    app.debug = False
    app.run(host='0.0.0.0')