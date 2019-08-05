from bs4 import BeautifulSoup
import subprocess
import ast
import requests

r = requests.get('https://mubi.com/showing')
soup = BeautifulSoup(r.text,'html.parser')
#htmldoc = open('showing.html','r').read()
#soup = BeautifulSoup(htmldoc,'html.parser')

movies = soup.findAll("article",{"class": "full-width-tile full-width-tile--now-showing"})

movie_list = {}

spans_yearcountry = soup.find_all("span", {"class": "now-showing-tile-director-year__year-country light-on-dark"})

for movie in range(0,len(movies)):
    movie_list[movie] = {}
    movie_list[movie]['title'] = movies[movie].h2.text
    movie_list[movie]['director'] = movies[movie].find('span', {'class': 'riforma-header'}).text
    movie_list[movie]['plot'] = movies[movie].p.text
    yearcountry = movies[movie].find("span", {"class": "now-showing-tile-director-year__year-country light-on-dark"}).text
    movie_list[movie]['year'] = (yearcountry).split(', ',2)[1]
    movie_list[movie]['country'] = (yearcountry).split(', ',2)[0]
    movie_list[movie]['poster'] = (movies[movie].a.get('data-film-still-url'))
    
    print('####################################################')
    print(' ')
    print('title: ' + movie_list[movie]['title'])
    print('director: ' + movie_list[movie]['director'])
    print('plot: ' + movie_list[movie]['plot'])
    print('year: ' + movie_list[movie]['year'])
    print('country: ' + movie_list[movie]['country'])
    print('poster: ' + movie_list[movie]['poster'])
    
    print('----------------------------------------------------')
    torrent = subprocess.check_output(['torrent-hound','-q',str(movie_list[movie]['title']) + ' ' + movie_list[movie]['year']]).decode()
    try: 
        torrent = subprocess.check_output(['torrent-hound','-q',str(movie_list[movie]['title']) + ' ' + movie_list[movie]['year']]).decode()
        torrent = ast.literal_eval(torrent)

        movie_list[movie]['magnetlink'] = torrent['sky']['results']['0']['magnet']
        movie_list[movie]['magnetlinktitle'] = torrent['sky']['results']['0']['name'] + ' ratio: ' + torrent['sky']['results']['0']['ratio'] + ' seeders: '+ torrent['sky']['results']['0']['seeders']
        print('magnetlinktitle: '+ movie_list[movie]['magnetlinktitle'])
        print('magnetlink: \n'+ movie_list[movie]['magnetlink'])
    except:
        movie_list[movie]['magnetlink'] = 'N/A'
        movie_list[movie]['magnetlinktitle'] = 'N/A'
        print('magnetlinktitle: '+ movie_list[movie]['magnetlinktitle'])
        print('magnetlink: '+ movie_list[movie]['magnetlink'])
    
    print('----------------------------------------------------')
    print('####################################################')
    print(' ')
