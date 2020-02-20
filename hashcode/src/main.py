import random
import sys

book_score = []
max_days = 0
libs = []

class lib:
    def __init__(self, sign_up, books, books_per_day):
        self.sign_up = sign_up
        self.books = books
        self.books_per_day = books_per_day


def ss_out(file_name, slideshow):
    out = ""
    out += str(len(slideshow)) + "\n"
    file_name_splited = file_name.split("/")
    for i in slideshow:
        # TODO update this
        tempS = ""
        for j in i[0]:
            tempS += str(j) + " "
        out += tempS + "\n"
    f = open("hashcode/out/" + file_name_splited[2], 'w')
    f.writelines(out)
    f.close()


# take second element for sort
def value(elem):
    return book_score[elem]*-1

def organize_books(book_array):
    book_array.sort(key=value)
    #TODO não sei se o parametro é alterado ou se o tenho de retornar
    return book_array

def get_book(lib):
    best_book = lib.books[0]
    lib.books = lib.books[1:]
    return best_book


def main():
    # Parsing
    file_name = sys.argv[1]
    f = open(file_name, 'r')

    #First Line aka number of days
    first_line = f.readline()
    line_params = first_line.split(' ')
    max_days = int(line_params[2])

    #Second line aka book scores
    second_line = f.readline().split(' ')
    for param in second_line:
        book_score.append(int(param))

    #Rest of the lines aka populate libs
    #Reads two lines to create a lib
    for line in f:
        #Gets the first line with the sign_up and books_per_day
        line_params = line.split(' ')

        #Gets the books
        library_books = f.readline().split(' ')
        books = []
        for param in library_books:
            if param != '':
                books.append(int(param))
            
        organize_books(books)
        libs.append(lib(line_params[1], books, line_params[2]))


    #Algorith
    #get melhor lib
    #actualizar dias que faltam
    #acTUALIZAR O VALOR DOS LIVOS
    #actualizar valor das libs
    #reordenar o array de libs
 
    # Output
    #ss_out(file_name, slideshow)


if __name__ == "__main__":
    main()




