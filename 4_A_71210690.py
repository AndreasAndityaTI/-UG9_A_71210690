print("====MASUKKAN JUMLAH MAKANAN YANG DIPESAN====")
#menu1=Ikan bakar, menu2=Es doger, menu3=Rujak cingur
menu1=int(input("IKAN BAKAR		Rp 25.000,00	: "))
menu2=int(input("ES DOGER		Rp 6.000,00	: "))
menu3=int(input("RUJAK CINGUR		Rp 8.000,00	: "))
print("=====TOTAL=====")
totalmenu1=menu1*25000
totakmenu2=menu2*6000
totalmenu3=menu3*8000
print("TOTAL IKAN BAKAR		: Rp",totalmenu1)
print("TOTAL ES DOGER			: Rp",totalmenu2)
print("TOTAL RUJAK CINGUR		: RP",totalmenu3)
print("Jumlah total biaya yang harus dibayar adalah Rp",totalmenu1+totalmenu2+totalmenu3)
