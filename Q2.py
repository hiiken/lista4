zero = 0
positivo = 0
negativo = 0

for c in range(0, 10):
  n = int(input())
  if(n == 0):
    zero += 1
  elif(n > 0):
    positivo += 1
  elif(n < 0):
    negativo += 1
    
print("{}\n{}\n{}".format(positivo, negativo, zero))
