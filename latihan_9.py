list=[]
try:
	jumlah_nama = int(input("masukan jumlah nama yang akan dimasukan: "))
	for i in range(jumlah_nama):
		nama= str(input("nama ke %1: "%(i)))
		list.append(nama)
	pilihan = int(input("masukan nama dengan index ke: "))
	print("nama pada index %1 adalah %s " % (pilihan,list[pilihan]))
except ValueError:
	print("masukan nilai angka bilangan bulat,bukan string")
except Indexerror:
	print("index data tersebut tidak tersedia")
