import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:***@localhost:5432/postgres')
# print(engine)

con = engine.connect()

count_musician = con.execute("""
    SELECT count(name_of_the_style), name_of_the_style FROM "style" s
    JOIN musician_style ms ON ms.style_id = s.id 
    JOIN musician m ON m.id = ms.musician_id 
    GROUP BY s.name_of_the_style;
""").fetchall()

print(count_musician)  # количество исполнителей в каждом жанре

count_track = con.execute("""
    SELECT COUNT(t."name") FROM track t 
    JOIN album a ON a.id = t.album_id 
    WHERE a.year_of_release = '2019-01-01' OR a.year_of_release = '2020-01-01';
""").fetchall()

print(count_track)  # количество треков, вошедших в альбомы 2019-2020 годов

avg_duration = con.execute("""
    SELECT a.title, AVG(t.duration) FROM track t 
    JOIN album a ON a.id = t.album_id 
    GROUP BY a.title, a.id;
""").fetchall()

print(avg_duration)  # средняя продолжительность треков по каждому альбому

not_play_year = con.execute("""
    SELECT alias FROM musician m 
    LEFT JOIN musician_album ma ON m.id = ma.musician_id 
    LEFT JOIN album a ON a.id = ma.album_id 
    WHERE year_of_release != '2020-01-01' OR year_of_release is NULL
    GROUP BY alias;
""").fetchall()

print(not_play_year)  # все исполнители, которые не выпустили альбомы в 2020 году

celentano_in_collection = con.execute("""
    SELECT mc.name_of_collection, m.alias FROM music_collection mc 
    JOIN track_collection tc ON mc.id = tc.music_collection_id 
    JOIN track t ON t.id = tc.track_id 
    JOIN album a ON a.id = t.album_id 
    JOIN musician_album ma ON ma.album_id = a.id 
    JOIN musician m ON m.id = ma.musician_id 
    WHERE m.alias = 'Adriano Celentano';
""").fetchall()

print(celentano_in_collection)  # названия сборников, в которых присутствует конкретный исполнитель (выберите сами)

many_style = con.execute("""
    SELECT mc.name_of_collection FROM musician m 
    JOIN musician_style ms ON m.id = ms.musician_id 
    JOIN style s ON ms.style_id = s.id 
    JOIN musician_album ma ON ma.musician_id = m.id 
    JOIN album a ON ma.album_id = a.id 
    JOIN track t ON t.album_id = a.id 
    JOIN track_collection tc ON tc.track_id = t.id 
    JOIN music_collection mc ON mc.id = tc.music_collection_id 
    GROUP BY  mc.name_of_collection, s.name_of_the_style
    HAVING COUNT(s.name_of_the_style) > 1 ;
""").fetchall()

print(many_style)  # название альбомов, в которых присутствуют исполнители более 1 жанра

not_collection = con.execute("""
    SELECT t."name" FROM track t 
    LEFT JOIN track_collection tc ON tc.track_id = t.id 
    WHERE tc.music_collection_id IS NULL;
""").fetchall()

print(not_collection)  # наименование треков, которые не входят в сборники

con = engine.connect()

small_musician_track = con.execute("""
    SELECT alias, duration FROM (
        SELECT m.alias, MIN(t.duration) AS duration FROM track t 
        LEFT JOIN track_collection tc ON tc.track_id = t.id
        JOIN album a ON a.id = t.album_id 
        JOIN musician_album ma ON ma.album_id = a.id 
        JOIN musician m ON m.id = ma.musician_id 
        GROUP BY m.alias 
        ORDER BY MIN(t.duration)) AS foo
    LIMIT 1;
""").fetchall()

print(small_musician_track)  # исполнителя(-ей), написавшего самый короткий по продолжительности трек
# (теоретически таких треков может быть несколько)

con = engine.connect()

album_little = con.execute("""
    SELECT * FROM (
        SELECT COUNT(t."name") AS quant, a.title AS title 
        FROM album a 
        JOIN track t ON t.album_id = a.id 
        GROUP BY a.title) AS f
    WHERE quant = 1;  
""").fetchall()

print(album_little)  # название альбомов, содержащих наименьшее количество треков 
# не понимаю, как вызвать функцию MIN, дело в том что у меня одинаковое количество песен в минимальных альбомах
