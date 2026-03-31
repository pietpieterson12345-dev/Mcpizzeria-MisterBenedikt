# Vul hier de naam van je programma in:
#Mcpizzeria-Mr.benedikt
#
# Vul hier jullie namen in:
#Benedikt Stoelinga
#
#


### --------- Bibliotheken en globale variabelen -----------------

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen


### ---------  Functie definities  -----------------


### --------- Hoofdprogramma  ---------------

