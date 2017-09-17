
import http.client, urllib.parse
import http.server
import requests

if __name__ == '__main__':
    localServer = http.client.HTTPConnection('127.0.0.1', 8080)
    remoteServer = http.client.HTTPConnection('127.0.0.1', 8081)
    #remoteServer.connect()
    #remoteServer.auto_open();
    # #------------------------------------------------
    # remoteServer.request("POST", "fire", "4,5");
    # localServer.auto_open();
    # localServer.request("POST", "fire", "4,5");

    # remoteServer.request("GET", "")

    params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Accept": "text/plain"}
    requests.post('http://127.0.0.1:8081/fire?x=4&y=5')
    #remoteServer.request("POST", "fire?x=4&y=5&x=4", params, headers)
    #remoteResponse = remoteServer.getresponse()
    #localResponse = localServer.getresponse()

    #remoteData = remoteResponse.read()
    #print(remoteDa