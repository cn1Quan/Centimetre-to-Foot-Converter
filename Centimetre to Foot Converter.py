Height = input("Height: ")
Centimetre_or_Foot = input("Height entered in (c)m/(f)t: ")
if "c" in Centimetre_or_Foot:
  Height = float(Height) / 30.48
  print(str(round(Height,2)) + "ft")
if "f" in Centimetre_or_Foot:
  Height = float(Height) * 30.48
  print(str(round(Height,0)) + "cm")
