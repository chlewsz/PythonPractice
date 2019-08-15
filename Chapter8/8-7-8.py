def make_album(singer_name, album_name, num=0):
    album = {
        'singer_name': singer_name,
        'album_name': album_name
    }
    if num != 0:
        album['num'] = num
    return album

while True:
    print("(enter 'q' at any time to quit)")

    singer_name = input('singer name: ')
    if singer_name == 'q':
        break
    
    album_name = input('album name: ')
    if album_name == 'q':
        break

    album = make_album(singer_name, album_name)
    print(album)
