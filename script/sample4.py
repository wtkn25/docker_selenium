#!/usr/local/bin/python3
from selenium import webdriver
from remote_chromedriver import RemoteChromeDriver
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

        # HEADLESSブラウザに接続
        browser = RemoteChromeDriver()
        # desired_capabilities=DesiredCapabilities.CHROME)

        # HEADLESSブラウザに接続

        # Googleで検索実行
        execSearch(browser)

    finally:
        # 終了
        browser.close()
        browser.quit()
