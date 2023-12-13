# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def dividirMayus(s):
    res = []
    i = 0
    while True:
        if i >= len(s):
            res.append(s)
            break
        elif s[i].isupper() and i!=0:
            res.append(s[:i])
            s=s[i:]
        i+=1
    return res  

def combineVariable(s):
    s = s.split()
    res = s[0].lower()
    s = s[1:]
    for i in s:
        res+=i[0].upper()+i[1:]
    return res

def camelCase(listString):
    for i in listString:
        operation = i[0]
        typeData = i[2]
        s = i.split("\r\n")[0][4:]
        if operation == "S":
            nombres = dividirMayus(s)
            acum = ''
            if typeData == 'M':
                nombres[-1] = nombres[-1][:-3]
            for nombre in nombres:
                acum += nombre.lower() + ' '
            print(acum)
        elif operation == 'C':
            if typeData == 'V':
                print(combineVariable(s))
            elif typeData == 'M':
                print(combineVariable(s)+'()')
            elif typeData == 'C':
                name = combineVariable(s)
                print(name[0].upper()+name[1:])

if __name__ == '__main__':
    listString = sys.stdin.readlines()
    camelCase(listString)
