#!/usr/bin/python3
def roman_to_int(roman_string):
    rmn_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    if not isinstance(roman_string, str):
        return 0
    for i in range(len(roman_string)):
        idx_c = roman_string[i]
        idx_p = roman_string[i - 1]
        if i > 0 and rmn_d[idx_c] > rmn_d[idx_p]:
            sum += rmn_d[idx_c] - 2 * rmn_d[idx_p]
        else:
            sum += rmn_d[idx_c]
    return (sum)
