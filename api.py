from jbscrape import jbhifi
from cheapflights import cheapflights
from ebay import ebay
from target import target
from chemist import chemist
from flask import Flask, request
import validators
import atexit
import os


app = Flask(__name__)


@app.route('/jbhifi', methods=['GET'])
def search_jbhifi():
    query = request.args.get('q')
    if not query:
        return 'Search term missing.'
    print(f"Scraping jbhifi.com for {query}....")
    result = jbhifi(query)
    return result


@app.route('/cheapflights', methods=['GET'])
def search_flight():
    if not request.args.get('url'):
        return 'Example: 0.0.0.0/cheapflights?url=your url'
    url = request.args.get('url')
    if not validators.url(url):
        return "Not a valid url."
    print("Scraping cheapflights.com....")
    result = cheapflights(url)
    return result


@app.route('/ebay', methods=['GET'])
def search_ebay():
    query = request.args.get('q')
    if not query:
        return 'Search term missing.'
    print("Scraping ebay.com....")
    result = ebay(query)
    return result


@app.route('/target', methods=['GET'])
def search_target():
    query = request.args.get('q')
    if not query:
        return 'Search term missing.'
    print(f"Scraping info for {query} from target.com....")
    result = target(query)
    return result


@app.route('/chemist', methods=['GET'])
def search_chemist():
    query = request.args.get('q')
    if not query:
        return 'Search term missing.'
    print(f"Scraping info for {query} from chemistwarehouse.com.au...")
    result = chemist(query)
    return result


def OnExitApp(user):
    os.system("taskkill /f /im geckodriver.exe /T")
    os.system("taskkill /f /im firefox.exe /T")
    print(user, " exit Flask application")


atexit.register(OnExitApp, user='ScrapeApi')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True,)
