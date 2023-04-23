"""
This is a probability calculator for multiple choice test scores
Input: total number of questions, number of questions you guessed
Output: list of probabilities for all possible scores, probability to get above 75%, lowest score if all your guessed are incorrect
Note: Numbers you don't guess are considered correct. The calculator assumes there are only 5 choices per number.
"""

#User Input through console
TotalSoal = int(input("Total number of questions:"))
TotalTembak = int(input("Number of questions you guessed:"))

#put it in yourself if you want
"""
TotalSoal = 10
TotalTembak = 5
"""

#lowest score if you guessed everything wrong
def NilaiMinimal():
    Points = TotalSoal - TotalTembak
    NilaiMin = (Points/TotalSoal)*100
    return NilaiMin

#List of possible scores above the lowest score
ListNilai=[]
for TotalBener in range(TotalSoal+1):
    if (TotalBener * 100 / TotalSoal) >= NilaiMinimal():
        ListNilai.append(int(TotalBener * 100 / TotalSoal))

def Factorial(TheNumber):
    FactorialOutput = 1
    for i in range(1,TheNumber + 1):
        FactorialOutput = FactorialOutput*i
    return FactorialOutput

#12th grade binomial distribution math
def Peluang(TembakBener):
    Chance = (Factorial(TotalTembak)/(Factorial(TembakBener)*Factorial(TotalTembak-TembakBener)))*(0.2**TembakBener)*(0.8**(TotalTembak-TembakBener))
    return round(Chance*100,5)

#Prints output
ListKKM=[]
TembakBener=0
print("--------------------------------------------------------------------------------------")
print("List of scores and probabilities:")
for x in ListNilai:
    print(x, Peluang(TembakBener), "%")
    if NilaiMinimal()+(100*TembakBener/TotalSoal) >= 75: #Peluang di atas 75
        ListKKM.append(Peluang(TembakBener))
    TembakBener+=1
    if TembakBener > TotalTembak:
        break

print("-------------------------------------------------------------------------------------")
print("Lowest prbably score:" + str(NilaiMinimal()))
print("Probability your score is above 75%:", round(sum(ListKKM),2), "%")
