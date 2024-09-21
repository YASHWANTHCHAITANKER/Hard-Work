import csv

# Sample dataset
dataset = [
    ['sunny', 'warm', 'normal', 'strong', 'warm', 'yes'],
    ['sunny', 'warm', 'high', 'strong', 'warm', 'no'],
    ['rainy', 'cold', 'high', 'strong', 'warm', 'yes'],
    ['sunny', 'warm', 'high', 'strong', 'cool', 'yes'],
]

hypo = ['%', '%', '%', '%', '%', '%']
data = []
print("\nThe given training examples are:")
for row in dataset:
    print(row)
    if row[-1].upper() == "YES":
        data.append(row)
#print(data)

print("\nThe positive examples are:")
for x in data:
    print(x)
print("\n")

TotalExamples = len(data)

if TotalExamples == 0:
    print("No positive examples found. Exiting...")
else:
    j = 0
    k = 0
    print("The steps of the Find-s algorithm are :\n", hypo)
    p = 0
    #p=1
    d = len(data[p]) - 1
    # d = len(data[p])

    for row in data:
        if len(row) != d + 1:
        # if 
        # len(row) != d:
            print("Error: Rows in the dataset have different lengths.")
            exit()

    for j in range(d):
        hypo[j] = data[0][j]

    for i in range(TotalExamples):
        for k in range(d):
            if hypo[k] != data[i][k]:
                hypo[k] = '?'
        print(hypo)

    print("\nThe maximally specific Find-s hypothesis for the given training examples is:")
    print(hypo)