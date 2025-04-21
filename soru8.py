wrd=input("kelime: ")
hrf=input("harf: ")
count=0
for harf in wrd:
    if harf == hrf:
        count+=1
print(count)