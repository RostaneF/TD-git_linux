import requests
import pandas as pd

def get_manor_ids(placeId):
	response = requests.get('https://opendomesday.org/api/1.0/place/'+placeId)
	data = response.json()
	if 'manors' in data.keys():
		manor_ids = data['manors']
		print(manor_ids) #J'ajoute cette ligne pour avoir un affichage lorsque j'X dans le prompt "python3 exo3.py"
		return manor_ids
	else:
		return []
def get_all_manors(county):
    res = requests.get('https://opendomesday.org/api/1.0/county/'+county)
    data = res.json()

    manorIds = []
    places = data['places_in_county']
    for place in places:
        manorIds.extend(get_manor_ids(str(place['id'])))
    return manorIds

def get_manors_info(county):
    manorIds = get_all_manors(county)
    df = pd.DataFrame()
    for manor in manorIds:
        res = requests.get("https://opendomesday.org/api/1.0/manor/"+str(manor['id']))
        data = res.json()
        manorInfo = pd.DataFrame({
            "geld": data['geld'],
            "totalploughs": data['totalploughs']
        }, index=[manor['id']])
        df = pd.concat([df, manorInfo])
    return df

if __name__ == "__main__":
	get_manor_ids("1036")

