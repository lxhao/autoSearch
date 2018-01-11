#!/usr/bin/env python3
# encoding: utf-8
import sys
import os
import time
import datetime
import re

# import Image
from PIL import Image
import pytesseract

prog = re.compile('\d{1,2}\.(.*)')

def search(problem=None):
    assert(problem)
    url = 'https://www.baidu.com/s?wd=%s' % problem
    os.system('/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome %s' % url)

# http://www.10tiao.com/html/761/201706/2650367001/1.html
# pip install pytesseract 先安装依赖包
def recogProblem(img_path):

    # 剪切出题目部分
    img = Image.open(img_path)
    img_wide, img_len = img.size
    x1 = int(img_wide * 69 / 1080)
    x2 = int(img_wide * 1010 / 1080)
    y1 = int(img_len * 282 / 1920)
    y2 = int(img_len * 570 / 1920)
    region = img.crop((x1, y1, x2, y2))

    # 保存到文件
    # output_filename = './题目/题目%s.png' % datetime.datetime.now()
    # region.save(output_filename) #保存图片

    # 识别
    text = pytesseract.image_to_string((region), lang='chi_sim')
    text = text.replace('\n', '')
    text = text.replace(' ', '')
    match_res = prog.match(text)
    if match_res:
        text = match_res.groups(1)[0]
    print(text)
    search(problem=text)

def main():
    while True:
        start_time = time.time()
        input("输入任意键截屏搜索:")
        os.system('sh getImage.sh')
        recogProblem('./problem.png')
        print('耗时：%.2f s' % (time.time() - start_time))

if __name__ == '__main__' :
    main()
