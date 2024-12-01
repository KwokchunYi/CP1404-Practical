import wikipedia

search = input("Search >>>")
while search != "":
    print(wikipedia.page(search))
    print(wikipedia.summary(search))
    search = input("Search >>>")