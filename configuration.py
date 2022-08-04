from selenium import webdriver


PATH = r"C:\Chrone\chromedriver.exe"
PARAMS = "start-maximized"
URL = "https://yandex.ru/"
PRICE = "20000"
DIAGONAL = "3"


OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])
OPTIONS.add_argument(PARAMS)
