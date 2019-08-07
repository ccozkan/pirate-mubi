# pirate-mubi

This one scrapes movies from the mubi.com now showing page, then looks for magnet links for those and hopefully finds them :D

You'll need to have torrent-hound in your system in order to search for magnet links. 
Install the required packages


```
wget https://raw.githubusercontent.com/baddymaster/torrent-hound/master/torrent-hound.py
pip3 install --user -r requirements.txt
```
Run the command and to get the output 

```
python3 get_movies.py
```

It saves output as json file too. But if you want to go traditional way you can save the output as text file in linux systems.

```
python3 get_movies.py > output.txt
```
Example output looks like this.

<center>
<img src="http://i68.tinypic.com/icl6c1.png" width="700" />
</center>

