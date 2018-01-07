# input

list_of_list = []

with open('input_question_5') as f_in:
    content = f_in.readlines()
content = [x.strip() for x in content]

for line in content:
    list_char = line.replace("Â","").split()
    list_int = list(map(int, list_char))
    list_of_list.append(list_int)

mul_vertical = []
mul_horizontal = []
mul_diag_dsc = []
mul_diag_asc = []

for r in range(len(list_of_list)):
    for c in range(len(list_of_list[r])):
        # sum of vertical
        if r < (len(list_of_list) - 3):
            mul_vertical.append(list_of_list[r][c] *
                                list_of_list[r + 1][c] *
                                list_of_list[r + 2][c] *
                                list_of_list[r + 3][c])

        # sum of horizontal
        if c < (len(list_of_list[r]) - 3):
            mul_horizontal.append(list_of_list[r][c] *
                                  list_of_list[r][c + 1] *
                                  list_of_list[r][c + 2] *
                                  list_of_list[r][c + 3])

        if r < (len(list_of_list) - 3) and \
                c < (len(list_of_list[r]) - 3):
            mul_diag_d = list_of_list[r][c] * \
                         list_of_list[r + 1][c + 1] * \
                         list_of_list[r + 2][c + 2] * \
                         list_of_list[r + 3][c + 3]
            mul_diag_dsc.append(mul_diag_d)

        if r > 2 and c < (len(list_of_list[r]) - 3):
            mul_diag_a = list_of_list[r][c] * \
                         list_of_list[r - 1][c + 1] * \
                         list_of_list[r - 2][c + 2] * \
                         list_of_list[r - 3][c + 3]
            mul_diag_asc.append(mul_diag_a)

greatest_vertical = max(mul_vertical)
greatest_horizontal = max(mul_horizontal)
greatest_diag_dsc = max(mul_diag_dsc)
greatest_diag_asc = max(mul_diag_asc)

f_out = open('output_question_5', 'w')
f_out.write(str(max(greatest_vertical,greatest_horizontal,greatest_diag_dsc,greatest_diag_asc)))
f_out.close()
