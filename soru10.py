wrd=input("kelime: ")
sh="AEIİOÖUÜaeıioöuü"
count=0
for krktr in wrd:
    for sli in sh:
        if sli == krktr:
            count+=1
print(count)
