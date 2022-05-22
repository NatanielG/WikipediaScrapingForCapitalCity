import requests
def capital_city(address) :
    r = requests.get(url=address, auth=('user', 'pass'))
    page = r.text
    relevant = page.split('<th scope="row" class="infobox-label">')
    relevant.pop(0)
    content=relevant[0].split('title="')
    content.pop(0)
    city = content[0].split("\"")
    print(city[0])

co = input("Enter the name of the country which capital city you want to find: ")
ad = 'https://en.wikipedia.org/wiki/{}'.format(co)
capital_city(ad)
