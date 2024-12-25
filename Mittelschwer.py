
while True:
    alt = int(input("Wie alt bist du? : "))
    note = int(input("Wie lautet Ihre Abschlussnote? : "))
    if alt<20 or alt>50 or note<80:
        print("Du wurdest nicht eingestellt")
        continue
    else:
        print("Du wurdest eingestellt")
        break

