# Ordbøker oppgaver fra boken

# 2

def mail(fil):
    with open(fil, 'r', encoding='utf-8-sig') as adr:
        ind = [i.strip().split(' ') for i in adr if i.startswith('From') and len(i.strip().split(' '))>4]
        ordbok = {}
        for i in ind:
            if i[2] not in ordbok.keys():
                ordbok.update({i[2]: 1})
            else:
                ordbok[i[2]] += 1
        return ordbok
    
k = mail('mbox-short.txt')

for i in sorted(k):
    print(i, k[i])

def mail1(fil):
    with open(fil, 'r', encoding='utf-8-sig') as adr:
        ind = [i.strip().split(' ') for i in adr if i.startswith('From') and len(i.strip().split(' '))>4]
        ordbok = {}
        for i in ind:
            if i[1] not in ordbok.keys():
                ordbok.update({i[1]: 1})
            else:
                ordbok[i[1]] += 1
        return ordbok
    
j = mail1('mbox.txt')

print(max(j), j[max(j)])


def mail2(fil):
    with open(fil, 'r', encoding='utf-8-sig') as adr:
        ind = [i.strip().split(' ') for i in adr if i.startswith('From') and len(i.strip().split(' '))>4]
        adr = [i[1].split('@') for i in ind]
        ordbok = {}
        for i in adr:
            if i[1] not in ordbok.keys():
                ordbok.update({i[1]: 1})
            else:
                ordbok[i[1]] += 1
        return ordbok
    
j = mail2('mbox-short.txt')

for i in sorted(j):
    print(i, j[i])
