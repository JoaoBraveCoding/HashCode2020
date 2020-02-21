import random
import sys

book_score = []
max_days = 0
libs = []
out_libs = []
globalbooks = []
books = []
day = 0

class lib:
    def __init__(self, number, sign_up, books, books_per_day):
        self.number = number
        self.sign_up = sign_up
        self.books = books
        self.books_per_day = books_per_day
        self.shiped_books = []

class book:
    def __init__(self, book_id):
        self.book_id = book_id
        self.added = False

def ss_in(file_name):
    # Parsing
    f = open(file_name, 'r')

    global max_days, book_score, books, libs 

    #First Line aka number of days
    first_line = f.readline().split(' ')
    max_days = int(first_line[2])

    #Second line aka book scores
    second_line = f.readline().split(' ')
    i = 0
    for param in second_line:
        book_score.append(int(param))
        books.append(book(i))
        i += 1


    #Rest of the lines aka populate libs
    #Reads two lines to create a lib
    i = 0
    for _ in first_line[1]*2:
        #Gets the first line with the sign_up and books_per_day
        lib_params = f.readline().split(' ')

        #Gets the books
        library_books = f.readline().split(' ')
        books_to_append = []
        for param in library_books:
            if param != '':
                books_to_append.append( books[ int(param) ] )
            
        organize_books(books_to_append)
        libs.append(lib(i, int(lib_params[1]), books_to_append, int(lib_params[2])))
        i += 1


def ss_out(file_name):
    out = "" + str(len(out_libs)) + "\n"
    for libe in out_libs:
        out += str(libe.number) + " " + str(len(libe.shiped_books)) + "\n"
        tempS = ""
        for j in libe.shiped_books:
            tempS += str(j.book_id) + " "
        out += tempS + "\n"


    file_name_splited = file_name.split("/")
    f = open("hashcode/out/" + file_name_splited[3], 'w')
    f.writelines(out)
    f.close()


# take second element for sort
def value(elem):
    return book_score[elem.book_id]*-1

def organize_books(book_array):
    book_array.sort(key=value)
    #TODO não sei se o parametro é alterado ou se o tenho de retornar
    return book_array

def sum_books_values(book_array):
    total = 0
    for book in book_array:
        total += book_score[book.book_id]
    return total

def get_book(lib):
    best_book = None
    if len(lib.books) > 0:
        while len(lib.books) >= 2:
            best_book = lib.books[0]
            lib.books = lib.books[1:]
            if not best_book.added:
                break
        if len(lib.books) == 1 and (best_book == None) or (best_book.added and not lib.books[0].added):
            best_book = lib.books[0]
            lib.books = []

        if best_book != None:
            lib.shiped_books.append(best_book)

    return None

def get_lib_value(elem):
    days_until_no_more_books = len(elem.books)/elem.books_per_day
    return sum_books_values(elem.books)/days_until_no_more_books * -1

def sort_libs():
    global libs
    libs.sort(key=get_lib_value)

def pick_new_lib(i):
    global out_libs, libs

    if len(libs) > 0:
        # Sort from once in a while
        if i % 5 == 0:
            sort_libs()
        
        # Retrice always the first lib
        picked_lib = libs[0]
        libs = libs[1:]
        
        out_libs.append(picked_lib)
        return picked_lib.sign_up
    return 0


def let_time_fly():
    sigh_up = 0
    for i in range(0, max_days):
        if sigh_up == 0:
            sigh_up = pick_new_lib(i)
        sigh_up -= 1
        
        for lib in out_libs:
            for _ in range(0, lib.books_per_day):
                get_book(lib)
    return 

def main():
    # Input
    file_name = sys.argv[1]
    ss_in(file_name)
    #Algorith
    let_time_fly()

    # Output
    ss_out(file_name)


if __name__ == "__main__":
    main()





