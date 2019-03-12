import requests
import json
import csv



# the function that gets the api url
def get_api(func, wildcard):
    #url for the api minus varible parts
    base_api = "https://www.thecocktaildb.com/api/json/v1/1/"
    api = ''
    #check what function is to be performed and create full api url
    if func.lower() == 'search':
        api = base_api + "search.php?s=" + wildcard
    elif func.lower() == 'lookup':
        api = base_api + 'lookup.php?i=' + wildcard
    else:
        print("invaild function to perform")
    return api


#the function that takes the ids and writes to the csv file
def get_json(ids):
    #list for storing dictionaries of json data
    temp = []
    #get all the json data for drinks from the api
    for x in range(len(ids)):
        url = get_api('lookup', ids[x])
        print(url)
        req = json.loads(requests.get(url).text)

        #checking if the drink exists then removing the chinese charaters
        if str(req) != "{'drinks': None}":
            req = req['drinks']
            req = req[0]
            del req['strDrinkZH-HANT']
            del req['strDrinkZH-HANS']
            temp.append(req)
    #writing the json data to a csv file
    myFile = open('resources/test.csv', 'w')
    with myFile:
        myFields = ['idDrink', 'strDrink', 'strDrinkES', 'strDrinkDE', 'strDrinkFR', 'strVideo', 'strCategory', 'strIBA', 'strAlcoholic', 'strGlass', 'strInstructions', 'strInstructionsES', 'strInstructionsDE', 'strInstructionsFR', 'strInstructionsZH-HANS', 'strInstructionsZH-HANT', 'strDrinkThumb', 'strIngredient1', 'strIngredient2', 'strIngredient3', 'strIngredient4', 'strIngredient5', 'strIngredient6', 'strIngredient7', 'strIngredient8', 'strIngredient9', 'strIngredient10', 'strIngredient11', 'strIngredient12', 'strIngredient13', 'strIngredient14', 'strIngredient15', 'strMeasure1', 'strMeasure2', 'strMeasure3', 'strMeasure4', 'strMeasure5', 'strMeasure6', 'strMeasure7', 'strMeasure8', 'strMeasure9', 'strMeasure10', 'strMeasure11', 'strMeasure12', 'strMeasure13', 'strMeasure14', 'strMeasure15', 'dateModified']
        writer = csv.DictWriter(myFile, fieldnames=myFields)
        writer.writeheader()
        writer.writerows(temp)
    return

# currently the function to call to update the csv file
def update_json():
    #variable to hold all the ids of the drinks
    ids = []
    file = open('resources/ids.txt','r')
    #read lines in the id text file
    for x, line in enumerate(file):
        temp = file.readline(5)
        #making sure not to add non ids to the list
        if temp != '\n' or '':
            ids.append(temp)
    get_json(ids)
    return
update_json()
