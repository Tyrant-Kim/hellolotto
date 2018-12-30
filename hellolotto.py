from selenium import webdriver
from selenium.webdriver.support.ui import Select

def download_excel_lotto645(nfrom):
    webpage = 'https://www.nlotto.co.kr/gameResult.do?method=byWin'
    driver = webdriver.Chrome()
    driver.get(webpage)
    select_start = Select(driver.find_element_by_id('drwNoStart'))
    select_start.select_by_value(nfrom)
    driver.find_element_by_id('exelBtn').click()

