print("Введите три целых числа через пробел:")
a, b, c = map(int, input().split())
m1 = a*b
m2 = b*c
m3 = c*a
Stepen = a ** 4
Ostatokkkk = b % c
целостное = c // a
print ("Результаты умножений:" , m1, m2, m3)
print ("Результаты дополнительных действий:" , Stepen, Ostatokkkk, целостное)
print ("Результаты :" , Stepen + Ostatokkkk + целостное)