import random

punkty_zycia = 10
punkty = 0

print("Witaj w grze **Poszukiwacz Diamentów**")
print("Twoim celem jest zdobycie 10 punktów, zanim stracisz wszystkie punkty życia")
print("Masz 10 punktów życia i startujesz z 0 punktami")
print("Powodzenia!\n")

while punkty_zycia > 0 and punkty < 10:
    kierunek = input("Wybierz: \n Prosto - w \n Do tyłu - s \n Lewo - a \n Prawo - d \n Sklep - q \n WPISZ: ")
    wydarzenie = random.choice(["npc", "diament", "potwór", "apteczka", "pusty", "npc", "npc"])
    if kierunek == "q":
        if punkty >= 2:
            print(f"Witaj w sklepie! \n Masz {punkty} diamentów. \n Możesz kupić: ")
            print("1. Mała mikstura życia (+1 hp) - koszt 2 diamenty")
            print("2. Duża mikstura życia (+2 hp) - koszt 3 diamenty")
            print("3. Wykrywacz diamentów (zwiększa szanse na znalezienie diamentów) - koszt 2 diamenty")
            wybor = input("Co chcesz kupić, wybierz 1, 2 lub 3: ")
            if wybor == "1" and punkty >= 2:
                punkty -= 2
                punkty_zycia += 1
                print("Kupiłeś małą miksturę życia. Masz teraz", punkty_zycia)
            elif wybor == "2" and punkty >= 3:
                punkty -= 3
                punkty_zycia += 2
                print("Kupiłeś dużą miksturę życia. Masz teraz", punkty_zycia)
            elif wybor == "3" and punkty >= 2:
                punkty -= 2
                wydarzenie.append("diament")
                print("Kupiłeś wykrywacz diamentów. Powodzenia w szukaniu!")
            else:
                print("Zła odpowiedź lub niewystarczające środki na koncie")
        else:
            print("Nie masz wystarczającej liczby punktów, aby odwiedzić sklep")
        continue

    if wydarzenie == "diament":
        punkty += 1
        print(f"Znalazłeś diament! Masz teraz {punkty} punktów")
    elif wydarzenie == "potwór":
        punkty_zycia -= 1
        print(f"Spotkałeś potwora i tracisz 1 punkt życia! Masz {punkty_zycia} punktów życia")
    elif wydarzenie == "apteczka":
        punkty_zycia += 2
        print(f"Znalazłeś apteczkę i zyskujesz 2 punkty życia! Masz {punkty_zycia} punktów życia")
    elif wydarzenie == "npc":
        npc_tekst = random.choice(["Carlos: Witaj przybyszu powodzenia w dalszej trasie!", "Maciek: Nie widziałeś może moich okularów?", "Szymon: Uważaj na potwora, słyszałem że mocno gryzie", "Stasik: Kim jesteś i co tu robisz?!?", "Dianka: Pomocy, pomocy potrzebuje pomocy", "Milana: Masz kilof? Daj mi kilof, proszę", "Ivan: Oddawaj diamenty!!!"])
        print("Spotkałeś postać NPC")
        print(npc_tekst)
    else:
        print("Pusty korytarz. Nic się nie dzieje.")
    print()

if punkty >= 10:
    print("Gratulacje wygrałeś")
elif punkty_zycia <= 0:
    print("Game over")