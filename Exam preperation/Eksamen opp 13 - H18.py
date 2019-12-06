def filform(fil):
    with open(fil, 'r', encoding='utf-8-sig') as fil:
        l = [i.strip().split(';') for i in fil]
        for i in l:
            i.insert(3, float(i.pop(3)))
        tup = [tuple(i) for i in l]
        return tup
    
        
def funk(tup):
    fin = {}
    for i in tup:
        if i[0] not in fin.keys():
            fin.update({i[0]: [(i[2],i[3])]})
        else:
            fin[i[0]].append((i[2],i[3]))
    return fin

def salgs(di, dato):
    salg = [i[1] for i in di[dato]]
    return f'Evalueres til {salg}'

def sumsalg(di, datoer):
    ut = []
    for dato in datoer:
        if dato in di:
            for i in di[dato]:
                ut.append(i[1])
                
    ut_text = '+'.join([str(i) for i in ut])
    
    return f'som gir {sum(ut)} ({ut_text})'
            


x =filform('hei.csv')
y = funk(x)
