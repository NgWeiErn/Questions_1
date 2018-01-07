def main():
    ls = []
    for num in range(1, 1000):
        if num%3 == 0 or num%5 == 0:
            ls.append(num)

    f_out = open('output_question_4', 'w')
    f_out.write(str(sum(ls)))
    f_out.close()

if __name__ == '__main__':
    main()