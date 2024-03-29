#!/usr/local/bin/python3
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime


def execSearch(browser: webdriver):
    """
    Googleで検索を実行する
    :param browser: webdriver
    """
    # スクリーンショットのファイル名用に日付を取得
    dt = datetime.datetime.today()
    dtstr = dt.strftime("%Y%m%d%H%M%S")

    # Googleにアクセス
    browser.get('http://jusyo.jp/csv/new.php')
    sleep(5)

    browser.find_element_by_xpath(
        '//*[@id="dl-table"]/table[1]/tbody/tr[2]/td/span[2]/a').click()

    sleep(5)


if __name__ == '__main__':
    try:
        # browser = webdriver.Firefox()  # 普通のFilefoxを制御する場合
        # browser = webdriver.Chrome()   # 普通のChromeを制御する場合
        options = webdriver.ChromeOptions()
        prefs = {}
        prefs['download.default_directory'] = '/home/seluser/Downloads/test'
        prefs['download.directory_upgrade'] = True
        prefs['download.extensions_to_open'] = ''
        prefs['download.prompt_for_download'] = False
        prefs['safebrowsing.enabled'] = True
        options.add_experimental_option("prefs", prefs)
        desired_capabilities = options.to_capabilities()

        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=desired_capabilities)
        # desired_capabilities=DesiredCapabilities.CHROME)

        # HEADLESSブラウザに接続

        # Googleで検索実行
        execSearch(browser)

    finally:
        # 終了
        browser.close()
        browser.quit()
