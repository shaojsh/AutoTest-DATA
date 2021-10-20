jdk+python环境配置
简单介绍下allure库的特性：
@allure.feature # 用于定义被测试的功能，被测产品的需求点
@allure.story # 用于定义被测功能的用户场景，即子功能点
@allure.step # 用于定义被测功能的操作步骤
@allure.attach # 用于向测试报告中输入附加的信息或附件
@allure.severity # 用于标记测试用例的严重等级
(PS:后续会根据日常需要不断补充)

allure 缺陷标记
BLOCKER = 'blocker'　　阻塞缺陷
CRITICAL = 'critical'　严重缺陷
NORMAL = 'normal'　　  一般缺陷
MINOR = 'minor'　　    次要缺陷
TRIVIAL = 'trivial'　　轻微缺陷　

下载nodejs，下载anywhere 配置启动命令（bat文件做git成每天开机启动 taskschd.msc）：cmd /k "cd /d C:\Users\shaojunshuai\PycharmProjects\AutoTest-python\Auto_Test\report\reporthtml&&anywhere

验证码识别：https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247484292&idx=1&sn=1d948f56e57a6586f11aabc0f0f6b3af&scene=19#wechat_redirect


schtasks /create /tn oss_download /tr python C:\Users\shaojunshuai\Desktop\start.py /sc daily /st 10:06:00
schtasks /create /tn start_up /sc daily /st 10:14:00 /tr python C:\Users\shaojunshuai\Desktop\start.py
lala
