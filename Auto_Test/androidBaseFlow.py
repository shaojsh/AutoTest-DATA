#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

sys.path.append('.')
__author__ = 'shaojunshuai'

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

try:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    screenWidth, screenHeigth = poco.get_screen_size()
except:
    print('未驱动手机')


# 打开SmartXueWei App
def startSmartXueWeiApp():
    # 清除缓存
    clear_app('com.future.shopping')
    # 打开智慧徐圩app
    start_app("com.future.shopping")


if __name__ == '__main__':
    startSmartXueWeiApp()
