from PIL import Image, ImageDraw, ImageFont
import qrcode
import os
import csv

work_dir = os.getcwd()
font_path = work_dir + '/fonts/pingfang-sc-medium.otf'


def __get_font(font_size):
    return ImageFont.truetype(font_path, font_size)


def read_csv():
    store_list = []
    file_path = '/Users/xiaofu/Downloads/魏家凉皮合作机柜.csv'
    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        index = 0
        for row in spamreader:
            if index > 0:
                store_list.append(row[0].split(','))
            index += 1
    csvfile.close()
    return store_list


image_size = (1024, 1200)
span_width = 40


# 魏家凉皮二维码生成
def create_qrcode(store_name, device_sn, file_name):
    canvas = Image.new('RGB', image_size, '#FFFFFF')
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=1,
    )
    qr.add_data('https://mp.weixin.qq.com/mp/profile_ext?device_sn=%s&action=home&__biz=MzIzNjY1OTUzNQ==&scene=124#wechat_redirect' % device_sn)
    qr.make(fit=True)
    qrcode_image = qr.make_image(fill_color="black", back_color="white")
    qrcode_image = qrcode_image.resize((image_size[0]-span_width*2, image_size[0]-span_width*2), Image.ANTIALIAS)
    canvas.paste(qrcode_image, (span_width, span_width))
    # 写文字
    draw = ImageDraw.Draw(canvas)
    draw.text((span_width, image_size[0]), '%s\nSN：%s' % (store_name, device_sn),
              font=__get_font(64), fill='#000000')
    # 判断文件是否存在
    if os.path.exists(r'temp/%s' % file_name):
          # ok
          print('文件存在%s' % file_name)
    else:
      pass
    canvas.save('temp/%s' % file_name,'JPEG', dpi=[300, 300], quality=90)
    canvas.close()



# create_qrcode('魏家凉皮（雁塔路小学餐厅）', 'S345PA1465', 'qrcode/S345PA1465.jpg')
store_list = read_csv()
print(len(store_list))
index = 0
for store in store_list:
    create_qrcode(store[1], store[2], 'qrcode/%s-%s-%s-%s.jpg' %
                  (store[4], store[5], store[1], store[2]))
    index += 1
