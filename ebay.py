import time
from driver import Driver


def ebay(term):
    result = []
    for i in range(1, 3):
        dr = Driver()
        # url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw={term}&_sacat=0&LH_TitleDesc=0&_odkw={term}&_osacat=0"
        url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw={term}&_sacat=9355&LH_TitleDesc=0&_pgn={i}"
        try:
            dr.driver.get(url)
        except:
            dr.quit()
            return "error"
        try:
            time.sleep(10)
            # main = dr.driver.find_element_by_id('mainContent')
            items = dr.driver.find_elements_by_class_name('s-item')

            for item in items:
                try:
                    title = item.find_element_by_class_name(
                        's-item__title').text
                    image = item.find_element_by_tag_name(
                        'img').get_attribute('src')
                    price = item.find_element_by_class_name(
                        's-item__price').text
                    link = item.find_element_by_class_name(
                        's-item__link').get_attribute('href')
                    result.append({
                        'title': title,
                        'image': image,
                        'price': price,
                        'link': link
                    })
                except:
                    pass

        except:
            dr.quit()
            print('no more pages')

    dr.quit()
    print(len(result))
    return dict(result=result)
