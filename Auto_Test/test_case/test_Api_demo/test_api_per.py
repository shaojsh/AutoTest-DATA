#!/usr/bin/python
# -*- coding: UTF-8 _*_
import hashlib
import os
import sys
import threading
import time
import pytest

from common.Request import RequestsHandler
import allure
from common.Retrun_Response import dict_style

from common.Yaml_Data import HandleYaml
from run_all_case import logger

API_dir_cnf = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test'
handleyaml = HandleYaml(API_dir_cnf + '\\test_data\\test_yaml_data.yaml')
yamldict = handleyaml.get_data()

def_name = sys._getframe().f_code.co_name


@pytest.mark.run(order=1)
@allure.severity("blocker")
@allure.description("测试http://123.133.28.226:60011接口")
@allure.testcase("http://123.133.28.226:60011", "测试用例地址 👇")
def test_api_per():
    logger.info("开始执行脚本%s:\n", def_name)
    timer = threading.Timer(1, fun_ApiTimeLoop)
    timer.start()
    time.sleep(30)  # n秒后停止定时器
    timer.cancel()


def fun_ApiTimeLoop():
    # 优化格式化化版本
    timeNow = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    appid = 'cjt'
    checkcode = 'cjt' + timeNow + 'e14b7c06-f127-4f7c-86f0-eec9bbcdc8d6'
    m = hashlib.md5()
    m.update(checkcode.encode('utf-8'))

    opera_url = "http://123.133.28.226:60011/gpl/webservice/security/getToken?appid=" + appid + "&timestamp=" + timeNow + "&checkcode=" + m.hexdigest()
    opera_result = RequestsHandler().post_Req(url=opera_url, params='')
    sting_response = opera_result.content.decode()
    json_response = dict_style(sting_response)
    token = json_response.get("token")
    if token is None:
        print('ERROR,Token没拿到')
    print(json_response)
    global timer
    timer = threading.Timer(1, fun_ApiTimeLoop)
    timer.start()
