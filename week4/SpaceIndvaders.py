class SpaceInvaders:

    life = None
    location = 0

    def __init__(self, life = 3):
        self.life = life

    def move_left(self):
        self.location -= 1
        print("move left")


    def move_right(self):
        self.location += 1
        print("move right")

si = SpaceInvaders()
print(si.life)