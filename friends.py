class Friends:
    def __init__(self, connections):
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
                t = list(self.connections)
                t.remove(elem)
                self.connections = t
                deleted = True;
        return deleted

    def names(self):
        result = []
        for elem in self.connections:
            for x in elem:
                result.append(x)
        result = set(result);
        return result

    def connected(self, name):
        new_list2 = [];
        check = False;
        for elem in self.connections:
            elem2 = list(elem);
            if elem2[0] == name:
                new_list2.append(elem2[1]);
            if elem2[1] == name:
                new_list2.append(elem2[0]);
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
