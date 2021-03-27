import requests
import json
import keys
# print(keys.keys.accuKey)
def exec(lat,lng):
    try:
        url='http://api.apixu.com/v1/forecast.json?key='+keys.keys.accuKey+'&q='+str(lat)+','+str(lng)+'&days=10'
        print(url)
        locDetais=json.loads(requests.get(url).text)
        prep=0
        tmp=0
        k=0
        for i in locDetais["forecast"]["forecastday"]:
            prep=prep+(i["day"]["totalprecip_mm"])
            tmp=tmp+(i["day"]["avgtemp_c"])
            print(i["day"]["avgtemp_c"],tmp)
            k=k+1
        print(prep,k)
        return [(prep/k)*30,(tmp/k)]
    except:
        return 0

# exec(12.9745083,79.1572194)