# pirate-mubi

Arr! This one scrapes movies from the mubi.com now showing page, then looks for magnet links for those and hopefully finds them :D

You'll need to have torrent-hound in your system in order to search for magnet links. 


```
git clone https://github.com/ozkc/pirate-mubi
cd pirate-mubi/

curl https://raw.githubusercontent.com/baddymaster/torrent-hound/master/torrent-hound.py > torrent-hound.py
curl https://raw.githubusercontent.com/baddymaster/torrent-hound/master/requirements >> requirements

pip3 install --user -r requirements.txt
```
Run the command and to get the output 

```
python3 get_movies.py
```

It saves output as a json file too.

Example output looks like this.

<center>
<img src="https://raw.githubusercontent.com/ozkc/pirate-mubi/master/screenshot.png" width="700" />
</center>

