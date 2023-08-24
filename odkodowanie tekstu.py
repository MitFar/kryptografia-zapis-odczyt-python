import os
path = "Zakodowany.txt"
path2 = "Odkodowany.txt"

print("Witaj w systemie domowego kodowania!\n1)Wciśnij 1 aby wpisać ścieżkę do odczytu i zapisu\n2)Jeśli chcesz wybrać domyślną ścieżkę(Zakodowany.txt i Odkodowany.txt) wybierz 2 \n3)Jeśli chcesz opuścić program wybierz dowolny inny klawisz")
klawisz = input()
if klawisz == '1':
    path = input('Podaj scieżkę do odczytu\n')
    print(path)
    if os.path.exists(path):
        path2 = input("Podaj scieżke do zapisu\n")
        if os.path.exists(path2):
            print(path2)
        else:
            print("Taka ścieżka nie istnieje!\nProgram zamyka się!")
            input()
            exit()
    else:
        print("Taka ścieżka nie istnieje!\nProgram zamyka się!")
        input()
        exit()
elif klawisz == '2':

    print(path, path2)
else:
    print("Program zakończył się")
    input()
    exit()


with open(path, 'r') as plik:
    zawartosc_pliku = plik.read()
    print ('Ilość wszystkich wyrazów w tekście:', len(zawartosc_pliku.split()))
    string = zawartosc_pliku
    letters = len(string)
    print("ilość znaków", letters)
f = open(path, "r")
g = open(path2, "a")
znak = f.read()
tablica =[znak]
tablica_znaki=[]
tablica_ascii=[]
tablica_kodowa=[]
tablica_odkodowana=[]
print (tablica[0])
for i in range(0, letters):
    tablica_znaki.append(znak[i])
    print(tablica_znaki[i])
    tablica_ascii.append(ord(tablica_znaki[i]))
    tablica_kodowa.append(tablica_ascii[i]-2)
    tablica_odkodowana.append(chr(tablica_kodowa[i]))
    print (tablica_odkodowana[i])
    g.write(tablica_odkodowana[i])
f.close()
g.close()
print("Program zakończył działanie, wciśnij dowolny klawisz aby zamknąć okno")
end=input()