from random import randint
def print_name(name):
    print(f'Hello {name}')
    
names = ['Vasa', 'Petya', 'Kolya', 'Tola', 'Ola']


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

def search_fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

res = search_fact(3)


def matr_def_num(n, randon_from=1, random_to=9):
    matrx = []
    for row in range(n[0]):
        row = []
        for el in range(n[1]):
            row.append(randint(randon_from, random_to))
        matrx.append(row)
    print(matrx)
    return matrx

def test(*args):
    print(args)
    
def sum_args(*args):
    summ = 0
    for i, v in enumerate(args):
        summ+= v*i
    print(summ)
    return summ


def sum_max_task(*args):
    summ = 0
    maxx = args[0]
    for el in args:
        summ+=el
        if el > maxx:
            maxx = el
    return summ, maxx


def test_2(*args, **kwrags):
    print(type(kwrags))
    print(kwrags)
    print(args)
    for key, val in kwrags.items():
        print(f'key -- {key}, val -- {val}')
        

def search_key(**kwargs):
    for key, val in kwargs.items():
        if len(key) % 2 == 0:
            print(f'key - {key} val - {val}')


def arithmetic_mean(*args):
    return round(sum(args) / len(args),3)


def geometric_mean(*args):
    product = 1
    for x in args:
        product *= x
    return round(product ** (1 / len(args)), 3)


def mean_with_type(*args, mean_type="arithmetic"):
    t = str(mean_type).lower().strip()
    if t == 'arithmetic':
        return arithmetic_mean(*args)
    if t == 'geometric':
        return geometric_mean(*args)
    else:
        print('ERROR')


print(mean_with_type(2, 4, 8, mean_type="arithmetic"))
print(mean_with_type(2, 4, 8, mean_type="geometric"))