from random import randint

print("Welcome to the MadLabs Game")

playing = input("lets's play... Shall we\n")

if playing.lower() == 'no':
    quit()

print("ok let's play the game\n")

noun1=input("Enter your name ")
noun2=input("Enter your friend's name ")
noun3=input("Enter another friend's name ")
noun4=input("Enter your place name ")
adjective1=input("Enter an adjective ")
adjective2=input("Enter an adjective ")
adjective3=input("Enter an adjective ")
adverb1=input("Enter an adverb ")
adverb2=input("Enter an adverb ")
exclamation = input("Enter an Emoji ")
print("one day\t"+noun1+" went to "+noun4+"."+ "He felt very lonely, even though the view was "+ adjective1 +
      " . he decided to call his two friends "+noun2+" and "+ noun3+ "."+" when they came, they told "+noun1+" something "
      +adjective2+ " had happened ."+ noun1 +" went there very "+adverb1+" "+" when he came he found out that his other friend "+
      "was falling off a cliff "+noun1+" said " + exclamation+" indeed he was feeling "+adjective3+" . "+noun1+" managed to save him after that they had a "
       +adverb2+" celebration" )