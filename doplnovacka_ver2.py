def doplnovacka(text,CisloSlova): 

  text = text.replace('\n','#')
  
  seznam = []
  seznam = text.split(' ')
  interpunkce  = '.,?!-;\''

  slovo = seznam[CisloSlova-1]
  slovoUpraveno = ''
  for pismeno in slovo:
    if pismeno not in interpunkce:
      slovoUpraveno += '*'
    else:
      slovoUpraveno += pismeno
  
  seznam[CisloSlova-1] = slovoUpraveno

  s = ' '.join(seznam)
  s = s.replace('#','\n')
  return(s)

VstupniText = input('Vlož text: ')
VstupniCislo = int(input('Vlož číselné pořadí odpovídající slovu, které se má změnit: '))

Veta = []
Veta = VstupniText.split(' ')

while VstupniCislo <=0 or VstupniCislo > len(Veta):
  print('Zadal jsi chybné číslo.')
  VstupniCislo = int(input('Vlož číselné pořadí odpovídající slovu, které se má změnit: '))

vyslednyText = doplnovacka(VstupniText, VstupniCislo)
print(vyslednyText)