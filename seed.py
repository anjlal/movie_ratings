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
        user = model.User()
        user.id = int(data[0])
        user.age = int(data[1])
        user.gender = data[2]
        user.occupation = data[3]
        user.zipcode = data[4]
        # user_id = int(data[0])
        # age = int(data[1])
        # gender = data[2]
        # zipcode = data[3]
        #     
        # if len(data) == 4:
        #     email = None
        # #     password = None
        # if len(data) == 5:
        #     user.email = data[4]
        #     # password = None
        # if len(data) == 6:
        #     user.password = data[5]
    
        # user = model.User(user_id, age, gender, zipcode, email, password)
        session.add(user)
        session.commit()

def load_movies(session):
    # use u.item
    filename = "seed_data/u.item"
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter="|")
        try:
            for row in reader:
                movie = model.Movie()
                movie.id = int(row[0])
                title = re.sub(' \(\d\d\d\d\)$', '', row[1])
                movie.name = title.decode("latin-1")
                if row[2] != "":
                    movie.released_at = datetime.strptime(row[2], "%d-%b-%Y").date()
                movie.imdb_url = row[4]
                # movie = model.Movie(movie_id, title, release_date, imdb_url)
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
                rating = model.Rating()
                rating.id = count
                rating.user_id = int(row[0])
                rating.movie_id = int(row[1])
                rating.rating = int(row[2])
                rating.timestamp = int(row[3])
                
                count += 1
                
                # rating = model.Rating(rating_id, user_id, movie_id, rating, timestamp)
                session.add(rating)
                session.commit()
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
    

# def main(session):
#     # You'll call each of the load_* functions with the session as an argument
#     load_users(session)
#     load_movies(session)
#     load_ratings(session)
# if __name__ == "__main__":
#     #s= model.connect()
#     main(s)

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_users(session)
    load_movies(session)
    load_ratings(session)
if __name__ == "__main__":
    #s= model.connect()
    main(model.session)
