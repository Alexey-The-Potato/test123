stroka = str(input())
def palindrom(n):
    for i in range(len(n)):
        if n[i] != n[-(i+1)]:
            return 'False'
    return 'True'

print(palindrom(stroka))