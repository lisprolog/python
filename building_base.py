class Building:    

    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.s = south;
        self.w = west;
        self.we = width_WE;
        self.ns = width_NS;
        self.h = height;

    def corners(self):
        corners = {'north-east': [self.s + self.ns, self.w + self.we], 'south-east': [self.s, self.w + self.we], 'south-west': [self.s, self.w], 'north-west': [self.s + self.ns, self.w]};
        return corners
        
    def area(self):
        return self.we * self.ns

    def volume(self):
        return self.we * self.ns * self.h

    def __repr__(self):
        return 'Building'+ '(' + str(self.s)+ ', ' + str(self.w) + ', ' + str(self.we) + ', ' + str(self.ns) + ', ' + str(self.h)+ ')' 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"

