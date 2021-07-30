import time
from driver import Driver


def jbhifi(term):
    # url = f"https://www.jbhifi.com.au/search?query={term}&page=1"
    url = f"https://www.jbhifi.com.au/search?query={term}&page=1&hitsPerPage=100"
    dr = Driver()
    try:
        dr.driver.get(url)
    except:
        dr.quit()
        return "error"
    result = []
    try:
        # main = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.CLASS_NAME, "collection-container"))
        # )
        # print(main)

        time.sleep(10)
        items = dr.driver.find_elements_by_class_name(
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
        dr.quit()

    dr.quit()
    return dict(result=result)
