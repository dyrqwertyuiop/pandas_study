#! /usr/bin/env python
# -*- coding: utf-8 -*-

from MyQR import myqr
a = myqr.run(words = '小凯',version=10,picture='',colorized=True)
print(a)

# words : 文字内容,或者是个链接
# version : 二维码大小 范围是1~40
# level : 二维码的纠错级别 L M Q H ,默认是H
# picture : 二维码的背景图,默认是黑白
# colorized : 二维码的背景颜色,默认是False黑白
# save_name : 设置二维码的图片名,默认是qrcode
#