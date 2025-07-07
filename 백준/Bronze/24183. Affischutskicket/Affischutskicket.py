en, po, in_=map(int, input().split())

en_m2=0.229*0.324*en * 2
po_m2=0.297*0.420*po * 2
in_m2=0.210*0.297*in_
print(en_m2+po_m2+in_m2)