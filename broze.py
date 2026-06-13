code = input()

result = ""
i = 0

while i < len(code):

    if code[i] == ".":
        result += "0"
        i += 1

    elif code[i:i+2] == "-.":
        result += "1"
        i += 2

    else:
        result += "2"
        i += 2

print(result)
