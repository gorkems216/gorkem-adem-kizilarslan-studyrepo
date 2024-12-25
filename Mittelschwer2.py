note = int(input("Deine Abschlussnote: "))
programmiererfahrung = int(input("Deine programmiererfahrung (zwischen 1 für 'keine',5 für 'hohe'):"))
if note >= 90 or (note>69 and programmiererfahrung ==5):
    print("Du bist eingestellt")
elif note>70 or programmiererfahrung==4:
    print("Sie sind eingeladen, zu sprechen")
else:
    print("Du wurdest nicht eingestellt")