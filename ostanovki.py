
def statoin_on_vetka(station1,station2,vetka):           
    total = 0
    for i in range(len(vetka)):
        if vetka[i][0].split('-')[0] == station1:    
            for j in range(i,len(vetka)):
                if vetka[j][0].split('-')[1] == station2:
                    total+=vetka[j][1]
                    break
                else:
                    total+=vetka[j][1]
    return total

def peresadka(x1,x2):
    flag = False
    for i in range(len(x1)):
        for j in range(len(x2)):
            if x1[i][0].split('-')[0]==x2[j][0].split('-')[0]:
                flag = x1[i][0].split('-')[0]
                break
    return flag
#------------------------------------------------------------------------------
#print('Введите станции 1 ветки')
#lst = [input(str('№'+str(_+1)+' ')) for _ in range(int(input('Кол-во станций?: ')))]
#print('Введите время между станциями')
#my_lst = [[lst[i-1]+'-'+lst[i],int(input(str(lst[i-1]+'-'+lst[i]+' ')))] for i in range(1,len(lst))]
#print('Введите станции 2 ветки')
#lst2 = [input(str('№'+str(_+1)+' ')) for _ in range(int(input('Кол-во станций?: ')))]
#print('Введите время между станциями')
#my_lst2 = [[lst2[i-1]+'-'+lst2[i],int(input(str(lst2[i-1]+'-'+lst2[i]+' ')))] for i in range(1,len(lst2))]
#print(my_lst)
#print(my_lst2)
#station1 = input('Введите станцию отправления?: ')
#station2 = input('Введите станцию прибытия?: ')
#------------------------------------------------------------------------------
my_lst = [['Солнечногорск-Клин', 20],['Клин-Решетниково', 7],['Решетниково-Завидово', 10],['Завидово-Редкино', 12],['Редкино-Тверь',15]]
my_lst_reverse = [['Тверь-Редкино',15],['Редкино-Завидово', 12],['Завидово-Решетниково', 10],['Решетниково-Клин', 7],['Клин-Солнечногорск', 20]]
my_lst2 = [['Решетниково-Путепроводная',10], ['Путепроводная-Конаковский Мох',12],['Конаковский Мох-Донховка',8],['Донховка-Конаково',15]]
my_lst2_reverse = [['Конаково-Донховка',15],['Донховка-Конаковский Мох',8],['Конаковский Мох-Путепроводная',12],['Путепроводная-Решетниково',10]]
station1 = 'Путепроводная'
station2 = 'Решетниково'
total = 0
vetka = 0
#------------------------------------------------------------------------------


def proverka_napravlenya(n):
    s = False
    e = False    
    for i in n:
        if station1 == i[0].split('-')[0]:
            s = True
        if station2 == i[0].split('-')[1]:
            e = True
    return s,e

def vetkka():
    for n in [my_lst,my_lst_reverse,my_lst2,my_lst2_reverse]:
        start,end = proverka_napravlenya(n)
        if start == True and end == True:
            vetka = n
            break
    return vetka

station_peresadka = peresadka(my_lst,my_lst2)    


#if start == True and end == True:   
#    total = statoin_on_vetka(station1,station2,vetka)

if total != 0:
    print(total)
#else:
#    vetka = 
#    total = statoin_on_vetka(station1,station_peresadka,vetka)
#    #total += statoin_on_vetka(station_peresadka,station2,my_lst2)
    #print(total)  