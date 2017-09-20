
import urllib.parse
import sys
import requests

if __name__ == '__main__':

    ip = '127.0.0.1' # sys.argv[1]
    port = 5000 # sys.argv[2]
    x = 9 # sys.argv[3]
    y = 2 # sys.argv[4]

    params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Accept": "text/plain"}
    request = requests.post('http://' + str(ip) + ':' + str(port) +'/fire?x=' + str(x) + '&y=' + str(y))

    print(request, end= ' ')
    print(request.text)