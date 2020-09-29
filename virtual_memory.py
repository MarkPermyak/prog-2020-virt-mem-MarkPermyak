with open('RAM_frames.txt') as file:
    M = int(file.readline())
    RAM = [None]*M

with open('page_references.txt') as file:
    N = file.readline()
    addres_space = []
    for element in file.readline().strip().split():
        addres_space.append(int(element))


for i in range(M):
    RAM[i] = addres_space[i]


