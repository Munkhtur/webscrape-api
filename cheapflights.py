
import time
from selenium.common.exceptions import WebDriverException
from driver import Driver


def cheapflights(link):
    # url = f"https://www.cheapflights.com.au/flight-search/{}/{}/2021-11-18?sort=bestflight_a"
    dr = Driver()
    result = []
    try:
        try:
            dr.driver.get(link)
        except:
            dr.quit()
            return "error"
    except WebDriverException as e:
        return str(e)
    time.sleep(10)

    for i in range(2):
        try:
            button = dr.driver.find_element_by_link_text('Show more results')
            button.click()
            print('click')
            time.sleep(10)
        except:
            break

    try:
        items = dr.driver.find_elements_by_class_name(
            'Base-Results-HorizonResult ')

        for item in items:
            logo = item.find_element_by_tag_name('img').get_attribute('src')
            price = item.find_element_by_class_name('price-text').text
            hours = item.find_elements_by_class_name('time-pair')
            duration = item.find_element_by_class_name('duration').text
            name = item.find_element_by_class_name('name-only-text').text
            link = item.find_element_by_class_name(
                'Common-Booking-MultiBookProvider').find_element_by_tag_name('a').get_attribute('href')

            result.append({
                'logo': logo,
                'hours': hours[0].text + "-" + hours[1].text,
                'price': price,
                'duration': duration,
                'name': name,
                'link': link
            })
    except:
        dr.quit()
        return 'Could not get data'
    print(len(result))
    dr.quit()

    return dict(result=result)
