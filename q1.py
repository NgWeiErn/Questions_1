import pandas as pd
import numpy as np

list_of_tuples = []

with open('input_question_1') as f_in:
    content = f_in.readlines()
content = [x.strip() for x in content]

for line in content:
    list_char = line.split()
    tuple_int = tuple(map(int, list_char))
    list_of_tuples.append(tuple_int)

labels = ['employee', 'age', 'salary', 'service']

df = pd.DataFrame.from_records(list_of_tuples, columns = labels)

# part a

smallest_age = df['age'].min()
largest_age = df['age'].max()

# part b

salary_mean = df['salary'].mean()
salary_standard_deviation = np.std(df['salary'].values) # .values returns np array object

# part c

# sorted by age
df_sorted_by_age = df.sort_values(by='age')

# sorted by salary
df_sorted_by_salary = df.sort_values(by='salary')

# sorted by service
df_sorted_by_service = df.sort_values(by='service')

# Write file
f_out = open('output_question_1', 'w')

f_out.write(str(smallest_age) + " " + str(largest_age) + "\n\n")
f_out.write(str(salary_mean) + " " + str(salary_standard_deviation) + "\n\n")

for row, series in df_sorted_by_age.iterrows():
    string = str(series[0]) + " " + str(series[1]) + " " + str(series[2]) + " " + str(series[3]) + "\n"
    f_out.write(string)
f_out.write("\n")

for row, series in df_sorted_by_salary.iterrows():
    string = str(series[0]) + " " + str(series[1]) + " " + str(series[2]) + " " + str(series[3]) + "\n"
    f_out.write(string)
f_out.write("\n")

for row, series in df_sorted_by_service.iterrows():
    string = str(series[0]) + " " + str(series[1]) + " " + str(series[2]) + " " + str(series[3]) + "\n"
    f_out.write(string)
f_out.close()

# f_out.write(df_sorted_by_age.to_string(header=False, index=False, col_space=0, justify='right') + "\n\n")
# f_out.write(df_sorted_by_salary.to_string(header=False, index=False) + "\n\n")
# f_out.write(df_sorted_by_service.to_string(header=False, index=False))
