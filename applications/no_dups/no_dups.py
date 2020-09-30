def no_dups(s):
    # Your code here
    bob = []
    bob2 = ''
    words = s.split()

    for n in words:
        if n not in bob:
            bob.append(n)
    
    for n in range(len(bob)):
        if len(bob2) == 0:
            bob2 = bob[n]
        else:
            bob2 += " " + bob[n]

    return(bob2)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
