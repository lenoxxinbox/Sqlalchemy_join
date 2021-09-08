import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://postgres:***@localhost:5432/postgres')
connection = engine.connect()

adding_musician = connection.execute("""INSERT INTO music_website.musician(alias)
    VALUES('Santana'),
    ('Eminem'), ('Jon Bon Jovi'),
    ('Ace of Base'), ('Adriano Celentano'),
    ('Enrique Iglesias'), ('Sean Paul'),
    ('Manowar'),('Chuck Berry');
    """)

adding_style = connection.execute("""INSERT INTO music_website.style(name_of_the_style, description)
    VALUES('rock and roll', 'clear rhythm, fast tempo, relaxed performance'),
    ('metal', 'overloaded electric guitar sound, prolonged guitar solos, energetic rhythm, lightweight riffs'),
    ('reggae', 'the leading role of rhythmic elements, mainly bass guitars, moderate tempo, breaks on high tones'),
    ('rock music', 'a constant rhythm maintained by the rhythm section'),
    ('hip hop', 'it consists of stylized rhythmic music, which is usually accompanied by rap,
    rhythmic and rhyming speech'),
    ('pop music', 'simplicity of the instrumental part, rhythm, emphasis on vocals'),
    ('latin pop', 'a fast rhythm is characteristic');
    """)

adding_musician_style = connection.execute("""INSERT INTO music_website.musician_style(musician_id, style_id)
    VALUES(1, 4), (2,5), (3, 4), (4, 6), (5, 4), (6, 7), (7, 3), (8, 2), (9, 1);
    """)

adding_album = connection.execute("""INSERT INTO music_website.album(title, year_of_release)
    VALUES('Guitar Heaven', '2010-01-01'),
    ('Music to Be Murdered By', '2020-01-01'),
    ('Have a Nice Day', '2005-01-01'),
    ('Crush', '2000-01-01'),
    ('Dormi amore, la situazione non è buona', '2007-01-01'),
    ('Tomahawk Technique', '2012-01-01'),
    ('Imperial Blaze', '2009-01-01'),
    ('Mad Love: The Prequel', '2018-01-01'),
    ('Kings Of Metal', '1988-01-01');
    """)

adding_track = connection.execute("""INSERT INTO music_website.track(album_id, name, duration)
    VALUES(1, 'Whole Lotta Love', 231),
    (1, 'Sunshine Of Your Love', 283),
    (2, 'Godzilla', 211),
    (3, 'Story of My Life', 248),
    (3, 'Last Cigarette', 218),
    (4, 'Its My Life', 224),
    (4, 'One Wild Night', 258),
    (5, 'Ragazzo del sud', 334),
    (7, 'Straight From My Heart', 180),
    (6, 'She Doesnt Mind', 228),
    (8, 'Mad Love', 199),
    (9, 'Wheels of Fire', 251),
    (9, 'Kings of Metal', 223),
    (9, 'Heart of Steel', 310),
    (9, 'Sting of the Bumblebee', 165),
    (9, 'The Crown and the Ring', 286);
    """)

adding_musician_album = connection.execute("""INSERT INTO music_website.musician_album(musician_id, album_id)
    VALUES(1, 1), (2, 2), (3, 3), (3, 4), (5, 5), (7, 6), (7, 7), (7, 8), (8, 9);
    """)

adding_music_collection = connection.execute("""INSERT INTO music_website.music_collection(name_of_collection,
create_year)
    VALUES('Romantic guitar', '2009-01-01'),
    ('Summer hip hop', '2021-01-01'),
    ('Romantic collection', '2011-01-01'),
    ('Metal ballads', '2012-01-01'),
    ('Hip hop world', '2020-01-01'),
    ('The best of rock music', '2019-01-01'),
    ('Song of world', '2007-01-01'),
    ('The best of hip hop', '2012-01-01'),
    ('Hip hop dance', '2020-01-01');
    """)

adding_musician_track_collection = connection.execute("""INSERT INTO music_website.track_collection(track_id,
music_collection_id)
    VALUES(1, 1), (7, 1), (2, 2), (5, 3), (4, 3), (8, 3), (12, 4), (3, 5), (6, 6), (8, 7), (10, 8), (10, 9), (16, 3);
    """)
