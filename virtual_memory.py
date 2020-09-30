with open('RAM_frames.txt') as file:
    M = int(file.readline())
    RAM = [-1]*M

# массив, изображающий оперативную память


def refresh(array):
    for n in array:
        n = -1
# функция, обновления массива


def is_element_loaded(element):
    for j in range(M):
        if RAM[j] == element:
            return 'YES'
    return 'NO'
# проверка на наличие того или иного элемента в массиве


def load_page(page, k):
    if is_element_loaded(page) == 'NO':
        RAM[k] = page
# функция, загружающая элемент в массив, если его там еще нет


with open('page_references.txt') as file:
    N = int(file.readline())
    addres_space = []
    for number in file.readline().strip().split():
        addres_space.append(int(number))
# заполнили массив страничного пространства


def fifo(fifo_answers=0):
    refresh(RAM)
    used_frames = 0
    # количество уже занятых кадров памяти
    vacant_frame = 0
    # индекс первого свободного кадра памяти
    for i in range(N):
        if used_frames < M:
            # пока в каждом кадре не будет по странице
            if is_element_loaded(addres_space[i]) == 'NO':
                load_page(addres_space[i], vacant_frame)
                used_frames += 1
                vacant_frame += 1
                fifo_answers += 1
        else:
            if is_element_loaded(addres_space[i]) == 'NO':
                del RAM[0]
                RAM.insert(M-1, addres_space[i])
                # удаляем первый элемент, в конец ставим новый, тем самым сдвинув массив на один влево
                fifo_answers += 1
    return fifo_answers  # количество ответов второго типа


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
                # так как страница только что вызвалась, переставляем её вправо в свободный кадр
        else:
            if is_element_loaded(addres_space[i]) == 'NO':
                del RAM[0]
                RAM.insert(M - 1, addres_space[i])
                lru_answers += 1
            else:
                RAM.insert(vacant_frame, addres_space[i])
                RAM.pop(addres_space[i])
                # так как страница только что вызвалась, переставляем её в конец массива как самую новую
    return lru_answers # количество ответов второго типа


print(fifo())


print(lru())


print(RAM)
