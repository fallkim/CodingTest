def solution(my_string, queries):
    char_list = list(my_string)
    for i,j in queries:
        char_list[i:j+1] = char_list[i:j+1][::-1]
    return ''.join(char_list)