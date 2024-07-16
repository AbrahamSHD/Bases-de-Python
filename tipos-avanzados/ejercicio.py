from pprint import pprint

string = "Este es mi string"


def delete_space(text):
    return [char for char in text if char != ' ']


no_spaces = delete_space(string)
pprint(no_spaces)


def num_chars(list_of_letters):
    char_dict = {}
    for char in list_of_letters:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_in_tuples(dictionary):
    return sorted(
        dictionary.items(),
        key=lambda key: key[1],
        reverse=True,
    )


def greatest_tuples(list_of_tuples):
    maxm = list_of_tuples[0][1]
    response = {}
    for order in list_of_tuples:
        if maxm > order[1]:
            break
        response[order[0]] = order[1]
    return response


def create_message(dictionary):
    message1 = 'Los que más se repiten son: \n'
    for key, value in dictionary.items():
        message1 += f"- {key} con {value} repeticiones"
    return message1


count = num_chars(no_spaces)
organized = sort_in_tuples(count)
greatest = greatest_tuples(organized)
message = create_message(greatest)
pprint(f"Tuplas organizadas {organized}")
pprint(f"Tuplas más grandes {greatest}")
print(message)
