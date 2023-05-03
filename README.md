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
  "current_player": 1,
  "game_mode": 2,
  "player_name_1": "default 1",
  "player_name_2": "default 2",
  "opponent_ships": 0,
  "player_ships": 0,
  "first_cpu_memory": [],
  "shooting_iq": 0,
  "direction": 0,
  "p_schlachtschiff_1_p": [],
  "p_schlachtschiff_1_m": [],
  "p_kreuzer_1_p": [],
  "p_kreuzer_2_p": [],
  "p_zerstoerer_1_p": [],
  "p_zerstoerer_2_p": [],
  "p_zerstoerer_3_p": [],
  "p_uboot_1_p": [],
  "pUboot2p": [],
  "p_uboot_3_p": [],
  "p_uboot_4_p": [],
  "p_kreuzer_1_m": [],
  "p_kreuzer_2_m": [],
  "p_zerstoerer_1_m": [],
  "p_zerstoerer_2_m": [],
  "p_zerstoerer_3_m": [],
  "p_uboot_1_m": [],
  "p_uboot_2_m": [],
  "p_uboot_3_m": [],
  "p_uboot_4_m": [],
  "o_schlachtschiff_1_p": [],
  "o_schlachtschiff_1_m": [],
  "o_kreuzer_1_p": [],
  "o_kreuzer_2_p": [],
  "o_zerstoerer_1_p": [],
  "o_zerstoerer_2_p": [],
  "o_zerstoerer_3_p": [],
  "o_uboot_1_p": [],
  "o_uboot_2_p": [],
  "o_uboot_3_p": [],
  "o_uboot_4_p": [],
  "o_kreuzer_1_m": [],
  "o_kreuzer_2_m": [],
  "o_zerstoerer_1_m": [],
  "o_zerstoerer_2_m": [],
  "o_zerstoerer_3_m": [],
  "o_uboot_1_m": [],
  "o_uboot_2_m": [],
  "o_uboot_3_m": [],
  "o_uboot_4_m": [],
  "leaked_board_1": [
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
  "leaked_board_2": [
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
  "hidden_board_1": [
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
  "hidden_board_2": [
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
  "reset_board": [
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