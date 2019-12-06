
favorittForfattere={'Per':'Christie','Kari':'Ibsen', 'Liv':'Rowling','Ola':'Ibsen', 'Anne':'Allende', 'Jens':'Christie'}

# A.

def forfatterListe(forfdict):
    forfattere = []
    for forfatter in forfdict.values():
        if forfatter not in forfattere:
            forfattere.append(forfatter)
    return sorted(forfattere)

# B.

def fans(forfdict):
    f_dict = {}
    for navn in forfdict.items():
        if navn[1] not in f_dict.keys():
            f_dict.update({navn[1]: [navn[0]]})
        else:
	    f_dict[navn[1]].append(navn[0])
    return f_dict

# C.

def favbøker(forfdict, fil):
    with open(fil, 'r', encoding='utf-8-sig') as fil:
        bøker = {}
	ferdig_d = {}

	bøker_l = [i.strip().split(',') for i in fil]
	
	for item in bøker_l:
            if item[0] not in bøker.keys():
		bøker.update({item[0]: [item[1]]})
	    else:
		bøker[item[0]].append(item[1])
		
	for navn in forfdict:
            for forfatter in bøker:
                if forfatter in forfdict[navn]:
                    ferdig_d.update({navn: bøker[forfatter]})
                    
	return ferdig_d

# D.

# b = favbøker(favorittForfattere, 'forfattere.txt')

def skriv(b):
    for navn in b:
        print(f'{navn}----')
        for i in b[navn]:
	    print(i)




# d)

def liste1(liste):
    for verdi in liste:
        print(verdi)

def liste3(liste):
    ny_liste = [[i:i+3] for i in range(0, len(liste), 3) if len([i:i+3]) == 3]
    for verdier in ny_liste:
        print(verdier)


















