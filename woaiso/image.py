#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import io
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

    def draw_background_text(self, text, font_size=5,color=(100, 43, 43)):
         # 文本所占区域大小
        lines = self.text_wrap(text, self.__get_font(font_size), self.width)
        text_height = self.__get_text_size('的', font_size)[1]
        y = 0
        for line in lines:
            self.draw.multiline_text((0, y), line, font=self.__get_font(font_size), fill=color)
            y += text_height
        return self.draw
    def text_wrap(self, text, font, max_width):
    
        lines = []
        # If the width of the text is smaller than image width
        # we don't need to split it, just add it to the lines array
        # and return
        if font.getsize(text)[0] <= max_width:

            lines.append(text) 
        else:
            # split the line by spaces to get words
            words = list(text)  
            i = 0
            # append every word to a line while its width is shorter than image width
            while i < len(words):
                line = ''         
                while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                    line = line + words[i]
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                # when the line gets longer than the max width do not append the word, 
                # add the line to the lines array
                lines.append(line)    
        return lines
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
    def get_out_file_path(self,width,height,format, volume=None):
        ext = format
        file_name = '%sx%s' % (width, height)
        if volume:
            file_name += '_' + str(volume)
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
        # 使图片变得更大
    def make_it_large(self, file_path, size, out_path):
        # 首先得到图片体积，然后识别还需要追加多大的体积
        fsize = os.path.getsize(file_path)
        kb_size = fsize/float(1024)
        differ = size - kb_size
        print(differ)
        if differ > 0:
            # 文件体积不够，需要补充
            temp_file = work_dir + '/large/temp_' + str(time.time()).split('.')[0]
            os.system('dd if=/dev/zero of=%s bs=1024 count=0 seek=$[%d]' % (temp_file, differ))
            os.system('cat %s %s > %s' % (file_path, temp_file, out_path))
            os.system('rm %s' % temp_file)
        else:
            pass
        
    def create(self,width, height, text=None, format='png', color=(39, 43, 51, 255), volume=None):
        out_file_path = self.get_out_file_path(width, height, format)
        if format == 'gif':
            frames = self.create_gif(width, height, text, background=color, color_set = 'RGBA')
            frames[0].save(fp=out_file_path, format='gif', append_images=frames[1:], save_all=True, duration=100, loop=0)
        else:  
            color_set = 'RGBA'
            if format == 'jpg':
                color_set = 'RGB'
            drawer = DrawFrame(width, height, background=color, color_set = color_set)
            current_size = 0
            max_size = 100 * 1024
            drawer.draw_text(text)
            # while  current_size < max_size:
            #     drawer.draw_text(text)
            #     file_bytes = io.BytesIO()
            #     drawer.canvas.save(file_bytes, format=format)
            #     size = file_bytes.tell()
            #     print(size)
            drawer.draw_background_text('成为科学家的一个标志是首先是一个独立的研究者。一个科学家必需有参与科学研究，发表，交流等活动的自主性。而如何赢得这种自主性呢？这种自主性是和成果挂钩的。成果无是发表文章或获得专利权。这对于一位以科学研究为职业的科学家是至关重要的。在过去总强调科学家应该首先具备科学精神，也就是你如果想以科学发现为职业，就必须从精神上有一种献身，求实，严谨和持之以恒的内质。这就是所谓的科学精神。但是随着科学研究成了一种社会建制，特别是当现代科学活动出现了政府主导的特征之后，科学就一下子从”小科学“变成了“大科学”，科学也随之变成了一种职业。这就是为什么说科学从业人员也象社会中其他人群那样，有白领，兰领，师傅，学徒，领导者，被领导者，剥削者，被剥削者，甚至也有资本家，工人，甚至还会有无赖，骗子，夸夸其谈者和滥竽充数者。这等的原因了。所以从这个意义上讲，并不是所有从事科学研究活动的人员都可以被称为“科学家”。只有那些获得了“自主性”，独立性，并且可以参预科学研究和交流等活动的科学研究人员才能称为实质意义上的科学家。不管是不是一位具有独立能力的科学家，但从事的是科学研究，那就必须具备科学精神。也就是具备求实，敬业精神。')
            drawer.canvas.save(fp=out_file_path, quality=300, optimize=False)
            drawer.destroy()
        
        if volume:
            out_path = self.get_out_file_path(width, height, format, volume)
            out_file_path = self.make_it_large(out_file_path,volume, out_path)

        return out_file_path
            

if '__main__' == __name__:
    XImage().create(600, 400, text='街电测试', format='png', color=(100,20,300), volume=300)