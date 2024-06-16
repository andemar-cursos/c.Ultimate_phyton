def word_process(string):
    no_spaces = delete_whitespaces(string.lower())
    character_map = count_characters(no_spaces)
    tuple_list = order_map_by_key(character_map)
    tuple_list_ordered = list_with_highest_value(tuple_list)
    print_solution(tuple_list_ordered)


def delete_whitespaces(string):
    return [valor for valor in string if valor != " "]


def count_characters(character_list):
    count_map = {}
    for character in character_list:
        if character not in count_map:
            count_map[character] = 1
        else:
            count_map[character] += 1

    return count_map


def order_map_by_key(character_map):
    return sorted(character_map.items(), key=lambda x: x[0])


def list_with_highest_value(tuple_list):
    highest_numer = 0
    ordered_list = []

    for tuple_element in tuple_list:
        if tuple_element[1] == highest_numer:
            ordered_list.append(tuple_element)
        elif tuple_element[1] > highest_numer:
            ordered_list = [tuple_element]
            highest_numer = tuple_element[1]

    return ordered_list


def print_solution(tuple_list_ordered):
    print(f"Los caracteres que mas se repiten con {tuple_list_ordered[0][1]} "
          f"repeticiones son:")

    for tuple_element in tuple_list_ordered:
        print(f"- {tuple_element[0]}")


word_process("chanchito feliz")

