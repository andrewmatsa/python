class SonyWalkMan:

    status = False
    current_song = []

    def start(self, playlist):
        import random
        self.status = True
        self.current_song = playlist[random.randrange(len(playlist))]
        return self.current_song

    def stop(self):
        self.status = False
        return self.status

    def __str__(self):
        if self.status:
            return "Current song is: %s" % self.current_song
        else:
            return "Playlist is stopped"

class Human:
    name = ''
    second_name = ''
    player = SonyWalkMan()
 
    def __init__(self, weight):
        self.weight = weight
 
    def eat(self, eat_wight):
        self.weight += eat_wight
        return self.weight
 
    def run(self, run_weight):
        self.weight -= run_weight
        return self.weight
 
 
def main():
    person = Human(60)
    person.name = 'Ivan'
    person.second_name = 'Petrov'
    print person.name, person.second_name, person.weight
    print person.eat(20)
    print person.run(30)
    print person.name, person.second_name, person.weight
 
    playlist = ['song1', 'song2', 'song3', 'song4', 'song5']

    person.player.start(playlist)
    print person.player
    person.player.stop()
    print person.player
 
 
if __name__ == '__main__':
    main()