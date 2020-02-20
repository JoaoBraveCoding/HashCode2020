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
    def __init__(self, sign_up, books, books_per_day):
        self.sign_up = sign_up
        self.books = books
        self.books_per_day = books_per_day

class book:
    def __init__(self, book_id):
        self.book_id = book_id
        self.added = False

def ss_in(file_name):
    # Parsing
    f = open(file_name, 'r')

    global max_days, book_score, books, libs 

    #First Line aka number of days
    first_line = f.readline()
    line_params = first_line.split(' ')
    max_days = int(line_params[2])

    #Second line aka book scores
    second_line = f.readline().split(' ')
    i = 0
    for param in second_line:
        book_score.append(int(param))
        books.append(book(i))
        i += 1


    #Rest of the lines aka populate libs
    #Reads two lines to create a lib
    for line in f:
        #Gets the first line with the sign_up and books_per_day
        line_params = line.split(' ')

        #Gets the books
        library_books = f.readline().split(' ')
        books_to_append = []
        for param in library_books:
            if param != '':
                books_to_append.append( books[ int(param) ] )
            
        organize_books(books_to_append)
        libs.append(lib(line_params[1], books_to_append, line_params[2]))


def ss_out(file_name):
    out = "" + str(len(out_libs)) + "\n"
    for libe in out_libs:
        out += str(libe.sign_up) + " " + str(len(libe.books)) + "\n"
        tempS = ""
        for j in libe.books:
            tempS += str(j) + " "
        out += tempS + "\n"


    file_name_splited = file_name.split("/")
    f = open("hashcode/out/" + file_name_splited[2], 'w')
    f.writelines(out)
    f.close()


# take second element for sort
def value(elem):
    return book_score[elem.book_id]*-1

def organize_books(book_array):
    book_array.sort(key=value)
    #TODO não sei se o parametro é alterado ou se o tenho de retornar
    return book_array


def get_book(lib):
    best_book = None
    if len(lib.books) > 0:
        while len(lib.books) > 1:
            best_book = lib.books[0]
            lib.books = lib.books[1:]
            if not best_book.added:
                break
        if best_book.added and len(lib.books) == 1 and not lib.books[0].added:
            best_book = lib.books[0]

    return best_book


def main():
    file_name = sys.argv[1]
    ss_in(file_name)

    #Algorith
    #get melhor lib
    #actualizar dias que faltam
    #acTUALIZAR O VALOR DOS LIVOS
    #actualizar valor das libs
    #reordenar o array de libs


    # Output
    ss_out(file_name)


if __name__ == "__main__":
    main()






#passar id quando usado no choose_lib
def points_per_lib(lib, id):
    time_left = day - lib.sign_up
    #self.books_per_day
    #self.books - supostamente deve estar organizada por pontos
    num_of_books = time_left * lib.books_per_day
    books = []
    book_count=0
    total = 0
    #self books
    temp_books = books[:]
    while(book_count<num_of_books):
        book = temp_books[0]
        temp_books = temp_books[1:]
        if(book == []):
            break
        book_points = value(book)
        books.append(book)
        total+=book_points
        book_count+=1

    points_lib = lib(id, books, lib.books_per_day)
    return [total, points_lib]

def choose_lib():
    best_lib = None
    for i in range(0, len(libs)):
        new_lib = points_per_lib(libs[i], i)
        if (best_lib == None or new_lib[0] > best_lib[0]):
            best_lib = new_lib
    
    return best_lib

day = 0

while (day<max_days):
    #do stuff
    #
    day+=1
