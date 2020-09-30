with open('RAM_frames.txt') as file:
    M = int(file.readline())
    RAM = [-1]*M


def refresh(array):
    for n in array:
        n = -1


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


def fifo(fifo_answers=0):
    refresh(RAM)
    used_frames = 0
    vacant_frame = 0
    for i in range(N):
        if used_frames < M:
            if is_element_loaded(addres_space[i]) == 'NO':
                load_page(addres_space[i], vacant_frame)
                used_frames += 1
                vacant_frame += 1
                fifo_answers += 1
        else:
            if is_element_loaded(addres_space[i]) == 'NO':
                del RAM[0]
                RAM.insert(M-1, addres_space[i])
                fifo_answers += 1
    return fifo_answers


def lru(lru_answers=0):
    refresh(RAM)
    used_frames = 0
    vacant_frame = 0
    for i in range(N):
        if used_frames < M:
            if is_element_loaded(addres_space[i]) == 'NO':
                load_page(addres_space[i], vacant_frame)
                used_frames += 1
                vacant_frame += 1
                lru_answers += 1
            else:
                RAM.insert(vacant_frame, addres_space[i])
                RAM.pop(addres_space[i])
        else:
            if is_element_loaded(addres_space[i]) == 'NO':
                del RAM[0]
                RAM.insert(M - 1, addres_space[i])
                lru_answers += 1
            else:
                RAM.insert(vacant_frame, addres_space[i])
                RAM.pop(addres_space[i])
    return lru_answers


print(fifo())


print(lru())


print(RAM)
