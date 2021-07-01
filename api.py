from jbscrape import jbhifi
from cheapflights import cheapflights
from flask import Flask, request


app = Flask(__name__)


def get_jbhifi_result(url):
    result = jbhifi(url)
    return result


@app.route('/', methods=['GET'])
def search_api():
    url = request.args.get('url')
    if 'cheapflights' in url:
        print("Scraping cheapflights.com....")
        result = cheapflights(url)
    else:
        print("Scraping jbhifi.com....")
        result = jbhifi(url)
    return dict(result=result)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
