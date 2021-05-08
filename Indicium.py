def cases():
    nbr_cases = int(input())
    test_cases = list()
    for _ in range(nbr_cases):
        case_ch = input()
        test_cases += [case_ch.split()]
    return test_cases


def possible_traces(N):
    possible_traces = list()
    for i in range(1,N+1):
        possible_traces += [N*i]
    return possible_traces

def generate_matrix(dim,trace):
    matrix = list()
    if dim%2 == 1:
        for row in range(dim):
            for cell in range(dim):
            
            
        

def main(cases):
    i=1
    for case in cases:
        if int(case[1]) in possible_traces(int(case[0])):
            print('Case #'+str(i)+': POSSIBLE')
            for line in generate_matrix(case[0],case[1]*case[0]):
                print(' '.join(line))#works only with str
        else:
            print('Case #'+str(i)+': IMPOSSIBLE')
        i+=1

main(cases())
