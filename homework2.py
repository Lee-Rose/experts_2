print('-------------- Task 1 -------------')

list_id = ['Liya', 'Yoelson', 'age_30', 'Python']
for item in list_id:
    print(item)

print('-------------- Task 2 -------------')

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
new_list = []
index = 0
if len(list1) == len(list2):
    for i in list1:
        if i >= list2[index]:
            new_list.append(i)
            index += 1
        else:
            new_list.append(list2[index])
            index += 1
    print(new_list)
else:
    print('Strings of different lengths')


print('-------------- Task 3 -------------')

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_even_num = []
list_odd_num = []

for a in list_num:
    if type(a) == int:
        if a % 2 == 0:
            list_even_num.append(a)
        else:
            list_odd_num.append(a)
    elif type(a) == str:
        print('It’s a string!!!')
        list_even_num = []
        list_odd_num = []
        break
print(f'Number of even numbers : {len(list_even_num)} \nNumber of odd numbers : {len(list_odd_num)}')

print('-------------- Task 4 -------------')

def sum_numbers(list):
    sum_num = 0
    for b in list:
        sum_num += b
    print(sum_num)
sum_numbers([1, 4, 6, 12, 56, 72, 11, 8, 16])

print('-------------- Task 5 -------------')

def multiply(list):
    mult_num = 1
    for c in list:
        mult_num *= c
    print(mult_num)

multiply([1, 2, 3, 13, 52, 4, 14, 7])

print('-------------- Task 6 -------------')

def min_counter(list):
    min_count = list[0]
    for d in list:
        if d < min_count:
            min_count = d
    print(min_count)

min_counter([4, 6, 12, 3, 8, 67, 55])

print('-------------- Task 7 -------------')

my_string = 'Alex Kuznetsov'
upper_characters = 0
lower_characters = 0

for x in my_string:
    if  x.isupper():
        upper_characters += 1
    elif x.islower():
        lower_characters += 1
print(f'No. of Upper case characters: {upper_characters} \nNo. of Lower case Characters: {lower_characters}')

print('-------------- Task 8 -------------')

def unique_elements(list):
    newlist = []
    for y in list:
        if y not in newlist:
            newlist.append(y)
        else:
            pass
    print(newlist)

unique_elements([1, 2, 3, 3, 3, 3, 4, 5])

print('-------------- Task 9 -------------')

step = 8
for s in range(1, step + 1):
    for w in range(1, s + 1):
        print(w, end= ' ')
    print('')

print('-------------- Task 10 -------------')

