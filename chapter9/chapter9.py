import csv

text = open('chapter9.txt','w')
text.write('Hi from Python!')
text.close()

with open('chapter9.txt','r') as text:
    message = text.read()
    print(message)

with open('chapter9.csv','w',newline='') as text:
    w = csv.writer(text, delimiter = ',')
    w.writerow(['one','two','three'])
    w.writerow(['four','five','six'])

with open('chapter9.csv','r') as text:
    r = csv.reader(text, delimiter = ',')
    for row in r:
        print(",".join(row))
