# input

list_of_list = []

with open('input_question_2') as f_in:
    content = f_in.readlines()
content = [x.strip() for x in content]

for line in content:
    list_char = line.split()
    list_int = list(map(int, list_char))
    list_of_list.append(list_int)

# recursive function
def answer(n, x):
    if n == 0:
        return 1
    else:
        return x**n + answer(n-1, x)

# logic

answers = []

for ls in list_of_list:
    n = ls[0]
    x = ls[1]
    answers.append(answer(n,x))

# output
f_out = open('output_question_2', 'w')

for idx in range(len(list_of_list)):
    f_out.write(str(list_of_list[idx][0]) + " " + str(list_of_list[idx][1]) + " " + str(answers[idx]) + "\n")

f_out.close()