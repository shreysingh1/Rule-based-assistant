import urllib.request
import wikipedia


def internet_conn():
    try:
        urllib.request.urlopen('http://google.com')  # Python 3.x
        return True
    except:
        return False


def check_on_internet(query):
    query = query.lower()
    query = query.replace('who is', "")
    query = query.replace('what is', "")
    query = query.replace('do you know', "")
    query = query.replace('can you tell me', "")
    query = query.replace("tell me about", "")

    query = query.strip()

    try:
        result = wikipedia.summary(query, sentences=2, auto_suggest=False, redirect=True)
        return str(result)
    except Exception as e:
        return ""
