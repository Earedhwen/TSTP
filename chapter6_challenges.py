#Challenge 1

Camus = 'Camus'

for x in 'Camus':
    print(x)

#Challenge 2

noun = input("Enter a noun: ")
name = input("Enter a name: ")

response = "Yesterday I wrote a {}. I sent it to {}.".format(noun,name)
print(response)

#Challenge 3

mystring = "aldous Huxley was born in 1894."
mylist = mystring.split(" ",1)
mylist[0] = str(mylist[0]).capitalize()
mystring = mylist[0] + " " + mylist[1]

print(mystring)

#Challenge 4

mystring2 = "Where now? Who now? When now?"
mylist2 = mystring2.split("?")
for i in range(len(mylist2)):
    mylist2[i] += "?"
    mylist2[i] = mylist2[i].strip()
mylist2.pop()
print(mylist2)

#Challenge 5

mylist3 = ["The","fox","jumped","over","the","fence","."]
mylist3.pop()
mystring3 = " ".join(mylist3)
mystring3 += "."
print(mystring3)

#Challenge 6

mystring4 = "A screaming comes across the sky."
mystring4 = mystring4.replace('s','$')
print(mystring4)

#Challenge 7

mystring5 = "Hemingway"
print(mystring5.index('m'))

#Challenge 8

Luna = '"It\'s all right," said a dreamy voice from beside Harry as Ron ' + \
       'vanished into the coach\'s dark interior. "You\'re not going mad ' + \
       'or anything. I can see them too."'

print(Luna)

#Challenge 9

three = "three"

three1  = three + " " + three + " " + three
three2 = ((three + " ")*3).strip()
print(three1)
print(three2)

#Challenge 10

mylaststring = "It was a bright cold day in April, and the clocks were " + \
               "striking thirteen."
mylaststring = mylaststring[:33]
print(mylaststring)
