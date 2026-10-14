# import pandas to read the csv file

import pandas
data=pandas.read_csv("health_data.csv")

# print(data)

# first message user sees in chatbot
print("Healthbot: Hi, I'm a simple bot ask me about a symtop or say 'quit' ")

# while loop-->we do not know the number of times a chatbot will loop
while True:
    # geting e user input
    user_text=input("\n You: ").lower()

    # check if the user wants to quit

    if user_text == "quit":
        print("Healthbot: Goodbye! Stay Healthy")

    # stop the loop
        break

    # loop to check for answer that matches the input
    found_answer=False

    for index, row in data.iterrows():
        # cleanup the key word from the csv
        # print (row)

        keyword_list = str(row["Keywords"]).split(",")
        # print(keyword_list)

        # check every key word in that row
        for word in keyword_list:
            # check if the keyword are in the user input

            clean_word =word.strip().lower()
            if clean_word in user_text:
                print("Healthbot:" ,row["Response"])
                found_answer=True

                # stop looking for key words in the user input
                break

        # stop looking at the other rows 
        if found_answer:
            break
    # if keyword do not match(responce)
    if not found_answer:
        print("Healthbot: I dont Know that one, try asking about 'fever' or 'diet' ")




