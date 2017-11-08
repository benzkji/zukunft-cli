
zahlen = range(1, 11)
# zahlen = range(1, 10000000)

resultat = 0
for zahl in zahlen:
    # print zahl
    if zahl % 2 == 0:
        resultat = resultat + zahl

print resultat

# Aufgabe: Zzwischen jede Zahl ein ":" einsetzen?
# Aufgabe: Warum dauert es so lange? Wie kann man das Programm beschleunigen?
