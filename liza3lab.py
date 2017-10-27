#towse 9/22/17
def main():
  import random
  Therapy()
  getNickname()
  discussWeather()
  DC()
def therapy():
    import random
    import string
    prompt  = "How do you do.  Please tell me your problem."
    userAnswer = raw_input(prompt) 
    resCom = "why do you feel that way"
    resiam = ["Do you believe it is normal to be" , "why are you"]
    #swing low sweet chariot
    checkThisOne = string.lower(userAnswer)
    if "you" in checkThisOne:
      resCom = "we were taliking about you, not me"
    if "i " in checkThisOne and "you" in checkThisOne:
      iLocation = string.find (checkThisOne, " i ")
      youLocation = string.find (checkThisOne, "you")
      randresI= random.randint(0,2)
      resIlist = ["Do you wish to", "do you", "do you feel a need"]
      resc = resIlist[randresI]
      res3 = checkThisOne[iLocation + 1:youLocation]
      resCom = resc + " " + (res3) + "me"
    if "i am" in checkThisOne:
      randres1 = random.randint(0,1)
      reschosen = res[randres1]
      iamLocation = string.find (checkThisOne, "i am")
      res2 = checkThisOne[iamLocation + 4:]
      resCom = (reschosen) + (res2) +  "?"
    print (resCom)
def comlicatedYesNO
    #establish list of positive responses
    posRes = [yes, yep, yeah, sure]
    #establish list of negative responses
    negRes = [no, nope, nay]
    #assign a default value to the bot's response
    response = "could you sat that again, i missed it, try clarifying"
    #get user input
    userResponse = string.lower(userResponse)
    #break user input up into a list of words
    listOFWords = string.spit(userResponse," ")
    for words in List of words
        if posRes
    
    
    #iterate through each word in the user word list
    #see if that word is in the positive list
    #assign bot response an appropriate value for positive user input

    #see if that word is in the negative list
    #assign bot response an appropriate value for negative user input
  
    #display the botResponse
def discussMusic():

  #establish list of musicians to discuss
  artistList = ["Demi Lovato", "Ed Sheeran", "Ariana Grande", "Kanye West", "Future" ]
  print("Let's talk about music.")

  #iterate through each band in the list 
  #this is the start of the loop 
  for artist in artistList: 
      #all of these indented steps will be done repeatedly
      #this is the body of the loop

      # use the target variable to create a question
      prompt = "Do you like " + artist + "?"
      #ask the question and store the answer
      userInput = raw_input(prompt)


      #the loop has now finished
      #make a statement after going through the list
      print("See you later.")

def getNickname():
  #ask name
  prompt = "what is your name?"
  userName = raw_input(prompt)
  #Nickname maker
  character = userName[0]
  askNickname = "is it ok if i call you " 
  print (askNickname) + (character)
def discussWeather():
  #assign a value to the prompt variable with literal text
  prompt = "What is the weather like today? "

  #assign a value to the user input variable by calling the function to ask the user a question
  userInput = raw_input(prompt)

  #assign a value to the botResponse variable with literal text
  botResponse = "Do you like that kind of weather? "
  #decision structure to respond to different possible user input 
  if "sun" in userInput:
    #assign a new value to botResponse if user said the word sun
    botResponse = "Does it make you happy to see the sun? "
  if "hot" in userInput:
    botResponse = "how hot is it out?"
  if "cold" in userInput or "overcast" in userInput:
    botResponse = "how cold is it out there"
  if "snowy" in userInput:
    botResponse = "I love it when it snows out! Are you going to make a snowman?"
  if "hail" in userInput:
    botResponse = "LOOK OUT BELOW"
  if "clouds" in userInput:
    botResponse = "Hope they clear up!"
  #call the function for displaying text in the console
  print(botResponse)
def DC():
   prompt = "what is your favruite color?"
   userInput = raw_input(prompt)
   listRed = ["Alizarin", "crimson","Amaranth","rose","red"]
   listBlue = ["sea blue", "grape"]
   listGreen = ["leafy", "Green", "vermillion"]
   listYellow = ["Yellow","gold"]
   listBrown = ["Brown","bark"]
   listBlack = ["night","black"]
   listWhite = ["white","blank","eggshell"]
   R = "really? how odd..."
   if userInput in listBlue:
     R = "Off you got!"
   if userInput in listRed:
     R = "nope!"
   if userInput in listGreen:
     R = "i envy you"
   if userInput in listYellow:
     R = "off you go"
   if userInput in listBrown:
     R = "are you an afrocenttist?"
   if userInput in listBlack:
     R = "you're a weirdo"
   if userInput in listWhite:
     R = "did you vote trump?"
   
   print R
     