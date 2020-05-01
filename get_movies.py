import requests
import subprocess
import json
import ast

r = requests.get('https://mubi.com/showing').text

r = r.split('</script><script nomodule="" src="/_next/', 2)[0].split('script id="__NEXT_DATA__" type="application/json">', 2)[1]
d = json.loads(r)
m = d['props']['initialState']['filmProgramming']['filmProgrammingsByChannel']['0']

movies = []
movie_list = {}

for movie in range(0, len(m)):
    movies.append(m[movie]['film'])


for movie in range(0,len(movies)):
    movie_list[movie] = {}
    movie_list[movie]['title'] = movies[movie]['title']
    movie_list[movie]['director'] = movies[movie]['directors']
    movie_list[movie]['plot'] = movies[movie]['short_synopsis']
    movie_list[movie]['year'] = str(movies[movie]['year'])
    movie_list[movie]['country'] = movies[movie]['country']

    print('####################################################')
    print(' ')
    print('title: ' + movie_list[movie]['title'])
    print('director: ' + movie_list[movie]['director'])
    print('plot: ' + movie_list[movie]['plot'])
    print('year: ' + movie_list[movie]['year'])
    print('country: ' + movie_list[movie]['country'])
    print('----------------------------------------------------')

    try:
        title = movie_list[movie]['title']
        year = movie_list[movie]['year']

        print(title)
        print(year)
        title = title.replace("'", "")

        torrent = subprocess.check_output(['python2.7', 'torrent-hound.py','-q', title + ' ' + year]).decode()
        torrent = ast.literal_eval(torrent)

        movie_list[movie]['magnetlink'] = torrent['sky']['results']['0']['magnet']
        movie_list[movie]['magnetlinktitle'] = torrent['sky']['results']['0']['name'] + ' ratio: ' + torrent['sky']['results']['0']['ratio'] + ' seeders: '+ torrent['sky']['results']['0']['seeders']
        print('magnetlinktitle: '+ movie_list[movie]['magnetlinktitle'])
        print('magnetlink: \n'+ movie_list[movie]['magnetlink'])
    except Exception as e:
        print(e)
        movie_list[movie]['magnetlink'] = 'N/A'
        movie_list[movie]['magnetlinktitle'] = 'N/A'
        print('magnetlinktitle: '+ movie_list[movie]['magnetlinktitle'])
        print('magnetlink: '+ movie_list[movie]['magnetlink'])
        print('####################################################')

with open('movie_list.json','w') as f:
    json.dump(movie_list, f, indent=4, sort_keys=False)
