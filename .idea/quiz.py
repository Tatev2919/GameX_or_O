import random
import sys

file = open("test.txt", "w+")
file.write("What is the longest river in Russia and Europe ? \n")
file.write("Volga \n")
file.write("Amazon \n")
file.write("Araks \n")
file.write("Kur \n")
file.write("What is the capital city of Armenia ? \n")
file.write("Yerevan \n")
file.write("Paris \n")
file.write("Moskva \n")
file.write("Kahire \n")
file.write("5+5 ? \n")
file.write("10 \n")
file.write("20 \n")
file.write("30 \n")
file.write("40 \n")
file.write("15*2= ?\n")
file.write("30 \n")
file.write("40 \n")
file.write("50 \n")
file.write("60 \n")
file.write("15+11 * 2 = ? \n")
file.write("27 \n")
file.write("40 \n")
file.write("30 \n")
file.write("67 \n")
questionsL = []
ans = []
answers = []
randNums = random.sample(range(5), 2);
print(randNums)

file.close()
count = 0
question = ""
f = open("test.txt", "r")
f1 = f.readlines()

for m in randNums:
    ans = []
    question = f1[(5 * (m - 1))].strip();
    print(question)
    questionsL.append(question)
    for i in range(1, 5):
        ans.append(f1[(5 * (m - 1) + i)][:f1[(5 * (m - 1) + i)].index(" \n")])
    answers.append(ans)

print(questionsL)
print(answers)
dictionary = dict(zip(questionsL,answers))
for keys in dictionary.keys():
    print(keys, " ", dictionary[keys])

str = ""

# while str != answers[0][0]:
#     var = input("enter answer")
#     if(len(var) > 1):
#         var = input("Reenter answer")
#     for j in range(len(answer)):
#         if (var == answers[]):
#             str = str +
#     print(str)
# print("Congrats!")
file.close()

