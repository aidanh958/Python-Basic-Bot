import json #json is required
x =  '{ "name":"TestBot1", "age":"1", "city":"Springdale AR", "version":"1.0.0"}' #states the state of objects

# parse x:
y = json.loads(x)

def centers(): #function that gives list of centers
    print("question center  -  question()")
    print("command center  -  Run()")

def question(): #function that answer some of your questions
    a = input("what is your queston: ") #opening statment showing that they are in the question center
    if a == "how old are you" : 
        print(y["age"]) #prints age that was stated in the JSON
        anyquestion() #runs function that ask if they have anymore questions
    elif a == "where are you" :
        print(y["city"]) #prints city that was stated in the JSON
        anyquestion() #runs function that ask if they have anymore questions
    elif a == "NVM" :
        print("okay") #just closes the question center
    elif a == "what is your name" :
        print(y["name"]) #prints name that was stated in the JSON
        anyquestion() #runs function that ask if they have anymore questions
    elif a == "what version are you" :
        print(y["version"])
        anyquestion() #runs function that ask if they have anymore questions
    elif a == "what are you" :
        print("I am a python program created by Aidan Hook") #prints the text stating who made this 
        anyquestion() #runs function that ask if they have anymore questions
    else:
        print("question unknow") #states that there is no know answer
        anyquestion() #runs function that ask if they have anymore questions
def anyquestion():
    A = input("anything else [Y/N]") #asks if the questions should continue
    if A == "N" : #if they say No then it stops
        print("okay")
    elif A == "Y" : #if they say Yes then it activates the question function
        question()
    else :
        print("please answer with Y or N") ##states that it is a Y or N question
        anyquestion()
        
def Run():
    R = input("command: ") #opening statment stating that this is the command center
    if R == "login": #basic login command
        input("username: ") #ask what you want your username to be
        input("password: ") #ask what you want your passsword to be
        ElseRun()
    elif R == "close" :
        print("closing command center") #says that it is closing command center
    elif R == "server view" :
        while R == "server view" :
            print("error server refused to connect") #repeat "error server refused to connect" annoyinglly
    elif R == "open question center" :
        question() #activate question function
    else: print("command unknow")

def ElseRun(): #asks if there is anything else
    r = input("anything else [Y/N]")
    if r == "Y" :
        Run() #keeps command center open
    elif r == "N" :
        print("okay") #closes command center
    else :
        print("please use Y or N") #states that you need to say Yes or No
        ElseRun()
