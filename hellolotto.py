from selenium import webdriver
from selenium.webdriver.support.ui import Select


def download_excel_lotto645(n_from, dir_download):
    webpage = 'https://www.nlotto.co.kr/gameResult.do?method=byWin'
    prefs = {'download.default_directory' : dir_download}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', prefs)
    if isinstance(n_from, int):
        nfrom = str(n_from)
    else:
        return False

    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.Chrome()
    driver.get(webpage)
    select_start = Select(driver.find_element_by_id('drwNoStart'))
    select_start.select_by_value(nfrom)
    driver.find_element_by_id('exelBtn').click()
