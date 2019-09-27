VOWELS = "aeiou"

class Chat:
    def __init__(self):
        self.human = None;
        self.robot = None;
        self.human_message = "";
        self.human_dialog_history = "";
        self.robot_dialog_history = "";
        self.humanrobot_dialog_history = "";
        self.robot_message = "";
    def connect_human(self, name1):
        self.human = name1
        return 0
    def connect_robot(self, name2):
        self.robot = name2
        return 0
    def show_human_dialogue(self):
        human_dialog_split = self.human.message.split("*stop*")
        robot_dialog_split = self.robot.message.split("*stop*")
        complete_dialog = ""
        for elem in range(len(human_dialog_split)):
            if len(human_dialog_split[elem]) > 0:
                complete_dialog += self.human.firstname + " said: " + human_dialog_split[elem] + "\n" + self.robot.firstname2 + " said: " + robot_dialog_split[elem] + "\n";
        return complete_dialog[:-1]
    def show_robot_dialogue(self):
        human_words = encrypt(self.human.message[:-6])
        robot_words = encrypt(self.robot.message[:-6])
        robot_dialog = self.human.firstname + " said: " + human_words + "\n" + self.robot.firstname2 + " said: " + robot_words;
        self.robot_dialog_history += robot_dialog
        return self.robot_dialog_history
    pass
    
def encrypt(message):
    human_words = ""
    for letter in message:
        if letter.lower() in VOWELS:
            human_words += '0'
        else:
            human_words += '1'
    return human_words
    
class Human:
    def __init__(self, fname):
        self.firstname = fname
        self.message = ""
    def send(self, text):
        self.message += text + "*stop*"
    pass

class Robot:
    def __init__(self, fname2):
        self.firstname2 = fname2
        self.message = ""
    def send(self, text):
        self.message += text + "*stop*"
    pass

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    '''
    chat = Chat()
    bob = Human('Bob')
    ann = Robot('Ann-1244c')
    chat.connect_human(bob)
    chat.connect_robot(ann)
    bob.send("Hi, Ann! Is your part of work done?")
    ann.send("Hi, Bob. Sorry, I need a few more hours. Could you wait, please?")
    bob.send("Ok. But hurry up, please. It's important.")
    ann.send("Sure, thanks.")
    chat.show_human_dialogue()
    chat = Chat()
    karl = Human('Karl')
    bot = Robot('R2D2')
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    print(chat.show_robot_dialogue())    
    Right result:
    "Karl said: 101111011111011\nR2D2 said: 10110111010111100111101110011101011010011011"
    '''
    '''
    chat = Chat()
    bob = Human('Bob')
    ann = Robot('Ann-1244c')
    chat.connect_human(bob)
    chat.connect_robot(ann)
    bob.send("Hi, Ann! Is your part of work done?")
    ann.send("Hi, Bob. Sorry, I need a few more hours. Could you wait, please?")
    bob.send("Ok. But hurry up, please. It's important.")
    ann.send("Sure, thanks.")
    print(chat.show_human_dialogue())
    '''
    '''
    Right result:
    "Bob said: Hi, Ann! Is your part of work done?\nAnn-1244c said: Hi, Bob. Sorry, I need a few more hours. Could you wait, please?\nBob said: Ok. But hurry up, please. It's important.\nAnn-1244c said: Sure, thanks."
    '''
    #print("Coding complete? Let's try tests!") 
