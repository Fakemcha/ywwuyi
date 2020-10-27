# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def request_by_chrome(url):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        prefs = {"profile.managed_default_content_settings.images": 2}
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-plugins')  # 禁用插件
        chrome_options.add_argument('--disable-popup-blocking')  # 禁用弹出拦截
        chrome_options.add_argument('--incognito')  # 隐身模式
        chrome_options.add_argument('--no-sandbox')  # 取消沙盒模式
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome('chromedriver', options=options, chrome_options=chrome_options, keep_alive=False)
        browser.set_page_load_timeout(60)
        browser.set_script_timeout(60)
        try:
            browser.get(url)
            response = browser.page_source
            # time.sleep(1000000)
            browser.quit()
        except Exception as e:
            browser.quit()
            print(str(e))
    except Exception as e:
        print(str(e))
    return response


def jt(url):
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('disable-infobars')
        # chrome_options.add_argument('lang=zh_CN.UTF-8')
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # prefs["credentials_enable_service"] = False
        # prefs["profile.password_manager_enabled"] = False
        # chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument('--hide-scrollbars')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-plugins')  # 禁用插件
        chrome_options.add_argument('--disable-popup-blocking')  # 禁用弹出拦截
        chrome_options.add_argument('--incognito')  # 隐身模式
        chrome_options.add_argument('--no-sandbox')  # 取消沙盒模式
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome('chromedriver', options=options, chrome_options=chrome_options, keep_alive=False)
        browser.set_page_load_timeout(60)
        browser.set_script_timeout(60)
        try:
            browser.get(url)
            response = browser.page_source

            # time.sleep(1000000)
            browser.maximize_window()
            ele = browser.find_element_by_id("footer")
            left = ele.location['x']
            top = ele.location['y']
            right = left + ele.size['width']
            bottom = top + ele.size['height']
            browser.save_screenshot('/home/sc.png')
            # browser.save_screenshot(r'C:\Users\fakemcha\Desktop\ss.png')
            # time.sleep(1000000)
            browser.quit()
        except Exception as e:
            browser.quit()
            print(str(e))
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    url = r"http://www.winiis.com/"
    url = r"https://lol.qq.com/main.shtml"
    jt(url)