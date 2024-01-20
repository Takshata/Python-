
###Some basic while loop snippets###

### printing the name 'Hi nice to meet you 10 times###

i=1
while i<=10:
    print('Hi nice to meet you!')
    i=i+1
    print('Done')


###printing the numbers 1 to 10 
i=1
while i<=10:
    print(i)
    i=i+1


###lets create a function which takes numbers 1 to n and prints them accordingly
def print_m_n(m,n):
    i=m
    while i<=n:
        print(i)
        i=i+1
print_m_n(10,20)


def printing_m_n(m:int,n:int):
    #Since we will be having two numbers there will be an input where first number is higher so sorting it accordingly
    start=m if m<n else n
    end=n if m<n else m
    while start<=end:
        print(start)
        start+=1
printing_m_n(1,10)
