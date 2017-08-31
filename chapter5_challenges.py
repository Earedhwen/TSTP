musicians = ['David Harris', 'Idina Menzel', 'Folk On', 'Alan Menken', \
             'Andrew Lloyd Webber', 'Tim Rice', 'Lin-Manuel Miranda']

places = [(52.47,-1.89),(54.40,-3.48),(54.05,-2.80),(54.77,-1.58)]

me = {'name': "Hannah Ruth Charman", 'DoB': "05/07/1997", \
      'height': "1.68m", 'hair': "brown", 'eyes': "grey", \
      'colour': "blue", 'subject': "mathematics", 'author': "J. K. Rowling", \
      'game': "Professor Layton", 'film': "The Lord of the Rings"}

question = input("Would you like to know my height, favourite colour " + \
                 "or favourite author? ")
if 'height' in question:
    print(me['height'])
elif 'colour' in question:
    print(me['colour'])
elif 'author' in question:
    print(me['author'])
else:
    print("That is not a valid option.")

music = {'David Harris': 'Goodnight My Angel', \
         'Idina Menzel': 'Defying Gravity', \
         'Folk On': 'Alright', \
         'Susan Egan': 'A Change in Me'}

#Sets are used if infortmation will not be repeated.
