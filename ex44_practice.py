# This will demonstrate inheritance in python, both implicit and explicit

class Bird(object) :

    def fly(self) :
        print "Flapping my wings"

    def noise(self) :
        print "Tweet Tweet"

class Seagull(Bird) :

    def noise(self) :
        print "Sqwauk"

class LoveBird(Bird) :

    def noise(self) :
        print "Lovely bird song."

class Flamingo(Bird) :

    def fly(self) :
        print "Flamingos can't fly!"

    def noise(self) :
        print "Very Quiet"

def main() :
    
    gen_bird = Bird()
    seagull = Seagull()
    lovebird = LoveBird()
    flamingo = Flamingo()

    gen_bird.fly()
    gen_bird.noise()

    seagull.fly()
    seagull.noise()

    lovebird.fly()
    lovebird.noise()

    flamingo.fly()
    flamingo.noise()

if __name__ == "__main__" :
    main()