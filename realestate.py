import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def realstate(link):
    try:
        software_names = [SoftwareName.FIREFOX.value]
        operating_systems = [OperatingSystem.WINDOWS.value]

        user_agent_rotator = UserAgent(
            software_names=software_names, operating_systems=operating_systems, limit=100)

        desired = webdriver.DesiredCapabilities.FIREFOX

        user_agent = user_agent_rotator.get_random_user_agent()
        firefox_options = Options()
        # firefox_options.add_argument('--headless')
        firefox_options.add_argument('--window-size=1420,1080')
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument(f'user-agent={user_agent}')
        # firefox_options.add_argument("--disable-blink-features")
        # firefox_options.add_argument(
        #     '--disable-blink-features=AutomationControlled')
        # firefox_options.add_argument('--enable-automation')

        PROXY = '169.57.1.85:80'
        ip = '167.99.80.139'
        port = 1080

        profile = FirefoxProfile()
        profile.set_preference('network.proxy.type', 1)
        profile.set_preference('network.proxy.http', ip)
        profile.set_preference('network.proxy.http_port', port)
        # Step 5: Set up various protocols to share the agent
        profile.set_preference('network.proxy.share_proxy_settings', True)
        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference('useAutomationExtension', False)

        # profile.set_preference('network.proxy.autodetect', False)
        # profile.set_preference('devtools.jsonview.enabled', False)

        profile.update_preferences()

        # browser = webdriver.Firefox(options=firefox_options,
        #                             desired_capabilities=capabilities)  # to toggle proxy
        browser = webdriver.Firefox(
            firefox_profile=profile, options=firefox_options, desired_capabilities=desired)
        browser.command_executor("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
        })
        # browser = webdriver.Firefox(options=firefox_options)
        browser.get(link)
        # browser.get('http://lumtest.com/myip.json')

        result = []
        # try:
        #     WebDriverWait(browser, 10).until(
        #         EC.presence_of_element_located((By.TAG_NAME, "article")))
        # finally:
        #     browser.maximize_window()
        #     page_html = browser.page_source
        #     browser.close()
        #     # items = browser.find_elements_by_tag_name(
        #     #     'article')
        #     print(page_html)

        # driver.quit()

    except(TimeoutException, WebDriverException):
        print('error')

    # All requests will now use 'some_referer' for the referer


realstate('https://www.realestate.com.au/buy/in-melbourne,+vic+3000/list-1')
