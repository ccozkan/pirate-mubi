# pirate-mubi

this one scrapes movies from the mubi.com now showing page, then looks for magnet links for those and hopefully finds them :D

you'll need to have torrent-hound in your system in order to search for magnet links.

Install the required packages

```
pip2 install --user torrent-hound
pip3 install --user -r requirements.txt
```
Run the command and to get the output 

```
python3 getMovies.py
```

Also for later use you can save the output as text file in linux systems.

```
python3 getMovies.py > output.txt
```
Example output looks like this.

<center>
<img src="http://i68.tinypic.com/icl6c1.png" width="700" />
</center>
