# content of test_task.py

import random
import conftest, time
from configuration import *
from selenium.webdriver.common.by import By
from functools import partial
from pytest_bdd import scenario, given, when, then, feature
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


scenario = partial(scenario, "feature/test_case.feature")


# @feature('test_case.feature', 'Сортировка смартфонов в Яндекс.Маркете')
def test_case(base):
    driver = base
    driver.get(URL)
    assert "Яндекс" in driver.title

    # @scenario('Зайти на "Яндекс"')
    def test_market():
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Маркет"))).click()
        finally:
            time.sleep(4)
            assert "Маркет" in driver.page_source
    test_market()

    def test_page_smartphone_all_filter():
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.ID, "catalogPopupButton").click()
        time.sleep(4)

        # driver.find_element(By.LINK_TEXT, "Смартфоны").click()
        driver.find_element(By.XPATH, '//*[@id="catalogPopup"]/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/ul/li[1]/div/a').click()
        time.sleep(4)
        assert "No results found." not in driver.page_source

        driver.find_element(By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/div/div[5]/div/div/"
                                      "div/div/div/div[2]/div/div[5]/div/div/div/a/button").click()
        time.sleep(4)
        assert "No results found." not in driver.page_source
    test_page_smartphone_all_filter()

    def test_filters():
        driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]/input").send_keys(PRICE)
        time.sleep(4)
        #   assert find_element.get_attribute('value') == PRICE

        brands = driver.find_elements(By.CLASS_NAME, '_24XUl')
        l = list(range(0, 10))
        random.shuffle(l)
        for i in l:
            brands[i].click()
            time.sleep(4)

        driver.find_element(By.CSS_SELECTOR, 'body > div._111XI.main > section > div:nth-child(2) > div > div > div._3aaVQ > div:nth-child(1) > div:nth-child(14) > div > button').click()
        #   driver.find_element(By.CSS_SELECTOR, 'body > div._111XI.main > section > div:nth-child(2) > div > div > div._3aaVQ > div:nth-child(1) > div:nth-child(14)').click()
        time.sleep(4)

        driver.find_element(By.CLASS_NAME, "_2xtC2").click()
        time.sleep(4)

        driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[2]/div[1]/div[14]/div/div/div/div[1]/input").send_keys(DIAGONAL)
        #   assert diagonal.find_element.get_attribute('placeholder') == DIAGONAL

        driver.find_element(By.XPATH, "/html/body/div[4]/section/div[2]/div/div/div[3]/div/div/a[2]").click()
        time.sleep(3)
        assert "No results found." not in driver.page_source
    test_filters()

    def test_last_remember():
        name_phone = driver.find_element(By.XPATH, "")
        time.sleep(3)
        assert driver.find_element()
        return name_phone
    test_last_remember()

    def test_sorting_change():
        driver.find_element(By.XPATH, "").click()
        time.sleep(3)
        assert "No results found." not in driver.page_source
    test_sorting_change()

    def test_search_name_phone():
        name_phone = test_last_remember()
        driver.find_element(By.CLASS_NAME, "").send_keys(name_phone)
        time.sleep(3)
        assert "No results found." not in driver.page_source
    test_search_name_phone()

    def test_smartphone_rating():
        driver.find_element(By.LINK_TEXT, "").click()
        time.sleep(3)
        assert "No results found." not in driver.page_source
    test_smartphone_rating()

    def test_quit_browser():
        driver.close()
        driver.quit()
        assert driver is None
    test_quit_browser()


if __name__ == '__main__':
    test_case(conftest.base)
