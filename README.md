# Python_FleetBattle
Python Programmentwurf

- Speicherung Spielstand in .json-Datei -> mehrdimensionales Array
- Schiffdarstellung als o bspw., Wasser mit anderem ASCII-Zeichen
- Wenn Spieler an der Reihe ist, wird nur angezeigt, wohin bereits geschossen wurde bzw. die Treffer 
- Schiffplatzierung: Angabe Schiffsanfang, dann in welche Richtung 
- Eck zählt als Berührpunkt mit -> nicht möglich 


-Wikipedia Schiffe versenken Anleitung:
    https://de.wikipedia.org/wiki/Schiffe_versenken


   A  B  C  D  E  F  G  H  I  J
1  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
2  ~  ~  #  -  #  ~  ~  ~  ~  ~
3  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
4  ~  #  ~  ~  ~  ~  x  ~  ~  ~
5  ~  |  ~  ~  ~  ~  ~  ~  ~  ~
6  ~  #  ~  ~  ~  ~  ~  ~  ~  ~
7  ~  ~  ~  ~  ~  X  ~  ~  ~  ~
8  ~  ~  ~  ~  ~  ~  O  ~  ~  ~
9  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
10 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~


Legende:
O = leerer Treffer
x = Treffer
X = versenkter Treffer
"#" = Postion Schiff
~ = Wasser

Zahlenzugriffe:
0 = leeres Feld ~
1 = Feld mit Schiff #
2 = Feld mit leerem Treffer O
3 = Feld mit Treffer x
4 = Feld mit versenkter Treffer X


am besten doch verschiedene ASCII Zeichen für die unterschiedlichen Schiffe verwenden (Da die übersichtlichkeit stark leidet). Das mit den Strichen umzusetzen wird sehr schwer. Wenn man die unterschiedlichen Zeichen verwendet einfach beim angeben der Position eine vorgegebene Reihenfolge machen und somit die Zeichen festlegen.

playerIndex 1 = Spieler 1
playerIndex 2 = Spieler 2
playerIndex 3 = Computer