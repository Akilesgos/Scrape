import requests
import json
#   from requests_oauthlib import OAuth2Session, OAuth2


client_id = '1dhMYD2pJ19vPvADcpJe7A'
client_secret = 'N3nPYOYtCHiucJFexB4CVp5PEPnl3Q6yc1iML0N8jVW5sl6dgg4SoyHSxC7mwdeZ'
headers = {
    'Authorization': 'Bearer GetD22Tx2J_6UKTn9cH-fUb4H_pOnFhtTdVr70sFGHbJbljOSvofBrcO88AczD4r3Tbz_GoWr73XztO9vdMtqM4oAJkIPRDtJ-_8n3-HRaEKAFzM7b-qpbrvn9CNWnYx'}
url = 'https://api.yelp.com/v3/businesses/search'
redirect_uri = url
params = {'terms': 'food',
          'location': 'Newpot beach'}

r = requests.get(url, headers=headers, params=params)
print(r.text)
# oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
r = requests.get(url, headers=headers, params=params)
print(r.text)


def do_search(terms='food', location='Newpot beach'):
    url = 'https://api.yelp.com/v3/businesses/search'
    #  terms = terms.replace(' ','+')
    #  location=location.replace(' ', '+')
    #  final_url = '{base_url}?term={terms}&location={location}'.format(
    #  base_url=base_url,terms=terms,location=location)
    #  how with replace and cut we could do big url
    headers = {
        'Authorization': 'Bearer GetD22Tx2J_6UKTn9cH-fUb4H_pOnFhtTdVr70sFGHbJbljOSvofBrcO88AczD4r3Tbz_GoWr73XztO9vdMtqM4oAJkIPRDtJ-_8n3-HRaEKAFzM7b-qpbrvn9CNWnYx'}
    params = {'terms': terms,
              'location': location}
    r = requests.get(url, headers=headers, params=params)
    return r.json()  # we read data with json


search_1 = do_search()

print(search_1)  # take data with going through json
for i in search_1['businesses']:
    print(i["name"])
    print(i["phone"])
    print(i["location"]["display_address"])
    print(i["location"]["city"])
    print(search_1.get('image_url'))
