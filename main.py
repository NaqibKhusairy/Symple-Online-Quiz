import random

dash = "-" * 72

SoalanDanJawapan = [
	["Apakah Maksud Bahasa Istana 'Kaus' ?", "Berjalan", "Kasut", "Berlari", "Topi",
	 "Kasut","1"],#1
	["-3+9-x+12=10\nBerapakan Nilai x?", "-8", "18", "10", "8",
	 "8","2"],#2
	["Apakah Maksud Bahasa Istana 'Iram-Iram'?", "Sakit", "Kepala", "Hari Lahir", "Payung",
	 "Payung","3"],#3
	["(2p −3)(5p + 4) =", "4p^2-120", "10p^2-12", "10p^2-7p-12", "10p^2+7p-12",
	 "10p^2-7p-12","3"],#3
	["What The Meanig Of 'Skills in Economic Planning'", 
	"Kemahiran dalam Pemusnah Planning Ekonomi", "kemahiran dalam Kemelesetan Ekonomi",
	 "Kemahiran dalam Perancangan Ekonomi", "Kemahiran dalam Inflasi", 
	"Kemahiran dalam Perancangan Ekonomi","4"],#4
	["Apakah Fungsi Koroid", "Mengekalkan Bentuk Mata", "Menghasilkan Impuls Saraf", 
	"Mencegah Pantulan Cahaya Dalam Mata", "Melindungi Mata", 
	"Mencegah Pantulan Cahaya Dalam Mata","5"],#5
	["Negara X - kenaikan harga barang dan perkhidmatan secara berterusan\nApakah Yang Mungkin Berlaku Di Negara X ?", 
	"Deflasi", "Kemelesetan Ekonomi", "Ekonomi Negara X menigkat tinggi", "Inflasi", 
	"Inflasi","6"],#6
	["Apakah Maksud 5 bilah keris Di Logo Jata Negara Malaysia", "Mewakili Negeri-Negeri Besekutu",
	 "Mewakili Sabah,Sarawak,Pulau Pinang,Melaka dan Selangor", "Mewakili Negeri-Negeri Tidak Bersekutu",
	  "Melambangkan Keberanian 5 Orang Pendekar", 
	  "Mewakili Negeri-Negeri Tidak Bersekutu","10"],#10
]

bilangansoalan = len(SoalanDanJawapan)
total = 0
totalmarkah = 0
jumlahbetul = 0
soalan = 0

def gred(peratus):
	if peratus == 100 and peratus >= 90 :
		gredd = "A+"
		Tahap = "Cemerlang Tertinggi"
	elif peratus < 90 and peratus >= 80:
		gredd = "A"
		Tahap = "Cemerlang Tinggi"
	elif peratus < 80 and peratus >= 70:
		gredd = "A-"
		Tahap = "Cemerlang "
	elif peratus < 70 and peratus >= 65:
		gredd = "B+"
		Tahap = "Kepujuan Tertinggi"
	elif peratus < 65 and peratus >= 60:
		gredd = "B"
		Tahap = "Kepujuan Tinggi"
	elif peratus < 60 and peratus >= 55:
		gredd = "C+"
		Tahap = "Kepujuan Atas"
	elif peratus < 55 and peratus >= 54:
		gredd = "C"
		Tahap = "Kepujuan"
	elif peratus < 54 and peratus >= 45:
		gredd = "D"
		Tahap = "Lulus Atas"
	elif peratus < 45 and peratus >= 40:
		gredd = "E"
		Tahap = "Lulus"
	elif peratus < 40 and peratus >= 0:
		gredd = "G"
		Tahap = "Gagal"
	else :
		gredd = "invalid"
		Tahap = "Invalid"

	return gredd, Tahap

print(dash)
print("{:<20}{:<52}".format("", "Please answer All The Question : "))
print("{:<14}{:<58}".format("", "Kuiz Ini mempunyai : "+str(bilangansoalan)+" Yang Perlu Dijawab"))
print(dash)

while SoalanDanJawapan:
	soalan += 1
	Soalan = random.choice(SoalanDanJawapan)
	SOALAN = Soalan[0]
	PilihanJawapan = Soalan[1:5]
	JawapanYangBetul = Soalan[5]
	markah = int(Soalan[6])
	random.shuffle(PilihanJawapan)
	print(str(soalan)+" "+SOALAN)
	print("Soalan Ini Bernilai "+str(markah)+" Markah")
	totalmarkah += markah
	print()

	for pilihan, pilihanjawapan in enumerate(PilihanJawapan):
		pilihanABCD = chr(ord('A') + pilihan)
		print(f"{pilihanABCD}. {pilihanjawapan}")

		if pilihanjawapan == JawapanYangBetul :
			JawapanYangBetul = pilihanABCD
	print()

	while True :
		JawapanUser = input("Your answer (A-D): ").upper()
		if JawapanUser in ['A','B','C','D'] :
			break
		else:
			print("Your Must Only insert A, B, C, or D.")
			print("Please Reunswer the Question")
			print(dash)
			random.shuffle(PilihanJawapan)
			print(SOALAN)
			print("Soalan Ini Bernilai "+str(markah)+" Markah")

			for pilihan, pilihanjawapan in enumerate(PilihanJawapan):
				pilihanABCD = chr(ord('A') + pilihan)
				print(f"{pilihanABCD}. {pilihanjawapan}")
				
				if pilihanjawapan == JawapanYangBetul :
					JawapanYangBetul = pilihanABCD
			print()

	if JawapanUser == JawapanYangBetul:
		print("Correct Answer!\n")
		total += markah
		jumlahbetul += 1

	else:
		print("Wrong Answer!\n")

	SoalanDanJawapan.remove(Soalan)
	print(dash)

	
peratus = (total / totalmarkah) * 100

print("{:<17}{:<51}".format("\n", "Tahniah Anda Telah Menjawab "+str(bilangansoalan)+" Soalan"))
print("{:<2}{:<70}".format("", "Soalan Yang Anda Telah Jawab Dengan Tepat Adalah "+str(jumlahbetul)+" Daripada "+str(bilangansoalan)+" Soalan"))
print("\n"+dash)
print("{:<29}{:<43}".format("", "Keputusan Anda"))
print(dash)

gredd,Tahap = gred(peratus)

if gredd != "invalid" : 
	if peratus % 1 == 0 :
		persen = "Peratus Markah anda : {:.0f}%".format(peratus)
	elif peratus * 10 % 1 == 0 :
		persen = "Peratus Markah anda : {:.1f}%".format(peratus)
	else :
		persen = "Peratus Markah anda : {:.2f}%".format(peratus)
	print("Markah anda : " + str(total) + "/" + str(totalmarkah))
	print(persen)

	print("Gred Anda : "+gredd)

	if Tahap != "Gagal" : 
		print("Tahap Anda : "+Tahap)
	elif Tahap == "invalid":
		print("Your Result Is Invalid")
	else :
		print("Anda Gagal !!!")
else :
	print("Your Result Is Invalid !!!!")
print(dash)