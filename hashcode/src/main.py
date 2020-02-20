import random
import sys

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


def add_photo(line, id):
    photo = {}
    array = line.split(' ')
    photo['orientation'] = array[0]
    photo['tags'] = array[2:]
    photo['id'] = id
    pong = photo['tags'][-1][:-1]
    photo['tags'][-1] = pong
    photo['tags'] = set(photo['tags'])
    if photo['orientation'] == 'V':
        photos.append(photo)
        photosV.append(photo)
    else:
        photos.append(photo)
        photosH.append(photo)


def main():
    # Parsing
    file_name = sys.argv[1]
    f = open(file_name, 'r')
    f.readline()
    i = 0
    for line in f:
        add_photo(line, i)
        i += 1

    # Algorithm
    slides = make_slides(photosH, photosV)
    slideshow = make_ss(slides)
 
 
    # Output
    ss_out(file_name, slideshow)


if __name__ == "__main__":
    main()
