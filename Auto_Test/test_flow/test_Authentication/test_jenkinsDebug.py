import allure
import pytest
import sys

from airtest.core.api import start_app, touch, text
from airtest.core.cv import Template
from airtest.core.api import *
from selenium import webdriver
from airtest.core.android import Android
from androidBaseFlow import startSmartXueWeiApp, screenWidth, screenHeigth
from common import Assert
from run_all_case import jenkins, driverPath, mobileDriver
from time import sleep


# @pytest.mark.run(order=2)
# @allure.severity("blocker")
# @allure.description("测试 http://10.10.128.152:10053/user/register 中小微企业注册流程")
# @allure.testcase("http://10.10.128.152:10053/user/register", "注册 👇")
# def test_baidu():
#     def_name = sys._getframe().f_code.co_name
#     test_Assert = Assert.Assertions(def_name)
#     if jenkins:
#         option = webdriver.ChromeOptions()
#         option.add_argument('headless')  # 浏览器不提供可视化页面
#         option.add_argument('no-sandbox')  # 以最高权限运行
#         option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
#         option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
#         option.add_argument('--window-size=1920,1080')  # 设置浏览器分辨率（窗口大小）
#         driver = webdriver.Chrome(options=option)
#     else:
#         driver = webdriver.Chrome(executable_path=driverPath)
#     driver.get('https://www.baidu.com/')
#     sleep(1)
#     text = driver.find_element_by_id('s-top-loginbtn').text
#     test_Assert.assert_text_ui(text, '登录')


@pytest.mark.run(order=1)
@allure.severity("blocker")
@allure.description("测试 小程序自动化疏通测试-Android")
def test_Android():
    startSmartXueWeiApp()
    mobileDriver(text='同意并继续').click()
    mobileDriver(text='允许').click()
    i = 0
    while i < 3:
        sleep(1)
        # 滑动
        swipe([0.9 * screenWidth, screenHeigth / 2], [0.25 * screenWidth, screenHeigth / 2])
        i = i+1

    # 图片识别点击
    picture_dir = os.getcwd() + '\\test_data\\picture\\zhihuixuwei001.png'
    touch(Template(picture_dir))

    # 输入用户名，密码
    mobileDriver(text='请输入手机号').click()
    text('17621198933')
    mobileDriver(text='请输入密码').click()
    text('1q2w3e4r')
    mobileDriver(text='立即登录').click()
