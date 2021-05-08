def cases():
    NCases = int(input())
    cases = list()
    for _ in range(NCases):
        Matrix = list()
        MatrixSize = int(input())
        for _ in range(MatrixSize):
            line = input()
            Matrix += [line.split()]
        cases +=[Matrix]
    return cases


def trace(matrix):
    s = 0
    for i in range(len(matrix)):
        s += int(matrix[i][i])
    return s


def duplicate(tableau):
    for elm in tableau:
        if tableau.count(elm) != 1:
            return True
    return False


def duplicate_lines(matrix):
    d_lines = 0
    for line in matrix:
        if duplicate(line):
            d_lines += 1
    return d_lines


def dupliate_columns(matrix):
    d_columns = 0
    for i in range(len(matrix)):
        column = list()
        for line in matrix:
            column +=[line[i]]
        if duplicate(column):
            d_columns += 1
    return d_columns


def output(cases):
    i = 1
    for case in cases:
        print('Case #'+str(i)+':', trace(case), duplicate_lines(case), dupliate_columns(case))
        i+=1


if __name__ == '__main__':
    cases = cases()
    output(cases)
