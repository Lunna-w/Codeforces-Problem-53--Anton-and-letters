input_string=str(input())

def count_unique_letters(string):

    string = string.replace("{", "").replace("}", "").replace(" ", "")

    unique_letters = set(string)

    return len(unique_letters)



unique_letter_count = count_unique_letters(input_string)

if unique_letter_count-1 == -1:
    print(0)
elif unique_letter_count-1 == 0:
    print(1)
else:
    print(unique_letter_count-1)



