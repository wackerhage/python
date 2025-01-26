file_names = open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r")
names = file_names.readlines()

list_of_names = []
for name in names:
    list_of_names.append(name.strip())

read_letter = open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r")
letter = read_letter.readlines()

for i in range(len(list_of_names)):
    filename = f"letter_for_{list_of_names[i]}.docx"

    # Write file:
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/{filename}", mode="w") as file:
        for x in letter:
            save = x.replace("[name]", list_of_names[i])
            file.write(save)
