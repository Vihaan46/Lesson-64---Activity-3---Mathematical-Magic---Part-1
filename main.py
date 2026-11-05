def romantoInt(ri):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    resultinteger = 0

    for i in range(len(ri)):
        if i > 0 and roman[ri[i]] > roman[ri[i - 1]]:
            resultinteger += roman[ri[i]] - 2 * roman[ri[i - 1]]
        else:
            resultinteger += roman[ri[i]]
    return resultinteger

roman = input("Input roman numeral: ")
print("Integer value is:", romantoInt(roman))