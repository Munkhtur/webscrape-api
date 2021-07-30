import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
import os

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference(
    'dom.ipc.plugins.enabled.libflashplayer.so', 'false')
firefox_profile.set_preference("network.http.pipelining", True)
firefox_profile.set_preference("network.http.proxy.pipelining", True)
firefox_profile.set_preference("network.http.pipelining.maxrequests", 8)
firefox_profile.set_preference("content.notify.interval", 500000)
firefox_profile.set_preference("content.notify.ontimer", True)
firefox_profile.set_preference("content.switch.threshold", 250000)
# Increase the cache capacity.
firefox_profile.set_preference("browser.cache.memory.capacity", 65536)
firefox_profile.set_preference("browser.startup.homepage", "about:blank")
# Disable reader, we won't need that.
firefox_profile.set_preference("reader.parse-on-load.enabled", False)
firefox_profile.set_preference(
    "browser.pocket.enabled", False)  # Duck pocket too!
firefox_profile.set_preference("loop.enabled", False)
# Text on Toolbar instead of icons
firefox_profile.set_preference("browser.chrome.toolbar_style", 1)
# Don't show thumbnails on not loaded images.
firefox_profile.set_preference(
    "browser.display.show_image_placeholders", False)
# Don't show document colors.
firefox_profile.set_preference(
    "browser.display.use_document_colors", False)
# Don't load document fonts.
firefox_profile.set_preference("browser.display.use_document_fonts", 0)
# Use system colors.
firefox_profile.set_preference("browser.display.use_system_colors", True)
# Autofill on forms disabled.
firefox_profile.set_preference("browser.formfill.enable", False)
# Delete temprorary files.
firefox_profile.set_preference(
    "browser.helperApps.deleteTempFileOnExit", True)
firefox_profile.set_preference("browser.shell.checkDefaultBrowser", False)
firefox_profile.set_preference("browser.startup.homepage", "about:blank")
firefox_profile.set_preference("browser.startup.page", 0)  # blank
# Disable tabs, We won't need that.
firefox_profile.set_preference("browser.tabs.forceHide", True)
# Disable autofill on URL bar.
firefox_profile.set_preference("browser.urlbar.autoFill", False)
# Disable autocomplete on URL bar.
firefox_profile.set_preference(
    "browser.urlbar.autocomplete.enabled", False)
# Disable list of URLs when typing on URL bar.
firefox_profile.set_preference("browser.urlbar.showPopup", False)
# Disable search bar.
firefox_profile.set_preference("browser.urlbar.showSearch", False)
firefox_profile.set_preference(
    "extensions.checkCompatibility", False)  # Addon update disabled
firefox_profile.set_preference("extensions.checkUpdateSecurity", False)
firefox_profile.set_preference(
    "extensions.update.autoUpdateEnabled", False)
firefox_profile.set_preference("extensions.update.enabled", False)
firefox_profile.set_preference("general.startup.browser", False)
firefox_profile.set_preference("plugin.default_plugin_disabled", False)
firefox_profile.set_preference(
    "permissions.default.image", 2)  # Image load disabled again


class Driver:
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(
        options=options, firefox_profile=firefox_profile)

    def quit(self):
        self.driver.quit()
        os.system("taskkill /f /im geckodriver.exe /T")
        os.system("taskkill /f /im firefox.exe /T")
