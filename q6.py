# generate 10-bit binary sequence
import itertools

bin_sequences = ["".join(seq) for seq in itertools.product("01", repeat=10)]

# logic
same_pair_counts = []

for seq in bin_sequences:
    count = 0
    
    for i in range(0, 10):
        if i != 0:
            if seq[i] == prev:
                count += 1
        if i != 9:
            prev = seq[i]

    same_pair_counts.append(count)

set_same_pair_counts = set(same_pair_counts)
unique_same_pair_counts = list(set_same_pair_counts)
unique_same_pair_counts.sort()

frequency = []

for pair_count in unique_same_pair_counts:
    frequency.append(same_pair_counts.count(pair_count))

f_out = open('output_question_6', 'w')

for idx in range(len(frequency)):
    f_out.write(str(unique_same_pair_counts[idx]) + " " +
                str(frequency[idx]) + "\n")

f_out.close()
