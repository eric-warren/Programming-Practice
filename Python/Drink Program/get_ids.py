import requests
import json

base_api = "https://www.thecocktaildb.com/api/json/v1/1/"



ids = []
for x in range(10000):
    req = json.loads(requests.get(base_api + "lookup.php?i=" +  str(x + 10000)).text)
    print(str(x) + '   ' + str(req))
    if str(req) != "{'drinks': None}":
        req = req['drinks']
        req = req[0]
        ids.append(req['idDrink'])
    
   # print(req['strDrink'])
with open('ids.txt', 'w') as f:
    for item in ids:
        f.write("%s\n" % item)

