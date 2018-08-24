from gmusicapi import Mobileclient
import secret


api = Mobileclient()
api.login(secret.USERNAME, secret.PASSWORD, Mobileclient.FROM_MAC_ADDRESS)

playlists = api.get_all_user_playlist_contents()

# Gets the playlists we are working with: The playlist with all the songs, the
# playlist that will hold uncategorized songs, and the playlists for the two
# categories
playlists_to_use = [p for p in playlists if p['name'] in (secret.BIG_PLAYLIST, secret.UNCATEGORIZED, secret.CATEGORY_A, secret.CATEGORY_B)]

# It is valid to assume that the playlist which holds ALL songs already exists
big_playlist = [p for p in playlists_to_use if p['name'] == secret.BIG_PLAYLIST]
big_playlist = big_playlist[0]

uncategorized = [p for p in playlists_to_use if p['name'] == secret.UNCATEGORIZED]
category_a = [p for p in playlists_to_use if p['name'] == secret.CATEGORY_A]
category_b = [p for p in playlists_to_use if p['name'] == secret.CATEGORY_B]

# If "Uncategorized" playlist already exists, we want it empty so we can
# populate it with new uncategorized songs, and the easient way to do that is to
# delete it and recreate it.
if uncategorized:
    playlist_id = uncategorized[0]['id']
    api.delete_playlist(playlist_id)

uncategorized_id = api.create_playlist(secret.UNCATEGORIZED)
playlists = api.get_all_user_playlist_contents()
uncategorized = [p for p in playlists if p['id'] == uncategorized_id]
uncategorized = uncategorized[0]

# If "Category A" playlist does not yet exist, create it
if not category_a:
    category_a_id = api.create_playlist(secret.CATEGORY_A)
    playlists = api.get_all_user_playlist_contents()
    category_a = [p for p in playlists if p['id'] == category_a_id]
category_a = category_a[0]

# If "Category B"playlist does not exist, create it
if not category_b:
    category_b_id = api.create_playlist(secret.CATEGORY_B)
    playlists = api.get_all_user_playlist_contents()
    category_b = [p for p in playlists if p['id'] == category_b_id]
category_b = category_b[0]
