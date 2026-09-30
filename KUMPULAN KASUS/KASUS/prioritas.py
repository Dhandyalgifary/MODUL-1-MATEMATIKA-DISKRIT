kondisi_prioritas = True
status_vip = False

hasil = kondisi_prioritas ^ status_vip

if hasil:
    print("MENDAPAT PRIORITAS")
else:
    print("TIDAK MENDAPAT PRIORITAS")
