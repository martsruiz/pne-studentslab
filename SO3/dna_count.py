
user_sequence = input("Please enter a DNA sequence: ").upper()

dic = {"A": 0,
       "C": 0,
       "T": 0,
       "G": 0}

for i in user_sequence:
    if i in dic:
        dic[i] += 1

length_sequence = len(user_sequence)

print("The length of the sequence is:", length_sequence)
print(dic)
