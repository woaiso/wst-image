#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import threading
import time
from turtle import Canvas

from PIL import Image, ImageDraw, ImageFont

work_dir = os.getcwd()
font_path = work_dir + '/fonts/Alibaba-PuHuiTi-Light.ttf'
IMAGE_BASE_PATH = work_dir + '/temp'


# 创建一帧图像
class DrawFrame(object):
    def __init__(self,width, height, bg_color, color_set):
        # 画布
        self.canvas = Image.new(color_set, (int(width), int(height)), bg_color)
        # 画笔
        self.draw = ImageDraw.Draw(self.canvas)
        self.width = self.canvas.size[0]
        self.height = self.canvas.size[1]
    def draw_text(self, text, text_color):
        if text:
            self.__draw_center_text(text=text, font_size=40, color=text_color)
            self.__draw_right_bottom_text(text='%s x %s'%(self.width, self.height), font_size=40, color=text_color)
        else: #未传入文本则绘制宽高
            # 需要绘制的文本，如 400 x 600
            text = '%s × %s' % (self.width, self.height)
            self.__draw_center_text(text=text, font_size=40)
    # 获取字体
    def __get_font(self, font_size):
        return ImageFont.truetype(font_path, font_size)
    # 获取文本在该字体下所占大小
    def __get_text_size(self, text, font_size):
        fnt = self.__get_font(font_size)
        fnt_size = fnt.getsize(text)
        while fnt_size[0] > self.width or fnt_size[1] > self.height:
            font_size -= 5
            fnt = ImageFont.truetype(font_path, font_size)
            fnt_size = fnt.getsize(text)
        return fnt_size

    # 在右下角绘制图片大小文案
    def __draw_right_bottom_text(self, text=None, font_size=20, color='#FFFFFF'):

        # 文本所占区域大小
        text_size = self.__get_text_size(text, font_size)
        point_x = self.width - text_size[0] - 10
        point_y = 10
        self.draw.text((point_x, point_y), text, font=self.__get_font(font_size), fill=color)
        return self.draw

    def __draw_center_text(self, text=None, font_size=20, color='#FFFFFF'):
        # 文本所占区域大小
        text_size = self.__get_text_size(text, font_size)
        point_x = (self.width - text_size[0])/2
        point_y = (self.height - text_size[1])/2
        self.draw.text((point_x, point_y), text, font=self.__get_font(font_size), fill=color)
        return self.draw
    def draw_background(self, bg_image_path):
          img_full_path = '%s/%s' % (IMAGE_BASE_PATH, bg_image_path)
          bg_image = Image.open(img_full_path).convert("RGBA")

          canvas_x, canvas_y = self.canvas.size
          bg_image_x, bg_image_y = bg_image.size

          # 缩放图片
          scale = 1
          bg_image_scale = max(canvas_x / (scale * bg_image_x), canvas_y / (scale * bg_image_y))
          new_size = (int(bg_image_x * bg_image_scale), int(bg_image_y * bg_image_scale))

          bg_image = bg_image.resize(new_size, resample=Image.ANTIALIAS)

          bg_image_x, bg_image_y = bg_image.size
          # 水印位置
          self.canvas.paste(bg_image, (canvas_x - bg_image_x, canvas_y - bg_image_y), bg_image)
          return self.draw;
    def draw_rectangle(self,radius=10, color='#009AD9'):
          '''Rounds'''
          w, h = self.canvas.size
          x,y = (0,0)
          r = radius
          self.draw.ellipse((x,y,x+r,y+r),fill=color)
          self.draw.ellipse((x+w-r,y,x+w,y+r),fill=color)
          self.draw.ellipse((x,y+h-r,x+r,y+h),fill=color)
          self.draw.ellipse((x+w-r,y+h-r,x+w,y+h),fill=color)

          '''rec.s'''
          # self.draw.rectangle((x+r/2,y, x+w-(r/2), y+h),fill=color)
          # self.draw.rectangle((x,y+r/2, x+w, y+h-(r/2)),fill=color)
          return self.draw;
    def destroy(self):
        del self.draw
        del self.canvas




class XImage(object):
    def __init__(self):
        pass
    def get_out_file_path(self,width,height,format, volume=None):
        ext = format
        file_name = '%sx%s' % (width, height)
        if volume:
            file_name += '_' + str(volume)
        tstamp = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        uniq_fname = '{}_{}.{}'.format(file_name, tstamp, ext)
        return os.path.join(IMAGE_BASE_PATH, uniq_fname)

    def create_gif(self, width, height, text, bg_color, text_color):
        frames = []
        for i in range(10):
            item = DrawFrame(width, height,bg_color, 'RGBA')
            if i%3 == 0:
                item.draw_text(text+str(i),text_color=text_color)
            else:
                item.draw_text(text+str(i), text_color=text_color)
            frames.append(item.canvas)
        return frames
        # 使图片变得更大
    def make_it_large(self, file_path, size, out_path):
        # 首先得到图片体积，然后识别还需要追加多大的体积
        fsize = os.path.getsize(file_path)
        kb_size = fsize/float(1024)
        differ = size - kb_size
        if differ > 0:
            # 文件体积不够，需要补充
            temp_file = work_dir + '/temp/temp_' + str(time.time()).split('.')[0]
            os.system('dd if=/dev/zero of=%s bs=1024 count=0 seek=%d' % (temp_file, differ))
            os.system('cat %s %s > %s' % (file_path, temp_file, out_path))
            os.system('rm %s %s' % (temp_file, file_path))
        else:
            pass
        return out_path

    def create(self,width, height, text, format, bg_color, text_color, volume,radius,padding,bg_image):
        # 设置默认值
        if not width:
            width = 520
        if not height:
            height = 520
        if not format:
            format = 'png'
        if not bg_color:
            bg_color = '#009AD9'
        if not text_color:
            text_color = '#FF0000'
        if not volume:
            volume = None
        else:
            volume = int(volume)
        out_file_path = self.get_out_file_path(width, height, format)
        if format == 'gif':
            frames = self.create_gif(width, height, text, bg_color=bg_color, text_color=text_color)
            frames[0].save(fp=out_file_path, format='gif', append_images=frames[1:], save_all=True, duration=100, loop=0)
        else:
            color_set = 'RGBA'
            if format == 'jpg' or format== 'jpeg':
                color_set = 'RGB'
            drawer = DrawFrame(width, height, bg_color=bg_color, color_set=color_set)
            if bg_image:
                  # 设置一个背景图片
                  drawer.draw_background(bg_image)
            if int(padding) > 0:
                  drawer.draw_rectangle()
            drawer.draw_text(text, text_color)
            drawer.canvas.save(fp=out_file_path, quality=300, optimize=False)
            # 预览
            drawer.canvas.show()
            # 预览
            drawer.destroy()


        if volume:
            if volume > 1024 * 5:
                volume = 1024 * 5 # 最大支持5MB文件
            out_path = self.get_out_file_path(width, height, format, volume)
            out_file_path = self.make_it_large(out_file_path,volume, out_path)


        # 10秒后移除文件
        timer = threading.Timer(3, self.delete_file, [out_file_path])
        timer.start()
        return out_file_path
    def delete_file(self, file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            print('delete file error %s' % e)

if '__main__' == __name__:
    XImage().create(1080,720,'anyimage.xyz','png','#1890FF', '#FFFFFF', 0,0,100,'1559913294198.jpg')
