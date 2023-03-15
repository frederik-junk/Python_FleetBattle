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
- | = Verbidungsglieder
~ = Wasser