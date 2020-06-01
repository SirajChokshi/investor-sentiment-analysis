import http.client
import json

def stockPrice(symbol):
    conn = http.client.HTTPSConnection("apidojo-yahoo-finance-v1.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "8c5526adc2msh39597ddd562bfbbp123143jsn6a803ee93095"
        }

    url = "/stock/v2/get-chart?interval=5m&region=US&symbol="+symbol+"&lang=en&range=1d"

    conn.request("GET", url, headers=headers)

    res = conn.getresponse()
    string = res.read().decode("utf-8")
    json_obj = json.loads(string)
    data = json_obj['chart']['result'][0]['meta']

    print(data['symbol'])
    print(data['previousClose'])


# Examples
stockPrice("TSLA")
stockPrice("AAPL")
stockPrice("ZM")
