
import random
import os

scoreabang = 0
scoreadik = 0

def main():
  global scoreabang, scoreadik
  os.system("clear")
  print("=====")
  print("Score Abang : " + str(scoreabang))
  print("Score Adik : " + str(scoreadik))
  print("=====")
  abang = random.randint(1,10)
  adik = random.randint(1,10)
  if (abang > adik): 
    print("abang menang!")
    scoreabang += 1
  else:
    print("adik menang!")
    scoreadik += 1
  print("")
  dummy = raw_input("tekan tombol enter untuk mencoba lagi")
  main()

main()