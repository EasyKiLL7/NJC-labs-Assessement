import sqlite3

conn = sqlite3.connect('Movies.db')
cursor=conn.cursor()

#table creation
cursor.execute("""CREATE TABLE IF NOT EXISTS Movies (
                Name TEXT PRIMARY KEY,
                Actor TEXT,
                Actress TEXT,
                Director TEXT,
                yearOfRelease INTEGER)""") 

#Inserting Values
cursor.execute(" INSERT INTO Movies VALUES ('The Matrix','Keanu Reeves','Carrie-Anne Moss','The Wachowskies',1999)")
cursor.execute(" INSERT INTO Movies VALUES ('Inception','Leonardo DiCaprio','Marion Cotillard','Christopher Nolan',2010)")
cursor.execute(" INSERT INTO Movies VALUES ('The Shawshank Redemption','Tim robbins','','Frank Darabont',1994)")
cursor.execute(" INSERT INTO Movies VALUES ('Gladiator','Maximus','Connie Nielsen','Ridley Scott',2000)")
cursor.execute(" INSERT INTO Movies VALUES ('A Quiet place','Cillian Murphy','Emily Blunt','John Krasinski',2018)")
cursor.execute(" INSERT INTO Movies VALUES ('Malignant','George Young','Annabelle wallis','James Wan',2021)")
cursor.execute(" INSERT INTO Movies VALUES ('3 Idiots','Aamir Khan','Kareena Kapoor','Rajkumar Hirani',2009)")
cursor.execute(" INSERT INTO Movies VALUES ('Taare Zammen Par','Aamir Khan','Tisca Chopra','Aamir Khan',2007)")
cursor.execute(" INSERT INTO Movies VALUES ('Parasite','','','',2019)")

#executing queries...

cursor.execute("SELECT * FROM Movies")
query=cursor.fetchall()

cursor.execute("SELECT * FROM Movies WHERE Name='The Matrix'")
query1=cursor.fetchall()
 
cursor.execute("SELECT Name,yearOfRelease FROM Movies ORDER BY yearOfRelease DESC")
query2=cursor.fetchall()

cursor.execute("SELECT * FROM Movies LIMIT 3") 
query3=cursor.fetchall()

#printing the output

print('All Movies from the Database: \n', query) 
print('\n')
print('More queries: \n',query1)
print('\n')
print('More queries: \n',query2)
print('\n')
print('More queries: \n',query3)
print('\n')
print("That's All, Thankyou")
