fw = open('question_bank.txt', 'w')
fw.write('How are you\n')
fw.write('How to determine birth order\n')
fw.close()

fr = open('question_bank.txt', 'r')

def write_stuff():
    x = 'baby bonus\n'
    return x

fa = open('test.txt', 'a')

for i in range(0, 3):
    fa.write(write_stuff())

myList = []
for line in fr:
    myList.append(line)
print(myList)
