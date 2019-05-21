#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
from PIL import Image, ImageDraw, ImageFont


work_dir = os.getcwd()
font_path = work_dir + '/fonts/Alibaba-PuHuiTi-Light.otf'
IMAGE_BASE_PATH = work_dir + '/temp'


# 创建一帧图像
class DrawFrame(object):
    def __init__(self,width, height, background=(39, 43, 51, 255), color_set='RGBA'):
        # 画布
        self.canvas = Image.new(color_set, (int(width), int(height)), background)
        # 画笔
        self.draw = ImageDraw.Draw(self.canvas)
        self.width = self.canvas.size[0]
        self.height = self.canvas.size[1]
    def draw_text(self, text):
        if text:
            self.__draw_center_text(text=text, font_size=40)
            self.__draw_right_bottom_text(text='%s x %s'%(self.width, self.height), font_size=40)
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
    def __draw_right_bottom_text(self, text=None, font_size=20, color=(255,255,255)):
        
        # 文本所占区域大小
        text_size = self.__get_text_size(text, font_size)
        point_x = self.width - text_size[0] - 10
        point_y = self.height - text_size[1] - 10
        self.draw.text((point_x, point_y), text, font=self.__get_font(font_size), fill=color)
        return self.draw
        
    def __draw_center_text(self, text=None, font_size=20, color=(255,255,255)):
        # 文本所占区域大小
        text_size = self.__get_text_size(text, font_size)
        point_x = (self.width - text_size[0])/2
        point_y = (self.height - text_size[1])/2
        self.draw.text((point_x, point_y), text, font=self.__get_font(font_size), fill=color)
        return self.draw
    def destroy(self):
        del self.draw
        del self.canvas




class XImage(object):
    def __init__(self):
        pass
    def get_out_file_path(self,width,height,format):
        ext = format
        file_name = '%sx%s' % (width, height)
        tstamp = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime()) 
        uniq_fname = '{}_{}.{}'.format(file_name, tstamp, ext)
        return os.path.join(IMAGE_BASE_PATH, uniq_fname)

    def create_gif(self, width, height, text, background, color_set):
        frames = []
        for i in range(10):
            item = DrawFrame(width, height,background, color_set)
            if i%3 == 0:
                item.draw_text(text+str(i))
            else:
                item.draw_text(text+str(i))
            frames.append(item.canvas)
        return frames
    def create(self,width, height, text=None, format='png', color=(39, 43, 51, 255)):
        out_file_path = self.get_out_file_path(width, height, format)
        if format == 'gif':
            frames = self.create_gif(width, height, text, background=color, color_set = 'RGBA')
            frames[0].save(fp=out_file_path, format='gif', append_images=frames[1:], save_all=True, duration=100, loop=0)
        else:  
            drawer = DrawFrame(width, height, background=color, color_set = 'RGBA')
            drawer.draw_text(text)
            drawer.canvas.save(fp=out_file_path)
            drawer.destroy()
        return out_file_path
            

if '__main__' == __name__:
    XImage().create(600, 400, text='宝贝儿老婆我爱你', format='gif')