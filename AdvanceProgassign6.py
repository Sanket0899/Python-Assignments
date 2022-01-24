def find_difference(s1,s2):
    for i in s2:
        if i not in s1:
            print(i)

def count_datatypes(*args):
    int_count=0
    str_count=0
    bool_count=0
    list_count=0
    tuple_count=0
    dictionary_count=0
    for i in args:
        if type(i) == int:
            int_count=int_count+1
        elif type(i) == str:
            str_count=str_count+1
        elif type(i) == bool:
            bool_count = bool_count + 1
        elif type(i) == list:
            list_count = list_count + 1
        elif type(i) == tuple:
            tuple_count=tuple_count+1
        else:
            dictionary_count=dictionary_count+1
    return [int_count,str_count,bool_count,list_count,tuple_count,dictionary_count]

def fib_str(c,li):
    li.sort()
    new=[]
    new.append(li[0])
    new.append(li[1])
    count=0
    n1=li[0]
    n2=li[1]
    c=c-2
    while count<c:
        nth=n1+n2
        new.append(nth)
        n2=n1
        n1=nth

        count=count+1

    return new
def ones_threes_nines(n):
    li = []
    quo_9=0
    quo_3=0
    quo_1=0
    if(n>=9):
        rem=int(n%9)
        quo_9=int(n/9)
        li.append(quo_9)
        if(rem>=3):
            rem1=rem
            rem=int(rem%3)
            quo_3=int(rem1/3)
            quo_1=rem
            li.append(quo_3)
            li.append(quo_1)
        else:
            quo_1=rem
            li.append(quo_3)
            li.append(quo_1)




    return "nines:"+str(quo_9)+",threes:"+str(quo_3)+",ones:"+str(quo_1)

def fib(n):
    li=[]
    n1=0
    n2=1
    li.append(n1)
    li.append(n2)
    count=n-2
    while(count>=0):
        new=n1+n2
        li.append(new)
        n1=n2
        n2=new
        count=count-1
    return li[n]


find_difference("","a")
print(count_datatypes(1, 45, "Hi", False))
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) )
print(fib_str(5,["e","a"]))
print(ones_threes_nines(15))
print(fib(2))
