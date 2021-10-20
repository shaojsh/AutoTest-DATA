#!/usr/bin/python
# -*- coding: UTF-8 _*_
import time
import os
import sys
from common.Logs import Log
import pytest
from common import Shell

from common.Yaml_Data import HandleYaml

root_dir = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test'
runMode = 'UI'
evn = ''
jenkins = False
try:
    jenkins = os.environ["jenkins"]
    print('jenkins Run.....')
except:
    print('本地环境测试')
# 环境run取得
driverPath = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test\\' + 'chromedriver.exe'
if not jenkins:  # 本地 获取参数
    config = HandleYaml(root_dir + '\\test_data\\config.yaml')
    runMode = config.get_data()['configEvn']['runMode']
    evn = config.get_data()['configEvn']['evn']
if jenkins:
    runMode = os.environ["runMode"]
    evn = os.environ["evn"]
    RunPath = os.environ["RunPath"]

if evn == 'SIT':
    handleyaml = HandleYaml(root_dir + '\\test_data\\ConfigGol-SIT.yaml')
    if jenkins:  # linux 路径表示
        handleyaml = HandleYaml('/var/lib/jenkins/workspace/AutoTest-DaTa/Auto_Test/test_data/ConfigGol-SIT.yaml')
else:
    handleyaml = HandleYaml(root_dir + '\\test_data\\ConfigGol-UAT.yaml')
    if jenkins:  # linux 路径表示
        handleyaml = HandleYaml('/var/lib/jenkins/workspace/AutoTest-DaTa/Auto_Test/test_data/ConfigGol-UAT.yaml')

# handleyaml = HandleYaml(os.getcwd() + '\\..\\test_data\\ConfigGol-SIT.yaml')  # 调试db用

yamldict = handleyaml.get_data()

mobileDriver = ''
if runMode != 'UI':
    pass
    # import androidBaseFlow
    # mobileDriver = androidBaseFlow.poco
file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger

if __name__ == "__main__":
    try:
        print("开始执行脚本")
        logger.info("==================================" + time.strftime('%Y-%m-%d %H:%M:%S',
                                                                         time.localtime()) + "===================================")
        if not jenkins:
            root_dir = os.path.dirname(os.path.abspath('.')) + '\\Auto_Test' + yamldict['test_path_list']['url_ui']
        else:
            root_dir = os.path.dirname(os.path.abspath('.')) + '/Auto_Test' + RunPath
        pytest.main([root_dir, "--alluredir","./report/reportallure/"])
        print("脚本执行完成")
    except Exception as e:
        logger.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)

    try:
        shell = Shell.Shell()
        cmd = 'allure generate %s -o %s --clean' % ('./report/reportallure/', './report//reporthtml/')
        print("开始执行报告生成")
        shell.invoke(cmd)
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        raise

    time.sleep(5)
