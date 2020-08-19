from enum import Enum


class path_backstage_examine(Enum):
    # 后台登录以及审核页面
    input_actLogin_css = '#root > div > div.main___3sFq0 > div > form > div:nth-child(1) > div.ant-col.ant-form-item-control-wrapper > div > span > span > input'  # 用户名
    input_actPwd_css = '#root > div > div.main___3sFq0 > div > form > div:nth-child(2) > div.ant-col.ant-form-item-control-wrapper > div > span > span > input'  # 密码
    btn_login_css = '#root > div > div.main___3sFq0 > div > form > div:nth-child(3) > button'  # 用户登录
    txt_backstage_css = '#root > section > section > main > div > div > section:nth-child(1) > div.banner___3Un5s > h5'  # 财金通企业后台管理系统
    btn_bussMan_xpath = "//*[text() = '企业管理']"  # 企业管理按钮
    btn_bussList_css = '#sMenu_0kawa954x-0172-726f1870-8a8a018c-0001\$Menu > li'  # 企业列表按钮
    btn_bussListName_xpath = '//*[@id="root"]/section/section/main/div/div/div/div[2]/table/tbody/tr'  # 企业名称
    txt_userInfor_css = '#root > section > section > main > div > div:nth-child(1) > div.ant-tabs-bar.ant-tabs-top-bar > div > div > div > div > div:nth-child(1) > div'  # 用户基本信息
    btn_examinePass_css = '#root > section > section > main > div > div:nth-child(4) > div.ant-btn-group > button.ant-btn.ant-btn-primary'  # 审核通过