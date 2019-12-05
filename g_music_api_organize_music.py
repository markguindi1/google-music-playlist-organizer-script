from gmusicapi import Mobileclient
# secret.py contains sensitive information, as well as the names of the
# playlists the script will be working with. The names should be self-explanatory:
# secret.BIG_PLAYLIST
# secret.UNCATEGORIZED
# secret.CATEGORY_A
# secret.CATEGORY_B
import secret


api = Mobileclient()
api.login(secret.USERNAME, secret.PASSWORD, Mobileclient.FROM_MAC_ADDRESS)
print("Logged in as", secret.USERNAME)

print("Getting playlist data...")
playlists = api.get_all_playlists()

# Gets the playlists we are working with: The playlist with all the songs, the
# playlist that will hold uncategorized songs, and the playlists for the two
# categories
# It is valid to assume that the playlist which holds ALL songs already exists
big_playlist = [p for p in playlists if p['name'] == secret.BIG_PLAYLIST][0]
uncategorized_lst = [p for p in playlists if p['name'] == secret.UNCATEGORIZED]
category_a_lst = [p for p in playlists if p['name'] == secret.CATEGORY_A]
category_b_lst = [p for p in playlists if p['name'] == secret.CATEGORY_B]

# If "Uncategorized" playlist already exists, remove all songs from it.
# Otherwise create the playlist.
if uncategorized_lst:
    uncategorized_playlist = uncategorized_lst[0]
    if 'tracks' in uncategorized_playlist:
        old_uncategorized_songs_set = {song['id'] for song in uncategorized_playlist['tracks']}
        old_uncategorized_songs_lst = list(old_uncategorized_songs_set)
        api.remove_entries_from_playlist(old_uncategorized_songs_lst)
        print("Cleared all songs from uncategorized playlist named", secret.UNCATEGORIZED)
else:
    api.create_playlist(secret.UNCATEGORIZED)
    print("Created playlist for uncategorized songs, named", secret.UNCATEGORIZED)

# If "Category A"playlist does not exist, create it
if not category_a_lst:
    api.create_playlist(secret.CATEGORY_A)
    print("Created playlist named",  secret.CATEGORY_A)

# If "Category B"playlist does not exist, create it
if not category_b_lst:
    api.create_playlist(secret.CATEGORY_B)
    print("Created playlist named",  secret.CATEGORY_B)

print("Finding uncategorized songs...")
playlists = api.get_all_user_playlist_contents()
playlists_to_use = [p for p in playlists if p['name'] in (secret.BIG_PLAYLIST, secret.UNCATEGORIZED, secret.CATEGORY_A, secret.CATEGORY_B)]
big_playlist = [p for p in playlists_to_use if p['name'] == secret.BIG_PLAYLIST][0]
uncategorized = [p for p in playlists_to_use if p['name'] == secret.UNCATEGORIZED][0]
category_a = [p for p in playlists_to_use if p['name'] == secret.CATEGORY_A][0]
category_b = [p for p in playlists_to_use if p['name'] == secret.CATEGORY_B][0]

# Create sets of song ids
all_songs_set = {song['trackId'] for song in big_playlist['tracks']}
cat_a_songs = {song['trackId'] for song in category_a['tracks']}
cat_b_songs = {song['trackId'] for song in category_b['tracks']}

# Set of all categorized songs
categorized_songs = cat_a_songs | cat_b_songs
uncategorized_songs = all_songs_set - categorized_songs
uncategorized_songs = list(uncategorized_songs)

# Add songs to playlist
uncategorized_id = uncategorized['id']

print("Adding uncategorized songs to playlist named",  secret.UNCATEGORIZED)
api.add_songs_to_playlist(uncategorized_id, uncategorized_songs)
print("Success! Added", len(uncategorized_songs), "songs to playlist named", secret.UNCATEGORIZED)
api.logout()
print("Logged out")
