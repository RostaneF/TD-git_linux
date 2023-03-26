import requests

def get_manor_ids(placeId):
	response = requests.get('https://opendomesday.org/api/1.0/place/'+placeId)
	data = response.json()
	if 'manors' in data.keys():
		manor_ids = data['manors']
		print(manor_ids) #J'ajoute cette ligne pour avoir un affichage lorsque j'X dans le prompt "python3 exo3.py"
		return manor_ids
	else:
		return []

if __name__ == "__main__":
	get_manor_ids("1036")

