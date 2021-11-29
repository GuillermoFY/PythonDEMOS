import requests

print("--- GETTING THE DATA FROM THE NETWORK ---")
print("Please wait...")

#Setting the query by the command line
specie = input("Text a specie (With the first capital letter): ")
query = {"species":specie}

#Getting the number of pages of the characters
dataForPages = requests.get("https://rickandmortyapi.com/api/character",query)
dataJForPages = dataForPages.json() #Now, we make the json
elementsInInfo =  dataJForPages["info"] #from the json we get the element info
nPages = int(elementsInInfo["pages"]) #inside info, there is an element called pages that contains the page number

print("")

total = 0
for i in range((nPages+1)):
    #This is why we want the number of pages, to change the url by the pages
    URL = ""
    if i == 0:
        URL = "https://rickandmortyapi.com/api/character"
    else:
        URL = "https://rickandmortyapi.com/api/character?page=" + str(i)
    
    data = requests.get(URL)

    dataJ = data.json() #get the json of the requested url

    for element in dataJ["results"]:
        if element["species"] == specie:
            print("Name: " + element["name"] + ", specie: " + element["species"] + "\n")
            total+=1

print("\n Total: " + str(total))