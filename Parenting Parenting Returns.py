def cases():
    cases_list =list()
    nbr_cases = int(input())
    for case in(range(nbr_cases)):
        nbr_activ = int(input())
        actvties =list()
        i = 0
        for actvtie in range(nbr_activ):
            actvtie = input()
            actvtie_lis =actvtie.split()
            start, end = actvtie_lis
            actvties+=[[i, int(start),int(end)]]
            i+=1
        cases_list += [sorting(actvties)]
    return cases_list


def sorting(actvties):
    sorted_list = actvties
    sorted_list.sort(key=lambda x: x[1])
    return sorted_list


def day_plan(day):
    C = 0
    J = 0
    for actvtie in day:
        if actvtie[1] >= C:
            C = actvtie[2]
            actvtie += ['C']
            
            #plan += 'C'
        elif actvtie[1] >= J:
            J = actvtie[2]
            actvtie += ['J']
            #plan += 'J'
        else:
            return('IMPOSSIBLE')
    plan=str()
    for i in range(len(day)):
        for actvtie in day:
            if i == actvtie[0]:
                plan += actvtie[3]
    return(plan)

def main(days):
    i =1
    for day in days:
        print('Case #'+str(i)+':',day_plan(day))
        i+=1

#main
days = cases()
main(days)

            
