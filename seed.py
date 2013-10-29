import model
import csv
import re
from datetime import datetime, date

def load_users(session):
    # use u.user
    _f = open("seed_data/u.user")
    line = _f.readline()
    while (line):
        data = line.strip("\n").split("|")
        line = _f.readline()
        
        user_id = int(data[0])
        age = int(data[1])
        gender = data[2]
        zipcode = data[3]
    
        if len(data) == 4:
            email = None
            password = None
        if len(data) == 5:
            email = data[4]
            password = None
        if len(data) == 6:
            password = data[5]
    
        user = model.User(user_id, age, gender, zipcode, email, password)
        session.add(user)
        session.commit()

def load_movies(session):
    # use u.item
    filename = "seed_data/u.item"
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter="|")
        try:
            for row in reader:
                movie_id = int(row[0])
                title = re.sub(' \(\d\d\d\d\)$', '', row[1])
                title = title.decode("latin-1")
                if row[2] != "":
                    release_date = datetime.strptime(row[2], "%d-%b-%Y").date()
                imdb_url = row[4]
                movie = model.Movie(movie_id, title, release_date, imdb_url)
                session.add(movie)
                session.commit()
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

def load_ratings(session):
    # use u.data
    filename = "seed_data/u.data"
    count = 1
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter="\t")
        try:
            for row in reader:
                rating_id = count
                user_id = int(row[0])
                movie_id = int(row[1])
                rating = int(row[2])
                timestamp = int(row[3])
                
                count += 1
                
                rating = model.Rating(rating_id, user_id, movie_id, rating, timestamp)
                session.add(rating)
                session.commit()                
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
    

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    load_ratings(session)
if __name__ == "__main__":
    s= model.connect()
    main(s)
