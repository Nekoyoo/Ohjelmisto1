import requests
#import json

hakusana = input('Anna hakusana: ')

pyyntö = 'https://api.tvmaze.com/search/shows?q=' + hakusana

try:
    vastaus = requests.get(pyyntö)
    if not vastaus.ok:
        print('jokin meni pieleen')
except Exception as e:
    print('haussa tapahtui virhe')

print('toimii')



#sarjat = requests.get(pyyntö).json()

#for sarja in sarjat:
    #print(sarja['show']['name'])
#print(vastaus[0]['show']['name']) ensimmäinen alkio
#print(json.dumps(vastaus, indent=2)) koko roska paremmassa muodossa