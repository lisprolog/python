class Friends:
    def __init__(self, connections):
        print(connections);
        self.connections = connections;


    def add(self, connection):
        if connection in self.connections:
            return False
        else:
            self.connections = list(self.connections);
            self.connections.append(connection);
            return True

    def remove(self, connection):
        deleted = False;
        for elem in self.connections:
            if str(elem) == str(connection):
                print(type(self.connections));
                print("test1:");
                print(self.connections);
                self.connections.remove(elem);
                print("test2:");
                print(self.connections);
                deleted = True;
        return deleted

    def names(self):
        result = []
        for elem in self.connections:
            for x in elem:
                result.append(x)
        result = set(result);
        print("result:");
        print(result);
        return result

    def connected(self, name):
        new_list = [];
        new_list2 = [];
        print("name: " + name);
        check = False;
        for elem in self.connections:
            for item in elem:
                item_buffer = item;
                print("item: " + item);
                if check == True:
                    new_list2.append(item);
                    check = False;
                #item_buffer.append(item);
                if item == name:
                    print("same!");
                    #new_list2.append(item_buffer);
                    check = True;
                new_list.append(item);
            item_buffer = ();
        print("new_list:");
        print(new_list);
        print("new_list2:");
        print(new_list2);
        print(set(new_list2));
        return set(new_list2);

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
