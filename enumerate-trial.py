def main():
    fruits=["Apple", "Banana","Cherry","Guava"]
    my_fav_movie="Moana"

    #creating enumerate objects
    obj1=enumerate(fruits)
    obj2=enumerate(my_fav_movie)

    print (list(enumerate(fruits)))

    #to start the indexing from 2
    print (list(enumerate(my_fav_movie,2)))

    for c, value in enumerate (fruits,1):
        print (c)

if (__name__=="__main__"):
    main()