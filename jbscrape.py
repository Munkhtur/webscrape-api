import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def jbhifi(link):
    driver = webdriver.Firefox()
    driver.get(link)
    result = []
    try:
        # main = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.CLASS_NAME, "collection-container"))
        # )
        # print(main)

        time.sleep(10)
        items = driver.find_elements_by_class_name(
            'ais-hits--item')
      
        for item in items:
            title = item.find_element_by_xpath(
                './div/a/div/div[1]/h4').text
            image = item.find_element_by_xpath(
                './div/a/div/div[2]/div/img').get_attribute('src')

            price = item.find_element_by_xpath(
                './div/div[1]/a/div/div/span[1]').text

            result.append({
                'title': title,
                'image': image,
                'price': price,
            })
    except:
        driver.quit()

    driver.quit()
    return result
