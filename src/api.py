import requests

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

def get_data():
    
    r = requests.get(url)
    data = r.json()
    return data

def get_team(team):
    
    r = requests.get(url)
    data = r.json()
    for t in data['teams']:
        if (t['name'] == team) or (t['name'].lower() == team):
            data = t
    return data


if __name__ == '__main__':
    
    get_data()