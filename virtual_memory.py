with open('RAM_frames.txt') as file:
    M = int(file.readline())
    RAM = [0]*M


def is_element_loaded(element):
    for j in range(M):
        if RAM[j] == element:
            return 'YES'
    return 'NO'


def load_page(page, k):
    if is_element_loaded(page) == 'NO':
        RAM[k] = page


with open('page_references.txt') as file:
    N = int(file.readline())
    addres_space = []
    for number in file.readline().strip().split():
        addres_space.append(int(number))


for i in range(M):
    load_page(addres_space[i], i)


print(RAM)
