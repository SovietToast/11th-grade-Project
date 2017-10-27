#towse 9/22/17
def main():
  import random
  import time
  import string
  listAbort = ["exit", "stop", "abort","quit", "goodbye"]
  #initialize the Boolean to show that the chat is now on
  userWantsToChat = true
  #your code comment to describe the purpose of the while loop
  while userWantsToChat == true:
        #start therapy session
        prompt  = "How do you do.  Please tell me your problem."
        userAnswer = raw_input(prompt) 
        userAnswer = string.lower(userAnswer)
        userWordList = string.split(userAnswer)
        for userWord in userWordList:
          if userWord in listAbort:
            #exit
            userWantsToChat = false
            break
        if userWantsToChat == false:
          break
        #code to repeat will go in here; it's not ready yet
        therapy(userAnswer)
        discussWeather()
  
def therapy(userAnswer):
    import random
    import time
    import string
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
      reschosen = resiam[randres1]
      iamLocation = string.find (checkThisOne, "i am")
      res2 = checkThisOne[iamLocation + 4:]
      resCom = (reschosen) + (res2) +  "?"
    print (resCom)
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
     