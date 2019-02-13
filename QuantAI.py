import webbrowser
from time import gmtime, strftime
import socket

#QuantAI
global AIName;
AIName = "QuantAI";
global AIPrefix;
AIPrefix = "QuantAI";
Version = "v0.0.2";
#Defined Functions
def SetAIPrefix(prefix):
    global AIPrefix
    AIPrefix = "["+prefix+"]";

SetAIPrefix(AIPrefix);

def GetAIPrefix():
    return AIPrefix;

def SetMasterName(masterName):
    global MasterName;
    MasterName = masterName;

def GetMasterName():
    return MasterName;

def ClearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");

def DebugMode():
    DevInput = input("\n[~]Input: ").lower();
    if DevInput == "assistant mode" or DevInput == "end" or DevInput == "exit":
        print("[~]Saving files...");
        print("[~]Closing files...");
        print("[~]Starting QuantAI Assistant...");
        AssistantStart();

    elif DevInput == "change prefix ai":
        newAIPrefix = input("[~]Input the new QuantAI prefix: ");
        print("[~]Change AI prefix...");
        SetAIPrefix(newAIPrefix);
        print("[~]Changed AI prefix to "+newAIPrefix);
        DebugMode();

    elif DevInput == "test":
        print("[~]THIS IS AUTO GENERATED MESSAGE TO TEST INPUT/OUTPUT FUNCTION[~]");
        print("[~]IF YOU SEE THE FOLLOWING MESSAGE AS 'TRUE' EVERYTHING IS WORKING[~]");
        print("TRUE");
        DebugMode();
    else:
        print("[~]Unknown command!");
        DebugMode();
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
    MasterQuestion = input("\n"+GetAIPrefix()+"Hello, "+GetMasterName()+"! How can I help you today? ").lower();
    print(MasterPrefix+""+MasterQuestion+"\n");
    if MasterQuestion == "version":
        print(GetAIPrefix()+"My current version is "+Version);
        AssistantStart();
    elif MasterQuestion == "calc" or MasterQuestion == "calculate" or MasterQuestion == "calculator":
        equation = input(GetAIPrefix()+"Write the equation: ");
        equationResult = eval(equation, {'__builtins__': None});
        print(GetAIPrefix()+"Equation result: "+ str(equationResult));
        AssistantStart();
    elif MasterQuestion == "stop" or MasterQuestion == "exit" or MasterQuestion == "quit" or MasterQuestion == "bye":
        print(GetAIPrefix()+"Goodbye, "+GetMasterName()+"!");
        quit();
    elif MasterQuestion == "help" or MasterQuestion == "h" or MasterQuestion == "?":
        print("-----------------------------------------");
        print("-            Manual For QuantAI         -");
        print("-----------------------------------------\n");

        print("Created by GGodTheDeveloper Git: https://github.com/GGodTheDeveloper\n");

        print("Here are some commands, that QuantAI has learned:\n");
        print("-----------------------------------------\n");
        print("help/? - Opens QuantAI Manual\n");
        print("version - Shows current QuantAI version\n");
        print("calc - Opens Equation Solver, can solve simple equations (and some difficult ones)\n");
        print("exit/quit - Quits from QuantAI\n");
        print("link/web - Opens Web Link Opener\n");
        print("time/date - Shows Real Date and Time\n");
        print("email/mail - Opens E-mail sender\n");
        print("-----------------------------------------");
        print("QuantAI ©RadicalGames 2019");
        AssistantStart();
    elif MasterQuestion == "link" or MasterQuestion == "web" or MasterQuestion == "browser":
        link = input(GetAIPrefix()+"Enter a web link to open: ");
        print(GetAIPrefix()+"Opening "+link+"...");
        webbrowser.open(link, new=0, autoraise=True);
        AssistantStart();
    elif MasterQuestion == "time" or MasterQuestion == "date" or MasterQuestion == "datetime" or MasterQuestion == "timedate":
        print(GetAIPrefix()+"Date and Time: " +strftime("%Y-%m-%d %H:%M:%S", gmtime()));
        AssistantStart();
    elif MasterQuestion == "ip" or MasterQuestion == "ipconfig" or MasterQuestion == "ifconfig":
        print(GetAIPrefix()+"Here is your network info:");
        print("-----------------------------------------");
        print("PC Name: "+socket.getfqdn());
        print("IPv4: "+socket.gethostbyname(socket.gethostname()));
        AssistantStart();
    elif MasterQuestion == "email" or MasterQuestion == "mail":
         email = input(AIPrefix+"Write the 'TO' email address: ");
         print(GetAIPrefix()+"Opening your email sender...");
         webbrowser.open("mailto:"+email, new=0, autoraise=True);
         AssistantStart();
    elif MasterQuestion == "debug mode":
         print("\n\n\n");
         print(GetAIPrefix()+"Starting Debug Mode...");
         print("==Debug Mode Enabled==\n");
         print("WARNING! This is QuantAI Developement Panel! If you dont know, what you are doing, plese write 'assistant mode' !\n");
         DebugMode();
    else:
        print(GetAIPrefix()+"Sorry, i could\'nt understand you. I am still learning. Lets start from the start...");
        AssistantStart();
        

#StartUp

print("Welcome! My name is QuantAI - High IQ personal assistant.");
CheckMasterName();
print("Ok. Starting QuantAI "+GetMasterName()+"'s Assistant...\n");
AssistantStart();






        

