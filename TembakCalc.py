"""
Yeah yeah, Python is cringe. Shut up.

Vincentius Daniel Budidharma 12A6/33
Program ini adalah kalkulator peluang yang terspesialisasi untuk peluang nilai ulangan
Input: ada berapa soal di ulangan, ada berapa soal yang lu tembak
Output: list peluang setiap nilai yang possible, peluang lu dapet di atas 75, nilai minimal kalo semua soal yang ditembak salah

Note: yang lu gak tembak diasumsi bener. Jenis soal adalah PG dengan 5 pilihan. Sama kayak PTS :)
"""

#User Input through console
TotalSoal = int(input("Total soal:"))
TotalTembak = int(input("Lu tembak berapa soal:"))

#put it in yourself if you want
"""
TotalSoal = 10
TotalTembak = 5
"""

#nilai minimal kalo semua tembak salah
def NilaiMinimal():
    Points = TotalSoal - TotalTembak
    NilaiMin = (Points/TotalSoal)*100
    return NilaiMin

#irrelevant
"""
#odds of getting 100
BerkatTuhan = (0.2)**TotalTembak
print("Peluang lu dapet 100:",BerkatTuhan)
"""

#List of possible nilai di atas nilai minimal
ListNilai=[]
for TotalBener in range(TotalSoal+1):
    if (TotalBener * 100 / TotalSoal) >= NilaiMinimal():
        ListNilai.append(int(TotalBener * 100 / TotalSoal))

#Python doesn't have any built in factorials so I had to learn how to do it from this guy: https://www.javatpoint.com/pyhton-factorial-number
def Factorial(TheNumber):
    FactorialOutput = 1
    for i in range(1,TheNumber + 1):
        FactorialOutput = FactorialOutput*i
    return FactorialOutput

#Rindu and Ito my beloved
def Peluang(TembakBener):
    Chance = (Factorial(TotalTembak)/(Factorial(TembakBener)*Factorial(TotalTembak-TembakBener)))*(0.2**TembakBener)*(0.8**(TotalTembak-TembakBener))
    return round(Chance*100,5)

#Felina. Print output
ListKKM=[]
TembakBener=0
print("--------------------------------------------------------------------------------------")
print("List nilai dan peluangnya:")
for x in ListNilai:
    print(x, Peluang(TembakBener), "%")
    if NilaiMinimal()+(100*TembakBener/TotalSoal) >= 75: #Peluang di atas 75
        ListKKM.append(Peluang(TembakBener))
    TembakBener+=1
    if TembakBener > TotalTembak:
        break

print("-------------------------------------------------------------------------------------")
print("Nilai minimal:" + str(NilaiMinimal()))
print("Peluang di atas 75:", round(sum(ListKKM),2), "%")
