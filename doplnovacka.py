'''with open('song.txt') as f:
  text = f.read()
f.closed

text = text.replace('\n','#')

seznam = []
seznam = text.split(' ')
vysledek = []

for i in range (0,len(seznam)):
  slovo = seznam[i]
  slovoUpraveno = ''
  if ((i + 1) % 5 == 0):
    for pismeno in slovo:
      slovoUpraveno += '-'
    vysledek.append(slovoUpraveno)
  else:
    vysledek.append(slovo)

s = ' '.join(vysledek)
s = s.replace('#','\n')
print(s)'''


with open('lorem.txt') as f:
  text = f.read()
f.closed

text = text.replace('\n','#')

seznam = []
seznam = text.split(' ')
vysledek = []
interpunkce  = '.,?!-;\''

for i in range (0,len(seznam)):
  slovo = seznam[i]
  slovoUpraveno = ''
  if ((i + 1) % 5 == 0):
    for pismeno in slovo:
      if pismeno not in interpunkce:
        slovoUpraveno += '*'
      else:
        slovoUpraveno += pismeno
    vysledek.append(slovoUpraveno)
  else:
    vysledek.append(slovo)

s = ' '.join(vysledek)
s = s.replace('#','\n')
print(s)   
