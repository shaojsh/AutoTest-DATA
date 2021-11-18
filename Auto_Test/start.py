import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# 生成环境日志构建
def productError():
    option = webdriver.ChromeOptions()
    # option.add_argument("headless")
    url = "http://10.10.128.153:5601/app/kibana#/discover?_g=(filters:!(),refreshInterval:(pause:!t,value:0)," \
          "time:(from:now-24h,to:now))&_a=(columns:!(appname,level,message),filters:!(('$state':(store:appState)," \
          "meta:(alias:!n,disabled:!f,index:'4cedbc90-f8b1-11ea-8343-ed223af86c0a',key:level,negate:!f," \
          "params:(query:ERROR),type:phrase),query:(match_phrase:(level:ERROR))))," \
          "index:'4cedbc90-f8b1-11ea-8343-ed223af86c0a',interval:auto,query:(language:kuery,query:''),sort:!()) "
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=option)
    driver.maximize_window()
    driver.get(url)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Refresh']")))
    el = driver.find_element_by_class_name('dscResultCount')
    error_tag = el.text
    time.sleep(2)
    html = driver.find_element_by_xpath("//*/tbody").get_attribute("outerHTML")
    driver.save_screenshot('prdLog.png')

if __name__ == "__main__":
    productError()
