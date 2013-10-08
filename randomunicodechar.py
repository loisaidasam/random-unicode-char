
from bs4 import BeautifulSoup
import requests

BLOOPLE_URL = "http://unicode.bloople.net/"


def get_random_unicode_char():
    page_str = requests.get(BLOOPLE_URL).text
    soup = BeautifulSoup(page_str)
    code_point = soup.find(id='code_point').text
    name = soup.find(id='name').text
    return (code_point, name)


if __name__ == '__main__':
    print u"%s (%s)" % get_random_unicode_char()
