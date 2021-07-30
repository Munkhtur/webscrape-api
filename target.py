import time
from driver import Driver


def target(term):
    # url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw={term}&_sacat=0&LH_TitleDesc=0&_odkw={term}&_osacat=0"
    url = f"https://www.target.com.au/search?text={term}&sEngine=c"
    dr = Driver()
    try:
        dr.driver.get(url)
    except:
        dr.quit()
        return "error"
    result = []
    try:

        time.sleep(10)
        total_height = int(dr.driver.execute_script(
            "return document.body.scrollHeight"))
        for i in range(1, total_height, 500):
            dr.driver.execute_script("window.scrollTo(0, {});".format(i))
        main = dr.driver.find_element_by_tag_name('main')
        items = main.find_elements_by_class_name('product')
        # images = dr.driver.find_elements_by_xpath(
        #     "//li[contains(@class, 'product')]//img[@src]")

        # for i in images:
        #     attrs = dr.driver.execute_script(
        #         'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', i)
        #     print(attrs)
        for i, item in enumerate(items):
            try:

                title = item.find_element_by_class_name('name-heading').text
                image = item.find_element_by_tag_name(
                    "img").get_attribute('src')
                price = item.find_element_by_class_name('price-regular').text
                link = item.find_element_by_tag_name('a').get_attribute('href')
                result.append({
                    'title': title,
                    # 'image': images[i].get_attribute('src'),
                    'image': image,
                    'price': price,
                    'link': link
                })
            except:
                pass
    except:
        dr.quit()

    dr.quit()
    print(len(result))
    return dict(result=result)
