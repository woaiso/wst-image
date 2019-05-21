#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, send_file
from image import XImage

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['jpg','png','gif'])



@app.route("/x/<image_width>/<image_height>/<format>/<text>")
def image(image_width, image_height, format, text):
    out_file = XImage().create(image_width, image_height, text, format)
    if os.path.isfile(out_file):
        return send_file(out_file, mimetype='image/%s' % format, cache_timeout=1)
    else:
        return "请传入正确的信息 %s %s %s %s" % (image_width, image_height, format, text)


if __name__ == '__main__':
    app.debug = True
    app.run()