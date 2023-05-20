def f_reverseWords (inputstr):
    wordlist = inputstr.split(" ")
    rev = ""
    for w in wordlist:
        for i in range(len(w) - 1, -1, -1):
            rev += w[i]
        rev += " "
    rev = rev[:-1]
    return rev

if __name__ == "__main__":
    inputstr = input()
    print(f_reverseWords(inputstr))