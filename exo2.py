import requests

def main():
    response = requests.get('https://opendomesday.org/api/1.0/county/dby')
    county = response.json()
    places = county['places_in_county']
    return places

if __name__ == '__main__':
    main()

