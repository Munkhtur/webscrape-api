import time
from selenium.common.exceptions import NoSuchElementException
from driver import Driver

result = []
dr = Driver()


def scrapeCategory():
    print('category')
    items = dr.driver.find_elements_by_class_name('category-product')
    for item in items:
        link = item.get_attribute('href')
        image = item.find_element_by_tag_name('img').get_attribute('src')
        title = item.find_element_by_class_name('product__title').text
        price = item.find_element_by_class_name('product__price-current').text
        result.append({
            'title': title,
            'image': image,
            'price': price,
            'link': link
        })


def scrapeNonCategory():
    print('noncategory')
    items = dr.driver.find_elements_by_class_name('search__result__product')
    for item in items:
        link = item.find_element_by_tag_name('a').get_attribute('href')
        image = item.find_element_by_tag_name('img').get_attribute('src')
        title = item.find_element_by_class_name(
            'search__result__product__name').text
        price = item.find_element_by_class_name(
            'search__result__product__price').text

        result.append({
            'title': title,
            'image': image,
            'price': price,
            'link': link
        })


def chemist(term):
    # url = f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw={term}&_sacat=0&LH_TitleDesc=0&_odkw={term}&_osacat=0"
    url = f"https://www.chemistwarehouse.com.au/search?searchtext={term}&fh=1"

    try:
        dr.driver.get(url)
    except:
        dr.quit()
        return "error"

    try:
        time.sleep(10)
        dr.driver.find_element_by_class_name('search__result__product__list')
        scrapeNonCategory()
        i = 2
        while True:
            try:
                dr.driver.find_element_by_xpath(
                    f'//button[normalize-space()="{i}"]').click()
                print(f'click {i}')
                time.sleep(5)
                scrapeNonCategory()
                i += 1
            except:
                break
    except:
        try:
            dr.driver.find_element_by_class_name('category-product-grid')
            scrapeCategory()
            i = 2
            while True:
                try:
                    dr.driver.find_element_by_xpath(
                        f'//button[normalize-space()="{i}"]').click()
                    print(f'click {i}')

                    time.sleep(5)
                    scrapeCategory()
                    i += 1
                except:
                    break
        except NoSuchElementException as e:
            dr.quit()
            return str(e)

    dr.quit()
    print(len(result))
    return dict(result=result)
