def solve(str1):
    dict_freq = {}
    for char in str1:
        if char in dict_freq:
            dict_freq[char] += 1
        else:
            dict_freq[char] = 1

    freq_list = []

    for val in dict_freq.values():
        freq_list.append(val)

    return freq_list

