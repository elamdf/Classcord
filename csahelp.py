import requests
import urllib.parse
def get_stackoverflow(query):
    query = requests.get("https://api.stackexchange.com/2.2/search/advanced?order=desc&sort=relevance&title=" + urllib.parse.quote(query) + "&site=stackoverflow")
    answers = query.json()
    final = []
    num = 0
    for i in answers["items"]:
        num += 1
        final.append([urllib.parse.unquote(i["title"]),urllib.parse.unquote(i["link"]) ])
        if num == 3:
            break
    return final
#print(get_stackoverflow("importError: cannot import name 'urlencode' when trying to install flask.ext.storage"))