# Analiza Algorytmów - Projekt - Głęboka analiza złożoności obliczeniowej podstawowych operacji na tablicy mieszającej z wykorzystaniem własnej implementacji generatora pseudo-słów bazującej na próbce języka polskiego.
Projekt wykonany w ramach przedmiotu AAL (Analiza Algorytmów) w semestrze 2020Z (5 semestr), na kierunku Informatyka, specjalizacji Inżynieria Systemów Informacyjnych (ISI) na Wydziale Elektroniki i Technik Informacyjnych (EiTI) Politechniki Warszawskiej.

**Prowadzący projekt**: dr Grzegorz Blinowski 
**Ocena implementacji**: 20/20

## Autorzy
Lukasz Pokorzyński, nr 300251  
l.pokorzynski@stud.elka.pw.edu.pl  
Adam Steciuk, nr 300263  
adam.steciuk.stud@pw.edu.pl

## Temat projektu
Wariant W11 i W21  
Przedmiotem analizy jest tablica mieszająca: tablica przechowuje rekordy zawierające napisy. Długość
tablicy jest ograniczona arbitralnie przez pewną stałą K. Dla danego napisu s obliczamy k=M(s) gdzie
M() jest funkcją mieszającą i umieszczamy strukturę reprezentującą napis w tablicy mieszającej: H[k].
W przypadku kolizji funkcji mieszającej (H[k] zajęte) reprezentujące napis s struktury danych
zapisywane są w liście jednokierunkowej, której głowa to H[k]. Przedmiotem implementacji powinno być:
dodanie i usunięcie elementów w H[].

Zastosować jedną funkcję mieszającą; dodatkowo przeprowadzić analizę dla enumeracji tablicy
(wydobycia wszystkich elementów). Wybór funkcji mieszającej M(s) do decyzji projektanta.

Testy przeprowadzić dla: sztucznie wygenerowanych słów, generator ma posługiwać się tablicą
prawdopodobieństw wystąpienia danej litery na początku słowa (początek słowa) oraz litery po
poprzedzającej literze, (spacja, kropka, przecinek, itp. traktowane są jako litera specjalna "koniec
słowa"). Prawdopodobieństwa należy uzyskać z próbki tekstu polskiego.

## Obsługa programu
Program jest uruchamiany z linii poleceń interpretera Python w następujący sposób:

main.py [-h] -m {1,2,3} -i INPUT [-d DELETE] [-n NUMBER] [-s SEED]

-h: opcja wyświetlająca tekst pomocniczy objaśniający działanie programu i pobierane parametry  
-m: tryb wykonywania programu:  
    1) z dostarczeniem danych wejściowych  
    2) z automatyczną generacją danych i analizą wyników  
    3) z automatyczną generacją danych przy pomocy wartości krokowej oraz analizą i stosownym wyświetleniem wyników  
-i: przekazanie pliku z danymi wejściowymi do programu, dla trybu 1 są to gotowe słowa, dla trybów 2 i 3 jest to próbka
tekstu polskiego do automatycznej generacji słów  
-d: parametr opcjonalny; przekazanie pliku zawierającego słowa do operacji usuwania, jeżeli taki plik nie zostanie
przekazany, to program spyta użytkownika, czy użyć słów przekazanych/wygenerowanych  
-n: parametr opcjonalny; maksymalna liczba słów do wygenerowania, domyślnie liczba 1000  
-s: parametr opcjonalny; ziarno generatora losowego, domyślnie nie jest przekazywane

Dla wszystkich trybów wykonania program spyta o liczbę list jednokierunkowych składających się na tablicę mieszającą.  
W trybie 3 program dodatkowo spyta o wartość krokową.

## Dane wejściowe
Danymi wejściowymi powinny być słowa rozdzielone spacjami lub innymi znakami białymi dla wszystkich trybów.  
Wszelkie znaki interpunkcyjne są automatycznie usuwane przez generator słów.

## Prezentacja wyników
W trybie 2 - na ekranie wyświetlany jest czas dodawania, enumeracji tablicy oraz usuwania elementów.
W trybie 3 - wyniki analizy działania są przedstawiane w formie tabeli, gdzie pokazane są wielkość problemu,
czas wykonywania algorytmu oraz wartość q oznaczającą współczynnik zgodności oceny teoretycznej z pomiarem.
Dodatkowo zebrane pomiary są ukazywane na wykresie.

## Metoda rozwiązania
Zastosowana funkcja haszująca:
Słowo wprowadzane do funkcji jest odczytywane litera po literze, a wartości unicode liter są po kolei dodawane do sumy.
Suma ta następnie jest poddawaniu dzieleniu modulo przez wielkość tablicy. Uzyskana wartość z dzielenia jest
haszem danego słowa.  
Wszystkie wymagane struktury takie jak lista jednokierunkowa oraz tablica haszująca zostały zaimplementowane od zera.

## Moduły źródłowe
Kod źródłowy został podzielony na następujace pliki:  
synthetic.py    - plik z zaimplementowanym generatorem słów na podstawie próbki tekstu polskiego.  
hash.py         - plik implementujący klasę węzła, listy jednokierunkowej oraz tablicy haszującej  
main.py         - interfejs użytkownika

## Informacje dodatkowe
Do prawidłowego działania programu wyagane jest zainstalowanie biblioteki matplotlib, która odpowiedzialna jest
za wizualizację wyników na wykresie.
