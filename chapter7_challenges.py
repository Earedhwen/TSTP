import random

#Challenge 1

filmlist = ["The Walking Dead","Entourage","The Sopranos","The Vampire Diaries"]
for film in filmlist:
    print(film)

#Challenge 2

for i in range(25,51):
    print(i)

#Challenge 3

for i in range(len(filmlist)):
    print(i,filmlist[i])

#Challenge 4

numberlist = [random.randint(1,20) for i in range(10)]
while True:
    guess = input("Guess a number or press q to quit ")
    if guess == 'q':
        break
    elif int(guess) in numberlist:
        print("Your guess is in my list!")
    else:
        print("You guessed incorrectly.")
    
#Challenge 5

list1 = [8,19,148,4]
list2 = [9,1,33,83]

list3 = []

for i in range(len(list1)):
    for j in range(len(list2)):
        list3.append(list1[i]*list2[j])

print(list3)
