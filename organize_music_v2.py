from gmusicapi import Mobileclient
# secret.py contains sensitive information, as well as the names of the
# playlists the script will be working with. The names should be self-explanatory:
# secret.BIG_PLAYLIST
# secret.UNCATEGORIZED
# secret.CATEGORY_A
# secret.CATEGORY_B
import secret

def get_ids_set(playlist):
    if 'tracks' not in playlist:
        return set()
    return {track['id'] for track in playlist['tracks']}

def get_trackids_set(playlist):
    if 'tracks' not in playlist:
        return set()
    return {track['trackId'] for track in playlist['tracks']}


api = Mobileclient()
api.login(secret.USERNAME, secret.PASSWORD, Mobileclient.FROM_MAC_ADDRESS)
print("Logged in as", secret.USERNAME)

# Get playlist data
print("Getting playlist data...")
playlists = api.get_all_playlists()
uncategorized_lst = [p for p in playlists if p['name'] == secret.UNCATEGORIZED]
category_a_lst = [p for p in playlists if p['name'] == secret.CATEGORY_A]
category_b_lst = [p for p in playlists if p['name'] == secret.CATEGORY_B]

# If certain playlists don't exist, create them
if not uncategorized_lst:
    api.create_playlist(secret.UNCATEGORIZED)
    print("Created playlist for uncategorized songs, named", secret.UNCATEGORIZED)
if not category_a_lst:
    api.create_playlist(secret.CATEGORY_A)
    print("Created playlist named",  secret.CATEGORY_A)
if not category_b_lst:
    api.create_playlist(secret.CATEGORY_B)
    print("Created playlist named",  secret.CATEGORY_B)

# Finding uncategorized songs
print("Finding uncategorized songs...")
playlists = api.get_all_user_playlist_contents()
big_playlist = [p for p in playlists if p['name'] == secret.BIG_PLAYLIST][0]
uncategorized_playlist = [p for p in playlists if p['name'] == secret.UNCATEGORIZED][0]
category_a_playlist = [p for p in playlists if p['name'] == secret.CATEGORY_A][0]
category_b_playlist = [p for p in playlists if p['name'] == secret.CATEGORY_B][0]

# Splitting up songs by whether they are categorized or not
all_songs_set = get_trackids_set(big_playlist)
cat_a_songs_set = get_trackids_set(category_a_playlist)
cat_b_songs_set = get_trackids_set(category_b_playlist)
all_categorized_songs_set = cat_a_songs_set | cat_b_songs_set
uncategorized_songs_set = all_songs_set - all_categorized_songs_set

# Remove songs from uncategorized that have been categorized already
print("Removing newly categorized songs from the uncategorized playlist named", secret.UNCATEGORIZED)
uncategorized_playlist_songs_set = get_trackids_set(uncategorized_playlist)
already_categorized_songs_set = all_categorized_songs_set & uncategorized_playlist_songs_set
already_categorized_songs_ids = [song['id'] for song in uncategorized_playlist['tracks'] if song['trackId'] in already_categorized_songs_set]
api.remove_entries_from_playlist(already_categorized_songs_ids)
print("Removed", len(already_categorized_songs_ids), "songs from the uncategorized playlist named", secret.UNCATEGORIZED)

# Add songs that are not categorized, to uncategorized
# First, don't re-add songs that are still uncategorized
print("Adding uncategorized songs to playlist named",  secret.UNCATEGORIZED)
newly_uncategorized_songs_set = uncategorized_songs_set - uncategorized_playlist_songs_set
api.add_songs_to_playlist(uncategorized_playlist['id'], list(newly_uncategorized_songs_set))
print("Success! Added", len(newly_uncategorized_songs_set), "songs to playlist named", secret.UNCATEGORIZED)
api.logout()
print("Logged out")





