import webbrowser
from time import gmtime, strftime

#QuantAI

AIName = "QuantAI";
AIPrefix = "[QuantAI]";
Version = "v0.0.1";
#Defined Functions

def SetMasterName(masterName):
    global MasterName;
    MasterName = masterName;

def GetMasterName():
    return MasterName;

def ClearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");

    
def CheckMasterName():
    global MasterPrefix;
    MasterName = input("\nHow can I call you? ");
    SetMasterName(MasterName);
    print("\nDid I heard that correctly - your name is " + GetMasterName() + "?");
    answer = input("Type Y(yes) or N(no) to change it: ");
    if answer == "N" or answer == "n" or answer == "no" or answer == "No" or answer == "NO":
        CheckMasterName();
    elif answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes" or answer == "YES":
        MasterPrefix = "["+GetMasterName()+"]";
        ClearScreen();
    else:
        print(MasterPrefix+"Sorry, something went wrong! Starting over...");
        CheckMasterName();

        
#Main Assistant Quests
def AssistantStart():
    MasterQuestion = input("\n"+AIPrefix+"Hello, "+GetMasterName()+"! How can I help you today? ");
    print(MasterPrefix+""+MasterQuestion+"\n");
    if MasterQuestion == "version" or MasterQuestion == "Version" or MasterQuestion == "VERSION":
        print(AIPrefix+"My current version is "+Version);
        AssistantStart();
    elif MasterQuestion == "calc" or MasterQuestion == "CALC" or MasterQuestion == "calculate" or MasterQuestion == "CALCULATE" or MasterQuestion == "calculator" or MasterQuestion == "CALCULATOR":
        equation = input(AIPrefix+"Write the equation: ");
        equationResult = eval(equation, {'__builtins__': None});
        print(AIPrefix+"Equation result: "+ str(equationResult));
        AssistantStart();
    elif MasterQuestion == "stop" or MasterQuestion == "STOP" or MasterQuestion == "exit" or MasterQuestion == "EXIT" or MasterQuestion == "quit" or MasterQuestion == "QUIT" or MasterQuestion == "bye" or MasterQuestion == "BYE":
        print(AIPrefix+"Goodbye, "+GetMasterName()+"!");
        quit();
    elif MasterQuestion == "help" or MasterQuestion == "HELP" or MasterQuestion == "h" or MasterQuestion == "H" or MasterQuestion == "?":
        print("-----------------------------------------");
        print("-            Manual For QuantAI         -");
        print("-----------------------------------------\n");

        print("Created by GGodTheDeveloper Git: https://github.com/GGodTheDeveloper\n");

        print("Here are some commands, that QuantAI has learned:\n");
        print("-----------------------------------------");
        print("help/? - Opens QuantAI Manual\n");
        print("version - Shows current QuantAI version\n");
        print("calc - Opens Equation Solver, can solve simple equations (and some difficult ones)\n");
        print("exit/quit - Quits from QuantAI\n");
        print("link/web - Opens Web Link Opener");
        print("time/date - Shows Real Date and Time");
        print("-----------------------------------------");
        print("QuantAI ©RadicalGames 2018");
        AssistantStart();
    elif MasterQuestion == "link" or MasterQuestion == "LINK" or MasterQuestion == "web" or MasterQuestion == "WEB" or MasterQuestion == "browser" or MasterQuestion == "BROWSER":
        link = input(AIPrefix+"Enter a web link to open: ");
        print(AIPrefix+"Opening "+link+"...");
        webbrowser.open(link, new=0, autoraise=True);
        AssistantStart();
    elif MasterQuestion == "time" or MasterQuestion == "TIME" or MasterQuestion == "date" or MasterQuestion == "DATE" or MasterQuestion == "datetime" or MasterQuestion == "DATETIME" or MasterQuestion == "timedate" or MasterQuestion == "TIMEDATE":
        print(AIPrefix+"Date and Time: " +strftime("%Y-%m-%d %H:%M:%S", gmtime()));
        AssistantStart();
    else:
        print(AIPrefix+"Sorry, i could\'nt understand you. I am still learning. Lets start from the start...");
        AssistantStart();
        

#StartUp

print("Welcome! My name is QuantAI - High IQ personal assistant.");
CheckMasterName();
print("Ok. Starting QuantAI "+GetMasterName()+"'s Assistant...\n");
AssistantStart();






        

