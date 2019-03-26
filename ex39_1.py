# dict wojewódzctwa: miasta
woj = {
    'Donlośląskie': 'Wrocław',
    'Kujawsko-pomorskie': 'Bydgoszcz',
    'Lubelskie': 'Lublin',
    'Lubuskie': 'Gorzów Wielkopolski',
    'Łódzkie': 'Łódź',
    'Małopolskie': 'Kraków',
    'Mazowieckie': 'Warszawa',
    'Opolskie': 'Opole',
    'Podkarpackie': 'Rzeszów',
    'Podlaskie': 'Białystok',
    'Pomorskie': 'Gdańsk',
    'Śląskie': 'Katowice',
    'Świętokrzyskie': 'Kielce',
    'Warmińsko-mazurskie': 'Olsztyn',
    'Wielkopolskie': 'Poznań',
    'Zachodniopomorskie': 'Szczecin'
}

# dict województwa: symobole literowe
rejestr = {
    'D': 'Donlośląskie',
    'C': 'Kujawsko-pomorskie',
    'L': 'Lubelskie',
    'F': 'Lubuskie',
    'E': 'Łódzkie',
    'K': 'Małopolskie',
    'W': 'Mazowieckie',
    'O': 'Opolskie',
    'R': 'Podkarpackie',
    'B': 'Podlaskie',
    'G': 'Pomorskie',
    'S': 'Śląskie',
    'T': 'Świętokrzyskie',
    'N': 'Warmińsko-mazurskie',
    'P': 'Wielkopolskie',
    'Z': 'Zachodniopomorskie'
}

for w, m in list(woj.items()):
    print(f"Stolicą {w} jest miasto: {m}.")

print("-" * 10)

for l, w in list(rejestr.items()):
    print(f"Województwo {w} symbolizowane jest literą: {l}.")

print("-" * 10)

user_city = input("Twoje miasto: \n> ")
# user_city = 'Warszawa' 

# the simplest way
#for i, j in list(woj.items()):
    #if j == user_city:
        #found = True
        #break
    #else:
        #found = False

#if not found:
    #print("Miasto nie występuje w bazie.")
    #exit()
#else:
    #print(f"Twoje województwo: {i}")


# the best way is to swap key-variables making new dictionary
woj_rev = {val:key for (key, val) in woj.items()}
try:
    user_woj = woj_rev[str(user_city)]
except:
    print("Nie znaleziono miasta.")
    exit()

print(f"Twoje województwo: {woj_rev[str(user_city)]}")  

rejestr_rev = {val:key for (key, val) in rejestr.items()}
print(f"Symbol literowy województwa: {rejestr_rev[user_woj]}")
