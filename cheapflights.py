import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def cheapflights(link):
    driver = webdriver.Firefox()
    result = []
    driver.get(link)
    time.sleep(10)
    for i in range(3):
        try:
            button = driver.find_element_by_link_text('Show more results')
            button.click()
            print('click')
            time.sleep(10)
        except:
            break

    try:
        # main = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.ID, "MIBiGBN8-a-1"))
        # )

        items = driver.find_elements_by_class_name(
            'Base-Results-HorizonResult')
        print(items, '>>>>>>>>>>>>>>')
        print(items[1].text)
        print('-------------------')

        for item in items:
            logo = item.find_element_by_xpath(
                './div/div[2]/div/div[1]/div[2]/div/ol/li/div/div/div[1]/div/img').get_attribute('src')

            hours = item.find_element_by_xpath(
                './div/div[2]/div/div[1]/div[2]/div/ol/li/div/div/div[2]/div[1]').text

            duration = item.find_element_by_xpath(
                './div/div[2]/div/div[1]/div[2]/div/ol/li/div/div/div[4]/div[1]').text
            price = item.find_element_by_xpath(
                './div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/a/span/span').text
            name = item.find_element_by_xpath(
                './div/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/a/span').text

            result.append({
                'logo': logo,
                'hours': hours,
                'price': price,
                'duration': duration,
                'name': name,
            })
    except:
        driver.quit()

        # //*[@id = "vBUK"]
        # //*[@id = "vBUK-info-leg-0"]/div/div[1]/div/img
        # //*[@id = "vBUK-info-leg-0"]/div/div[2]/div[1]
        # //*[@id = "vBUK-info-leg-0"]/div/div[4]/div[1]
        # //*[@id = "U6W0-mb-aE-11246a416c6-price-text"]
        # /html/body/div[1]/div[1]/main/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[2]/div[1]/div/div[14]

        # //*[@id = "c33Mr-mb-nE038274bfd50-booking-link"]/span

    print(result)
    driver.quit()

    return result
