import ddddocr
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os


class Crawler:
    def __init__(self):
        self.url = "https://bsr.twse.com.tw/bshtm/bsMenu.aspx"

    # main function
    def crawl(self, id):
        options = Options()
        options.chrome_executable_path = "chromedriver.exe"
        # customizing location of downloaded files
        path = os.path.dirname(__file__)
        options.add_experimental_option("prefs", {
            "download.default_directory": os.path.join(path, "data")
        })

        # webdriver setup
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)

        # extracting captcha image
        img = driver.find_elements(By.TAG_NAME, "img")[1]
        urlretrieve(img.get_attribute("src"), "captcha.png")
        captcha = driver.find_element(By.NAME, "CaptchaControl1")
        captcha.send_keys(self.captcha_solve("captcha.png"))

        # filling in stock code
        stock_id = driver.find_element(By.ID, "TextBox_Stkno")
        stock_id.send_keys(id)

        # sending out request
        btn = driver.find_element(By.ID, "btnOK")
        btn.click()

        # downloading csv file
        download = driver.find_element(By.ID, "HyperLink_DownloadCSV")
        download.click()
        sleep(5)
        driver.close()

    def captcha_solve(self, img):
        with open(img, "rb") as f:
            img = f.read()
        ocr = ddddocr.DdddOcr()
        res = ocr.classification(img)
        return res


if __name__ == "__main__":
    crawler = Crawler()
    crawler.crawl("0050")
