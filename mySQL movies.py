import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bitlab"
)

mycursor = mydb.cursor()


def addMovie(year, movie_title, budget, director, box_office):
    global mydb
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (year, movie_title, budget, director, box_office) VALUES (%s, %s, %s, %s, %s)"
    values = (year, movie_title, budget, director, box_office)
    mycursor.execute(sql, values)
    mydb.commit()


def getMovies():
    global mydb
    mycursor = mydb.cursor()
    sql = "SELECT * FROM movies ORDER BY year DESC"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


def deleteMovie(movie_title):
    global mydb
    mycursor = mydb.cursor()
    sql = "DELETE FROM movies WHERE movie_title = " + str(movie_title)
    mycursor.execute(sql)
    mydb.commit()


def updateMovie(year, movie_title, budget, director, box_office):
    global mydb
    mycursor = mydb.cursor()
    sql = "UPDATE movies SET year = %s, budget = %s, director = %s, box_office = %s WHERE movie_title = " + str(movie_title)
    values = (year, movie_title, budget, director, director, box_office)
    mycursor.execute(sql, values)
    mydb.commit()


while True:
    print("PRESS 1 TO ADD MOVIE")
    print("PRESS 2 TO LIST MOVIES")
    print("PRESS 3 TO DELETE MOVIE")
    print("PRESS 4 TO UPDATE MOVIE")
    print("PRESS 0 TO EXIT")

    choice = input()

    if choice == "1":
        print("INSERT YEAR: ")
        year = input()
        print("INSERT MOVIE TITLE: ")
        movie_title = input()
        print("INSERT BUDGET: ")
        budget = input()
        print("INSERT DIRECTOR: ")
        director = input()
        print("INSERT BOX OFFICE: ")
        box_office = input()

        addMovie(year, movie_title, budget, director, box_office)

    elif choice == "2":
        movies = getMovies()
        for movie in movies:
            print(movie)

    elif choice == "3":
        movies = getMovies()
        for movie in movies:
            print(movie)

        print("CHOOSE MOVIE TITLE TO DELETE:")
        movie_to_delete = input()
        deleteMovie(movie_to_delete)

    elif choice == "4":
        movies = getMovies()
        for movie in movies:
            print(movie)

        print("CHOOSE MOVIE TITLE TO UPDATE:")
        movie_title = input()

        print("INSERT NEW YEAR OF ORIGIN: ")
        year = input()
        print("INSERT NEW MOVIE TITLE: ")
        movietitle = input()
        print("INSERT NEW BUDGET: ")
        budget = input()
        print("INSERT NEW DIRECTOR: ")
        director = input()
        print("INSERT NEW BOX OFFICE: ")
        box_office = input()
        updateMovie(year, movietitle, budget, director, box_office)

    elif choice == "0":
        break
