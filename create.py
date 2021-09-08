import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://postgres:***@localhost:5432/postgres')
connection = engine.connect()

############################################################
############# Создаю новую схему music_website #############
############################################################

create_schema = connection.execute("""CREATE SCHEMA music_website
    AUTHORIZATION postgres;;""")

############################################################
################ Создаю таблицу музыкантов #################
############################################################

create_musician = connection.execute("""CREATE TABLE IF NOT EXISTS music_website.musician (
    id serial PRIMARY KEY, 
    alias varchar(40) UNIQUE NOT NULL
);""")

############################################################
########### Создаю таблицу музыкальных жанров ##############
############################################################

create_style = connection.execute("""CREATE TABLE IF NOT EXISTS music_website.style (
    id serial PRIMARY KEY,	
    name_of_the_style varchar(40) UNIQUE NOT NULL, 
    description varchar(200)
); """)

############################################################
################ Создаю таблицу альбомов ###################
############################################################

create_album = connection.execute("""CREATE TABLE IF NOT EXISTS music_website.album (
    id serial PRIMARY KEY,	
    title varchar(100) UNIQUE NOT NULL,
    year_of_release date
);""")

###################################################################################################
########### Создаю таблицу треков, каждый трек связан с одним альбомом по id альбома ##############
###################################################################################################

create_track = connection.execute("""CREATE TABLE IF NOT EXISTS music_website.track (
    id serial PRIMARY KEY,
    album_id integer NOT NULL REFERENCES album(id),
    name varchar(100),	
    duration int
);""")

###################################################
########### Создаю таблицу сборников ##############
###################################################

create_collection = connection.execute("""CREATE TABLE IF NOT EXISTS music_website.music_collection (
    id serial PRIMARY KEY,
    name_of_collection varchar(100) UNIQUE NOT NULL,
    create_year date
);""")

######################################################
########### Добавляю таблицы со связями ##############
######################################################

##############################################################################
########### таблица musician_style связывает музыкантов и жанры ##############
##############################################################################

create_musician_style = connection.execute("""CREATE TABLE IF NOT EXISTS music_website.musician_style (
    id serial PRIMARY KEY,
    musician_id integer NOT NULL REFERENCES musician(id),
    style_id integer NOT NULL REFERENCES style(id)
);""")

################################################################################
########### таблица musician_album связывает музыкантов и альбомы ##############
################################################################################

create_musician_album = connection.execute("""CREATE TABLE IF NOT EXISTS music_website.musician_album (
    id serial PRIMARY KEY,
    musician_id integer NOT NULL REFERENCES musician(id),
    album_id integer NOT NULL REFERENCES album(id)
);""")

###################################################################################
########### таблица track_collection связывает музыкантов и сборники ##############
###################################################################################

create_track_collection = connection.execute("""CREATE TABLE IF NOT EXISTS music_website.track_collection (
    id serial PRIMARY KEY,
    track_id integer NOT NULL REFERENCES track(id),
    music_collection_id integer NOT NULL REFERENCES music_collection(id)
);""")
