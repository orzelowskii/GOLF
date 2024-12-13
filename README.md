# Projekt Gry 'Golf' - README\

## Opis Projektu

"Golf" to cyfrowa wersja strategicznej gry karcianej, której celem jest osiągnięcie jak najniższej liczby punktów poprzez zarządzanie kartami.

## Zasady Gry

1. Talia: Gra wykorzystuje standardową talię 52 kart.

2. Rozgrywka:
- Każdy gracz otrzymuje 5 kart (twarzą w dół).
- Na początku gracze podglądają 2 z 5 kart.
- W swojej turze gracz może dobierać, wymieniać lub odrzucać karty.

3. Celem gry jest minimalizacja punktów poprzez odpowiednie zagrania.

4. Wartości kart:
- As = 1 punkt
- Król = 0 punkt
- Karty 2-10 = wartość nominalna
- Walet = 11 punktów, Dama = 15 punktów

5. Koniec Gry: Gra kończy się, gdy gracz ogłosi "GOLF" lub skończą się karty w talii. Wygrywa osoba z najmniejszą liczbą punktów.

## Struktura Projektu
- Game.py: Logika gry.
- Menu.py: Obsługa menu i interfejsu.
- Objects.py: Definicje obiektów (gracze, karty, talia).
