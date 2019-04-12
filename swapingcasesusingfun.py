def swap_case(l):
    x=[]
    for i in range(len(l)):
        if l[i].islower():
            x.append(l[i].upper())
        elif l[i].isupper():
            x.append(l[i].lower())
        else:
            x.append(l[i])

    return(''.join(x))



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
