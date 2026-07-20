from Lesson1_remember.Remember import result

shopping_card = ['orange','peach','lemon']
empty_list = []
mixed =[2,'orange',4.22,True]
#*************************

fruits = ['orange','peach','lemon']
print(fruits)

fruits = ['orange','peach','lemon']
print(fruits[0])

fruits[1] = 'blueberry'
print(fruits)
print()

list1 = ['orange', 'peach']
list2 = ['shampoo','soap']
comb_list = list1+list2
print(comb_list)
print()

fruits = ['orange','peach','lemon']
fitst, second, third = fruits
print(fitst)
print(second)
print(third)
print()

fruits = ['orange','peach','lemon']
for item in fruits:
    print(f"item in fruits:{item}")

correct_answers = ['orange','peach','lemon']
user_answers = ['orange','peach','lemon']

if correct_answers == user_answers:
    print("All answers are correct")
else:
    print("Some answers are incorrect")

print(len(fruits))
print(max(fruits))
print(min(fruits))

numbers = [12,56,94,6]
print(max(numbers))
print(min(numbers))

#sorted - переворачивает строку
res = sorted(numbers)
print(res)
print(numbers)
print(sorted(numbers, reverse=True))

print(sorted(fruits, reverse=True))

word = 'pyThon'
print(sorted(word))
result = ''.join(sorted(word))
print(result)

#правило сортировки
names = ['Alexander', 'Bob', 'Tom']
print(sorted(names))
print(sorted(names,key=len))

# sort - только у листа, меняет список
# sorted - создает новый лист, но не меняет старую колекцию

#appendet - добавить в список в конец
fruits = ['orange','peach','lemon']
fruits.append("orange")
print(fruits)

#insert - добавить в строку
fruits.insert(2,'apple')
print(fruits)

#index - добавлять нумерацию
#first_peach_index = first.

numbers = [10,20,30,]
deleted = numbers.pop(1)
print(deleted)
print(numbers)
numbers.clear()
print(numbers)




















