student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    pass
    #Access key and value
    # print(key)
    # print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass
    #Access index and row
    #Access row.student or row.score
    # print(index)
    # print(row)
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
todo1 = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(todo1)
todo1_dict = {row.letter: row.code for (index, row) in todo1.iterrows()}
print(todo1_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

word_list = [todo1_dict[item] for item in word]
print(word_list)
