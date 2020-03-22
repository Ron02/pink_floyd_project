
def get_data ():
    """
    func dividing the data in file to bulding
    :return:the bulding
    """
    data_txt = open("Pink_Floyd_DB.txt" , 'r').read()
    main_dict = {}
    albums_songs = data_txt.split("#")[1:]
    for i in range(len(albums_songs)):
        albums_songs[i] = albums_songs[i].split("*")
        cont = True
        up = 0
        song_and_dil_lst = []
        while (cont):
            up += 1
            try:
                song_and_dil_lst.append({albums_songs[i][up].split("::")[0] : albums_songs[i][up].split("::")[1:]})
            except Exception as e:
                cont = False
        main_dict[tuple(albums_songs[i][0].split("::"))] = song_and_dil_lst
    return main_dict

def get_all_albums ():
    """
    func returning string of all the albums
    :return: string of all the albums
    """
    data = get_data()
    albums = []
    for i in data.keys():
        albums.append(i[0])
    return ','.join(albums)

def get_album_songs(album):
    """
    func getting all songs in album
    :param album:
    :return: all songs
    """
    data = get_data()
    key = ''
    songs = []
    for ky in data.keys():
        if (ky[0].lower() == album.lower()):
            key = ky
    if (key == ''):
        return ("album dosent exist")
    for sng in data[key]:
        songs.append(''.join(list(sng.keys())))
    return ','.join(songs)

def get_song_len (song):
    """
    func getting song lenth
    :param song:
    :return: lenth
    """
    data = get_data()
    for val in data.values():
        for dct in val:
            if (''.join(list(dct.keys())).lower() == song.lower()):
                return dct[''.join(list(dct.keys()))][1]
    return "song dosent exist"

def get_song_lyrics (song):
    """
    func getting song lyrics
    :param song:
    :return: lyrics
    """
    data = get_data()
    for val in data.values():
        for dct in val:
            if (''.join(list(dct.keys())).lower() == song.lower()):
                return dct[''.join(list(dct.keys()))][2]
    return "song dosent exist"

def get_song_album (song):
    """
    func getting songs album
    :param song:
    :return: album
    """
    data = get_data()
    for val in data.values():
        for dct in val:
            if (''.join(list(dct.keys())).lower() == song.lower()):
                return ([k for k,v in data.items() if v == val])[0][0]
    return "song dosent found"

def get_song_word(word):
    """
    func getting all songs include given word in name
    :param word:
    :return: the songs
    """
    data = get_data()
    songs = []
    for val in data.values():
        for dct in val:
            if word.lower() in ''.join(list(dct.keys())).lower():
                songs.append(''.join(list(dct.keys())))
    return ','.join(songs)

def get_lyrics_word(word):
    """
    func get all songs in their lyrics include given word
    :param word:
    :return: the songs
    """
    data = get_data()
    songs = []
    for val in data.values():
        for dct in val:
            if word.lower() in dct[''.join(list(dct.keys()))][2].lower():
                songs.append(''.join(list(dct.keys())))
    return ','.join(songs)




