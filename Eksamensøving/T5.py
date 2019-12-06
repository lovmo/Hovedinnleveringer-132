
def antV(setning):
    vokaler = 'aeiouyæøå'
    counter = 0
    for i in setning:
        if i in vokaler:
            counter += 1
    return counter


TV= \
'''
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari

pekto: vetle
neisann: jo


perko: s
'''

def filt(i):
    if len(i) != 2:
        return False
    else:
        return True

def fagf(verv, navn):
    l = verv.split('\n')
    l = l[2::]
    m = [i.split(':') for i in l]
    m = filter(filt, m)
    k = [i for i in m]
    v = {}
    for i in k:
        if i[1][1::] not in v.keys():
            v.update({i[1][1::]: [i[0]]})
        else:
            v[i[1][1::]].append(i[0])
    if navn in v:
        return v[navn]
    else:
        return v
