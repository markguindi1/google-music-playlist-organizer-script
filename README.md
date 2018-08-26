# google-music-playlist-organizer-script
A short Python script for helping me organize some of my music.

I had a (small) problem. I had a playlist with all of my favorite songs (around 60 of them), which I would listen to over the course of the day (while driving, or at work, or on the train, etc). However, half of the songs are of one style, while some are of another style. And sometimes I would be in the mood to listen to songs of onlyone genre over the other. But it would be annoying to have to keep track of which songs from my "favorites" playlist I have already added to a "genre A" or "genre B" playlist, especially since I add songs to my "favories" playlist all the time, and I don't want to then bother with locating the new songs, and adding them to the right playlist. That's why I'm writing this script. 

Whenever this script is run, it will find all the songs in my "favorites" playlist not in my "genre A" nor "genre B" playlist. It will create a new "uncategorized" playlist containing those songs (any songs previously in the "uncategorized" playlist will be removed). This will allow me to simply go through the "uncategorized" playlist at any time convenient for me, and categorize my songs as I see fit.

This script utilizes the `gmusicapi`, an unofficial Google Music client library, which can be found in [this](https://github.com/simon-weber/gmusicapi) repository. 

The only requirement to run this script is a valid installation of Python (the `gmusicapi` documentation specifies the versions of Python that are compatible with the library), and the `gmusicapi` library, which can be installed using `pip install gmusicapi`, as specified in the library's docs. I am using `Python 3.6.4`, and I have added my dependencies in a `requirements.txt` file for easy installation. 

Place you Google Music username and password in a `secret.py` file. Also put the names of the relevant playlists in that file. The file should look something like this:
```
USERNAME = "your-email@gmail.com"
PASSWORD = "your-password"

BIG_PLAYLIST = "All songs"
UNCATEGORIZED = "Uncategorized"
CATEGORY_A = "Fast songs"
CATEGORY_B = "Slow songs"
```

I created an alias/shortcut to run this script from the command line whenever I want. To create this shortcut, add the following line to your `.bash_profile` (or whatever startup file you like):
```
alias musicorg="workon virtual_env_name && python /path/to/g_music_api_organize_music.py && deactivate"
```
I have decided to call my shortcut `musicorg` (short for "music organize"), but you can call it whatever you want. 

This shortcut contains a few commands. It first activates my Python virtual environment that I created using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), using the `workon` command. Substitute `virtual_env_name` with the name of your virtual environment.

The shortcut then runs the Python script, using the script's full path: `python /path/to/g_music_api_organize_music.py`. Depending on your operating system, or whether you're using a virtual environment or not, you may need to substitute `python` with `python3`. 

The shortcut then deactivates the virtual environment, using the `deactivate` command. 

If you're using a different Python virtual environment tool, substitute the above virtual environment commands with your own. If you're not using a virtual environment, simply running the Python executable is sufficient:
```
alias musicorg="python /path/to/g_music_api_organize_music.py"
```

