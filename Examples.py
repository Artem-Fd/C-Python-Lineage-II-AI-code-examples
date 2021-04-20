...
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
...
def sadd(x,y):
    return x + y
def ssub(x,y):
    return x - y
def sdiv(x,y):
    if(y==0):return "Деление на 0!"
    return x / y
def smult(x,y):
    return x * y
def smod(x,y):
    if(y==0):return "Деление на 0!"
    return x % y
def spow(x,y):
    return x ** y
def sint_div(x,y):
    if(y==0):return "Деление на 0!"
    return x // y

operations = {
    '+': sadd,
    '-': ssub,
    '/': sdiv,
    '*': smult,
    'mod': smod,
    'pow': spow,
    'div': sint_div
    # ...
}

x=float(input())
y=float(input())
operation_type=input()
print(operations[operation_type](x,y))
...
В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".

Для того, чтобы это звучало правильно, для каждого n n n нужно использовать верное окончание слова.

Напишите программу, считывающую с пользовательского ввода целое число n n n (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.

В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.

Дополнительный комментарий к условию:
Обратите внимание, что задача не так проста, как кажется на первый взгляд. Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из случаев входных данных (число программистов 0≤n≤1000 0 \le n \le 1000 0≤n≤1000). Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания. 
...
# put your python code here
number_of_programmers=str(input())
number_of_programmers='0'+ number_of_programmers

exept={'11','12','13','14'}

def ending(end_digit):
    return {
                end_digit == 0:     'программистов',
                end_digit == 1:     'программист',
                1 < end_digit < 5:  'программиста',
                5 <= end_digit <= 9:'программистов'
                
    }[True]

if number_of_programmers[-2:] in exept:
    print(int(number_of_programmers),'программистов')   
else:
    print(int(number_of_programmers),ending(int(number_of_programmers[-1])))
...   
   Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.
...
inp=input()+'\0'
#inp='helloll'+'\0'
class RLE:#enum
    state=0
    prev_symbol=1
    symbol_count=2
   
    init=0 #states
    counting=1

def init(x,p):
    p[RLE.prev_symbol]=x
    p[RLE.symbol_count]=1
    p[RLE.state]=RLE.counting
    return ''
def cntg(x,p):
    if p[RLE.prev_symbol]==x:
        p[RLE.symbol_count]+=1
        p[RLE.state]=RLE.counting
        return ''
    else:
        code=p[RLE.prev_symbol]+str(p[RLE.symbol_count])
        init(x,p)
        return code

struct=[RLE.init,'',0] #state, previous symbol, symbol count
   
states={
        RLE.init:lambda x,p:init(x,p),
        RLE.counting:lambda x,p:cntg(x,p)
       }
   
for i in inp:
    print(states[struct[RLE.state]](i,struct),end='')
 ...   
 Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
...
inp=[int(i) for i in input().split()]

class SUMM:#enum
    state=0
    index=1

    init=0 #states
    middle=1
    last=2

def init(x,p,i):
    if len(i)==1:
        return i[0]
    elif len(i)==2:
        p[SUMM.state]=SUMM.last
    else:
        p[SUMM.state]=SUMM.middle
    return i[-1]+i[1]

def middle(x,p,i):
    sum=i[p[SUMM.index]-1]+i[p[SUMM.index]+1]
    if len(i)-2==p[SUMM.index]:
        p[SUMM.state]=SUMM.last
   
    p[SUMM.index]+=1
    return sum

def last(x,p,i):
    return i[0]+i[-2]

struct=[SUMM.init,1] #state,index
   
states={
        SUMM.init:lambda x,p,i:init(x,p,i),
        SUMM.middle:lambda x,p,i:middle(x,p,i),
        SUMM.last:lambda x,p,i:last(x,p,i)
       }
   
for i in inp:
    #print(struct,i)
    print(states[struct[SUMM.state]](i,struct,inp),end='')
    print(' ',end='')
...
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые встречаются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
...
inp = [int(i) for i in input().split()]

input_table=[0]*30000000 #30,000,000 only 256Mb for us(
for i in inp:
    input_table[i]+=1
    if input_table[i]==2:
        print(i,end=' ')
        Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

inp=int(input())
lst=[]
for i in range(1,int(pow(inp,0.555))+3):#asymptotic upper bound x^0.555
       lst+=[i]*i
for i in lst[:inp]:
    print(i, end='')
    print(' ',end='')
