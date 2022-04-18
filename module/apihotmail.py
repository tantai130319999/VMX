def getapicodever(keyapi,userm,passm):
    for a in range(0, 10):
        url = 'https://fbvip.org/api/ordercode.php?apiKey='+ keyapi +'&type=1&user=' + userm + '&pass=' passm
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(url, headers=headers)
        json = result.content.decode()
        json = json[json.find('http://'):json.find('}') - 1]
        print(json)
        sleep(5)
        result2 = requests.get(json, headers=headers)
        json2 = result2.content.decode()
        if json2[11:12] == "1":
            break
    if json2[11:12] == "1":
        codever = json2[json2.find('code') + 7:json2.find('code') + 13]
    return codever