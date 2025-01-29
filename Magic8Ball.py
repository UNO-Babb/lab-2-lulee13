#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answer = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", 
            "Don’t count on it.", "Doubt it.", "It is certain.", "Absolutely not.", "It is decidedly so.", "Most likely.", "Eh.", 
            "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Hell if I know.", "Reply hazy, try again.", 
            "You tell me.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it."]
  #Prompt the user for their question.

  #Answer question randomly with one of the options from your earlier list.
  num = random.random()
  num = int(num * 1000)
  num = num % 25
  
  question = input("Ask me a yes or no question: ")
  print(answer[num])


if __name__ == '__main__':
  main()
