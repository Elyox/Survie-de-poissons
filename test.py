# -*- coding: utf-8 -*-

ESCAPE = "\x1b"
BLACK = "[30m"
BLUE = "[34m"
RED = "[31m"
for i in (RED, BLUE, BLACK):
    print(ESCAPE + i + "Texte en couleur")
