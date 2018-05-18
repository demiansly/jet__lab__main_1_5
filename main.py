import pandas as pd

print('Hello World')

file_test = open('C:/Users/pv.ivanov/PycharmProjects/jet__lab__main_1_5/cod-wan-gw1.txt')

sample_lines = file_test.readlines()

#print('sample_lines = ',sample_lines[0])
#print('sample_lines = ',sample_lines[1])

#print(len(sample_lines[0]))

#Счётчик строк в файле
line_number = 0

#Номер символа найденной строки
bingo = 0

#Счётчик количества найденных строк
counter_finded_lines = 0

try:
    len(sample_lines[line_number])
except:
    print ('array is end')
else:
    while 1 < 2:
        try:
            len(sample_lines[line_number])
        except:
            print('array is end')
            break
        else:

            lab_find = "ip address"

            bingo = sample_lines[line_number].find(lab_find)
            if bingo > 0:
                print('bingo = ',bingo)
                bingo = 0;
                counter_finded_lines = counter_finded_lines + 1

            line_number = line_number + 1


print ('counter_finded_lines = ', counter_finded_lines)
print ('success')
