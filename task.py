from random import randint
def print_name(name):
    print(f'Hello {name}')
    
names = ['Vasa', 'Petya', 'Kolya', 'Tola', 'Ola']

for name in names:
    print_name(name)

def make_marx(num_el, num_row):
    matrix = []
    for row in range(num_row):
        row = []
        for el in range(num_el):
            row.append(randint(1,10))
        matrix.append(row)
    return matrix

def return_sum(matrx):
    summ = 0
    for row in matrx:
        for el in row:
            summ += el
    print(summ)
    return summ


def print_martrx(matrx):
    for row in matrx:
        print(row)

def search_max(matrix):
    maxx = matrx[0][0]
    for row in matrix:
        for el in row:
            if el>maxx:
                maxx = el
    print(maxx)
    return maxx

def search_min(matrix):
    minn = matrx[0][0]
    for row in matrix:
        for el in row:
            if el<minn:
                minn = el
    print(minn)
    return minn

def search_max_min_val(matrx, search_min=False):
    vall = matrx[0][0]
    for row in matrx:
        for el in row:
            if search_min:
                if el < vall:
                    vall = el
            else:
                if el > vall:
                    vall = el
    print(vall)
    return vall


def make_and_print_martix(num_el, num_row):
    matrix = []
    for row in range(num_row):
        row = []
        for el in range(num_el):
            row.append(randint(1,10))
        matrix.append(row)
        print(row)
    return matrix

def make_and_print_search_max_min_matrix(num_el, num_row, start_num, end_num, search_max=False):
    matrix = []
    summ = 0
    vall = float('inf') if not search_max else float('-inf')
    for row in range(num_row):
        row = []
        for el in range(num_el):
            elem = (randint(start_num, end_num))
            summ += elem
            row.append(elem)
            if search_max:
                if elem > vall:
                    vall = elem
            else:
                if elem < vall:
                    vall = elem
        matrix.append(row)
        print(row)
    print(f'max\min {vall}')
    print(f'sum - {summ}')
    return matrix, vall, summ


matrx, val, summ = make_and_print_search_max_min_matrix(num_el=2, num_row=3, start_num=1, end_num=20, search_max=True)