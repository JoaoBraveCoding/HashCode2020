import random
import sys

book_score = []
max_days = 0
libs = []
out_libs = []
globalbooks = []
books = []
days_left = 0
max_score = 0
min_score = 100000000


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

    global max_days, book_score, books, libs, max_score, min_score

    # First Line aka number of days
    first_line = f.readline().split(' ')
    max_days = int(first_line[2])

    # Second line aka book scores
    second_line = f.readline().split(' ')
    i = 0
    for param in second_line:
        score = int(param)
        book_score.append(score)
        books.append(book(i))
        i += 1
        if max_score < score:
            max_score = score
        if min_score > score:
            min_score = score

    # Rest of the lines aka populate libs
    # Reads two lines to create a lib
    i = 0
    for _ in range(0, int(first_line[1])):
        # Gets the first line with the sign_up and books_per_day
        lib_params = f.readline().split(' ')

        # Gets the books
        library_books = f.readline().split(' ')
        books_to_append = []
        for param in library_books:
            if param != '':
                books_to_append.append(books[int(param)])

        organize_books(books_to_append)
        sign_up = int(lib_params[1])
        books_per_day = int(lib_params[2])
        libs.append(lib(i, sign_up, books_to_append, books_per_day))
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
    tmp = book_array[:]
    for i in range(len(book_array), 0):
        if book_array[i].added:
            tmp.pop(i)

    tmp.sort(key=value)
    book_array = tmp
    return


def sum_books_values(book_array):
    total = 0
    for book in book_array:
        total += book_score[book.book_id]
    return total



def get_books(lib, i):
    max_shipped_book = (max_days - i) * lib.books_per_day
    if len(lib.books) > max_shipped_book:
        lib.shiped_books = lib.books[0:max_shipped_book]
    else:
        lib.shiped_books = lib.books

    if lib.shiped_books == []:
        print("JEy")

    for j in lib.shiped_books:
        j.added = True


def get_lib_value(elem):
    # days_until_no_more_books = len(elem.books)/elem.books_per_day

    # days_it_still_can_supply = days_until_no_more_books - days_left
    # if days_it_still_can_supply < 0:
    #     days_it_still_can_supply = days_until_no_more_books
    # else:
    #     days_it_still_can_supply = days_left

    # possible_remeinder_score = sum_books_values(elem.books) / days_left

    # return (possible_remeinder_score + days_it_still_can_supply)*-1
    return elem.sign_up


def sort_libs():
    global libs
    libs.sort(key=get_lib_value)


def pick_new_lib(i):
    global out_libs, libs

    if len(libs) > 0:
        # Sort from once in a while
        sort_libs()

        # Retrice always the first lib
        picked_lib = libs[0]
        libs = libs[1:]

        time_when_ready = i + picked_lib.sign_up
        if time_when_ready > max_days:
            return None

        out_libs.append(picked_lib)
        return picked_lib
    return None


def let_time_fly():
    global days_left
    i = 0
    while i < max_days:
        days_left = max_days - 1 - i
        latest_picked_lib = pick_new_lib(i)
        if latest_picked_lib != None:
            time_when_ready = i + latest_picked_lib.sign_up
            get_books(latest_picked_lib, time_when_ready)
            i += latest_picked_lib.sign_up
        else:
            return
    return


def main():
    # Input
    file_name = sys.argv[1]
    ss_in(file_name)

    # Algorith
    let_time_fly()

    # Output
    ss_out(file_name)


if __name__ == "__main__":
    main()
