import requests

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

def get_data():
    
    r = requests.get(url)
    data = r.json()
    return data


if __name__ == '__main__':
    
    get_data()