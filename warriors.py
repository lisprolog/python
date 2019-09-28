

class Warrior:

    def __init__(self):

        self.health = 50;

        self.attack = 5;

        self.is_alive = True;

    pass


class Knight(Warrior):

    def __init__(self):

        self.health = 50;

        self.attack = 7;

        self.is_alive = True;

    pass


def fight(unit_1, unit_2):

    fight_ongoing = True;

    while(fight_ongoing):

        unit_2.health = unit_2.health - unit_1.attack;

        if checkHealth(unit_2):

            unit_1.health = unit_1.health - unit_2.attack;

            if checkHealth(unit_1) == False:

                result = False;         #Fighter 1 dies, return False;

                fight_ongoing = False

        else:                           #Fighter 2 dies, return True

            result = True   

            fight_ongoing = False

    return result

            

            

    result = True;

    return result

    

def checkHealth(fighter):

    if fighter.health > 0:

        return True;

    else:

        fighter.is_alive = False;

        return False;


if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing


    chuck = Warrior()

    bruce = Warrior()

    carl = Knight()

    dave = Warrior()

    mark = Warrior()


    assert fight(chuck, bruce) == True

    assert fight(dave, carl) == False

    assert chuck.is_alive == True

    assert bruce.is_alive == False

    assert carl.is_alive == True

    assert dave.is_alive == False

    assert fight(carl, mark) == False

    assert carl.is_alive == False


    print("Coding complete? Let's try tests!")

