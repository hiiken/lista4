P = int(input())
TxContagio = float(input())

Cti = 0
Ctii = 0
Ct0 = 1872
Ctt = Ct0
dia = 0


while(Ctt < P*0.73):
  if(dia == 0):
    Cti = Ct0*TxContagio
    Ctii = Cti
    Ctt += Cti
    dia += 1

  else:
    Cti = Ctii*TxContagio
    Ctii = Cti
    Ctt += Cti
    dia += 1 

print("A cidade conseguiu imunidade coletiva em {} dias".format(dia))
