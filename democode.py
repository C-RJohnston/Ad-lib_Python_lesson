

def story():
    gender = str(input("What's your gender? \n")).lower() #each input is wrapped in a string function to force the type to a string and then the .lower() function is called to make the entire string lower case. \n creates a new line
    pronoun = "he" if gender == "boy" else "she" if gender == "girl" else "they" #inline conditional statements are formatted like this
    #this is equivalent to
    # if(gender == "boy"):
    # pronoun = "he"
    # elif(gender == "girl"):
    # pronoun = "she"
    # else:
    # pronoun = "they"
    name = str(input("your name?\n")).lower().capitalize() #here we have used .capitalize() as the name is a proper noun. We will do the same later to start sentences.
    item1 = str(input("robes or spell book \n")).lower()
    item2 = str(input("cauldron or wand? \n")).lower()
    colour = str(input("pick a colour\n")).lower()
    animal = str(input("pick an animal\n")).lower()
    animal_name = str(input("name your animal\n")).lower().capitalize()
    flavour = str(input("pick a flavour\n")).lower()
    house = str(input("Are you a Gryffindor, a Ravenclaw, a Hufflepuff, or a Slytherin?\n")).lower().capitalize()

    #here we are using an f string. This is a special type of string that allows us to very easily put variables into the string. You tell Python that you want it to use a variable by wrapping the name of the variable in {}
    story = f'''Once there was a young {gender} named {name}. {pronoun.capitalize()} was a wizard!
One day, an owl came with a letter for {name}. It said, “Please come to Hogwarts and learn magic.
You will need {item1} and a {item2}, and you may bring one pet. Your ticket for the Hogwarts Express is enclosed.” {name} went to Diagon Alley and bought a {colour} {animal}. {pronoun.capitalize()} named it {animal_name}.
Then it was time to go to Hogwarts. On the Hogwarts Express, {name} got some wizard candy. There were chocolate frogs and pumpkin
pasties, and even Bertie Bott's every flavor beans. The best flavor was {flavour}. Yum!
At Hogwarts the Sorting Hat put {name} in {house}. Then it was time to learn some magic! The teachers taught everyone how to
turn rats into teacups, make things float in the air, and take care of magical animals.\n'''
    print('\n') #putting space between the inputs and the story
    print(story)
    file = open("Stories.txt","a") #this opens the stories text file in writing mode so we can save the stories
    file.write(f"{name}'s story:\n"+story)
    file.close()

def main():
    playing = True
    while playing:
        story()
        playing = (str(input("Play again? y/n\n")).lower() == "y") #this line of code is asking the player if they want to play again. if they say y (for yes) then playing is set to true and the code loops. If they say no then playing is set to false and the game ends


main()
