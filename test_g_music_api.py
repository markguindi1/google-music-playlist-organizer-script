from gmusicapi import Mobileclient
import secret
#print(gmusicapi.__file__)

#print(username)
#print(pswd)
#def main():
api = Mobileclient()
api.login(secret.USERNAME, secret.PASSWORD, Mobileclient.FROM_MAC_ADDRESS)
# logged_in = api.login(secret.USERNAME, secret.PASSWORD, Mobileclient.FROM_MAC_ADDRESS)
# logged_in is True if login was successful

# playlists = api.get_all_playlists()
# names = [playlist['name'] for playlist in playlists]
# print(names)

playlists = api.get_all_user_playlist_contents()

playlists_to_use = [p for p in playlists if p['name'] in (secret.BIG_PLAYLIST, secret.UNCATEGORIZED, secret.CATEGORY_A, secret.CATEGORY_B)]

big_playlist = [p for p in playlists_to_use if p['name'] == secret.BIG_PLAYLIST][0]
uncategorized = [p for p in playlists_to_use if p['name'] == secret.UNCATEGORIZED]
category_a = [p for p in playlists_to_use if p['name'] == secret.CATEGORY_A]
category_b = [p for p in playlists_to_use if p['name'] == secret.CATEGORY_B]

if uncategorized:
    playlist_id = uncategorized[0]['id']
    api.delete_playlist(playlist_id)

category_a = api.create_playlist(secret.CATEGORY_A)
category_b = api.create_playlist(secret.CATEGORY_B)






#main()
