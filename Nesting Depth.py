def lescas():
    t = int(input())
    cases = list()
    for _ in range(t):
        case =input()
        cases += [case]
    return cases

def decremante(ch):
    ch1=str()
    for c in ch:
        ch1+=str(int(c)-1)
    return ch1

def encremante(ch):
    ch1=str()
    for c in ch:
        if c != '(' and c!=')':
            ch1+=str(int(c)+1)
        else:
            ch1 += c
    return ch1

def solution(ch):
    if ch == '':
        return ch
    if '0' in ch :
        for i in range(len(ch)):
            if ch[i] == '0':
                ch1 = solution(ch[:i]) + ch[i] + solution(ch[i+1:])   
                return(ch1)
    else:
        ch1 ='(' + solution(decremante(ch)) +')'
        return(encremante(ch1))

def main():
    cases = lescas()
    i = 1
    for case  in cases:
        print('Case #'+str(i)+':', solution(case))
        i += 1
main()
