def f_reverseString (inputstr):
    rev = ""
    for i in range(len(inputstr) - 1, -1, -1):
        rev += inputstr[i]
    return rev

if __name__ == "__main__":
    inputstr = input()
    print(f_reverseString(inputstr))