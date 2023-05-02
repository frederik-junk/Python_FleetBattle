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

1 = alles mit Computer oder Spieler 2
2 = Spieler

{
  "storage_available": 0,
  "currentPlayer": 1,
  "gameMode": 2,
  "playerName1": "default1",
  "playerName2": "default2",
  "opponentShips": 1,
  "playerShips": 1,
  "firstCpuMemory": [],
  "shootingIq": 0,
  "direction": 0,
  "pSchlachtschiff1p": [],
  "pSchlachtschiff1m": [],
  "pKreuzer1p": [],
  "pKreuzer2p": [],
  "pZerstoerer1p": [],
  "pZerstoerer2p": [],
  "pZerstoerer3p": [],
  "pUboot1p": [],
  "pUboot2p": [],
  "pUboot3p": [],
  "pUboot4p": [],
  "pKreuzer1m": [],
  "pKreuzer2m": [],
  "pZerstoerer1m": [],
  "pZerstoerer2m": [],
  "pZerstoerer3m": [],
  "pUboot1m": [],
  "pUboot2m": [],
  "pUboot3m": [],
  "pUboot4m": [],
  "oSchlachtschiff1p": [],
  "oSchlachtschiff1m": [],
  "oKreuzer1p": [],
  "oKreuzer2p": [],
  "oZerstoerer1p": [],
  "oZerstoerer2p": [],
  "oZerstoerer3p": [],
  "oUboot1p": [],
  "oUboot2p": [],
  "oUboot3p": [],
  "oUboot4p": [],
  "oKreuzer1m": [],
  "oKreuzer2m": [],
  "oZerstoerer1m": [],
  "oZerstoerer2m": [],
  "oZerstoerer3m": [],
  "oUboot1m": [],
  "oUboot2m": [],
  "oUboot3m": [],
  "oUboot4m": [],
  "leakedBoard1": [
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  ],
  "leakedBoard2": [
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  ],
  "hiddenBoard1": [
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  ],
  "hiddenBoard2": [
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  ],
  "resetBoard": [
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ],
    [
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0,
      0
    ]
  ]
}