
s = input("Type the parentheses string: ")

openning = []

ok = True

for ch in s:
    if ch in '[({':
        openning.append(ch) 
    else:
        if (len(openning) > 0):
            last = openning[-1]
            openning.pop(-1)
            if (ch == ']' and last != '[') or \
                (ch == ')' and last != '(') or \
                (ch == '}' and last != '{'):
                ok = False
                break
        else:
            ok = False
            break

if ok:
    if len(openning) != 0:
        ok = False

if ok:
    print("VALID")
else:
    print("INVALID")


