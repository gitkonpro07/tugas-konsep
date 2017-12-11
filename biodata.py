file = open("biodata.txt","a+")
nama = str(input("masukan nama: "))
result = file.write("nama saya adalah %s\n"%(nama))
print(result)
print("--------------------\"n")

file = open("biodata.txt","a+")
asal = str(input("masukan asal: "))
result = file.write("saya berasal dari %s\n"%(asal))
print(result)
print("--------------------\"n")

file = open("biodata.txt","a+")
tanggal = str(input("masukan tanggal lahir: "))
result = file.write("saya lahir pada %s\n"%(tanggal))
print(result)
print("--------------------\"n")
"# tugas-sangar" 
