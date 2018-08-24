# google-music-playlist-organizer-script
A short Python script for helping me organize some of my music.

I had a (small) problem. I had a playlist with all of my favorite songs (around 60 of them), which I would listen to over the course of the day (while driving, or at work, or on the train, etc). However, half of the songs are of one style, while some are of another style. And sometimes I would be in the mood to listen to songs of onlyone genre over the other. But it would be annoying to have to keep track of which songs from my "favorites" playlist I have already added to a "genre A" or "genre B" playlist, especially since I add songs to my "favories" playlist all the time, and I don't want to then bother with locating the new songs, and adding them to the right playlist. That's why I'm writing this script. 

Whenever this script is run, it will find all the songs in my "favorites" playlist not in my "genre A" nor "genre B" playlist. It will create a new "uncategorized" playlist containing those songs (any songs previously in the "uncategorized" playlist will be removed). This will allow me to simply go through the "uncategorized" playlist at any time convenient for me, and categorize my songs as I see fit.

I haven't quite finished yet, but hope to soon. 

This script utilizes the `gmusicapi`, an unofficial Google Music client library, which can be found in [this](https://github.com/simon-weber/gmusicapi) repository. 

The only requirement to run this script is a valid installation of Python (the `gmusicapi` documentation specifies the versions of Python that are compatible with the library), and the `gmusicapi` library, which can be installed using `pip install gmusicapi`, as specified in the library's docs. I am using `Python 3.6.4`, and I have added my dependencies in a `requirements.txt` file for easy installation. 
