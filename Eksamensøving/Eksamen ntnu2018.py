## EKSAMEN NTNU PYTHON

data = [['Customer','vase', 'maleri','sykkel','lego','tv'],
        ['Per',100,0,200,0,1500],
        ['Ida',110,50,200,0,1500],['Ottar',200,600,200,0,1700],
        ['Dag',200,600,200,0,1700],
        ['Lise',400,600,0,0,0]]


def item_offers(obj, data):
    indeks = data[0].index(obj)
    n = data[1::]
    ut_data = []

    for i in n:
        ut_data.append([i[0],i[indeks]])
        
    return ut_data

k = item_offers('sykkel', data)

        
def vinner(obj, data):
    indeks = data[0].index(obj)
    n = data[1::]
    ut_data = {}

    for i in n:
        ut_data.update({i[0]: i[indeks]})
    
    x = list(sorted(ut_data.items(), key=lambda x: x[1], reverse=True))
    return x[0]
                    
                    

v = vinner('tv', data)

def all_vinne(data):
    vinnere = {}
    objekter = data[0][1::]

    for obj in objekter:
        indeks = objekter.index(obj)+1
        personer = []
        for navn in data[1::]:
            personer.append([navn[0], navn[indeks]])
        vinner = list(sorted(personer, key=lambda x: x[1], reverse=True))
        if vinner[0][1] == 0:
            vinnere.update({obj: []})
        else:
            vinnere.update({obj: vinner[0]})
    return vinnere

alle = all_vinne(data)


def file_to_table(fil):
    with open(fil, 'r', encoding='utf-8-sig') as biler:
        biler = [i.strip().split(',') for i in biler]
        for elementer in biler:
            for i in elementer[0:-1]:
                indeks = elementer.index(i)
                elementer.insert(indeks, int(elementer.pop(indeks)))
        return biler

x = file_to_table('box_a.txt')
               

def formatTime(s):
    t = str(int(s)/3600)
    timer = t[0]
    minutter = str(float('0'+t[1::])*60)
    sekunder = str(float('0'+))
    return f'{timer}: {minutter}'
    

g = formatTime(12305)
print(g)


    



































            

    
