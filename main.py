import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
letters = data["letter"].to_list()
codes = data["code"].to_list()

df = pandas.DataFrame(data)

dict = {row["letter"]: row["code"] for (row, row) in df.iterrows()}
print(dict)

game_is_on = True
while game_is_on :
    name = input("Please, enter your name: ").upper()
    print(f"The phonetic code for this name is: ")
    for letter in name:
        list = [dict[letter] for letter in name]
    print(list)