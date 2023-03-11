import os
import sys
import requests
import deepl
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from dotenv import load_dotenv

# https://github.com/matthewwithanm/python-markdownify

# env variable
load_dotenv('.env')
deepl_api_key = os.environ.get("deepl_api_key")
selector = os.environ.get('selector')

# script arguments
url = sys.argv[1]
article_number = sys.argv[2]
article_type = sys.argv[3]

# prepare file path
out_file= str(article_number) + '_' + article_type + '.md'
out_path = '/root/opt/data/' + out_file
if os.path.isfile(out_path):
    os.remove(out_path)

def translate(text):
    translator = deepl.Translator(deepl_api_key)
    result = translator.translate_text(text, target_lang="JA", tag_handling = "html")
    return result.text

def fetch_web_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    response = requests.get(url, timeout=10, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = str(soup.select('h1'))

    for elm in soup.select(selector):
        # inner_html = elm.decode_contents(formatter="html")
        result = result + '\n\n' + str(elm)
    return result

#
# main
#

r = md(translate(fetch_web_page(url)))
# r = md(fetch_web_page(url))

with open(out_path, 'w') as f:
    f.write(r)
    f.write('\n\n')
    f.close()
