
import http.client, urllib.parse
import http.server
import requests

if __name__ == '__main__':

    ip = '127.0.0.1'
    port = 5000

    localServer = http.client.HTTPConnection('127.0.0.1', 5000)
    remoteServer = http.client.HTTPConnection(ip, 5000)
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
    request = requests.post('http://' + ip + ':' + str(port) +'/fire?x=4&y=5')
    print(request.text)
    #remoteServer.request("POST", "fire?x=4&y=5&x=4", params, headers)
    #remoteResponse = remoteServer.getresponse()
    #localResponse = localServer.getresponse()

    #remoteData = remoteResponse.read()
    #print(remoteDa