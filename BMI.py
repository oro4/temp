tall = float(input("�g������͂��Ă��������icm�j�F\n"))
wait = float(input("�̏d����͂��Ă��������ikg�j�F\n"))

bmi = wait/((tall/100)**2)
best = ((tall/100)**2)*22

if bmi < 18.5:
    hantei = "�₹�^"
elif bmi < 25:
    hantei = "���ʑ̏d"
elif bmi < 30:
    hantei = "�얞�i1�x�j"
elif bmi < 35:
    hantei = "�얞�i2�x�j"
elif bmi < 40:
    hantei = "�얞�i3�x�j"
else:
    hantei = "�얞�i4�x�j"

print("\nBMI�l�� {0:.1f} ".format(bmi) + "�y" + hantei + "�z"  + "�ł�")
print("�x�X�g�̏d�� {0:.1f} kg�ł�".format(best))