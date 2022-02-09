class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print('Jabi')

def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck) -> None:
    birdie.quack()

def alert_bird(birdie: Bird) -> None:
    birdie.quack()
