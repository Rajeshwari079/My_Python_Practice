 
class Anime:
    def __init__(self, title, genre, episodes):
        self.title = title
        self.genre = genre
        self.episodes = episodes

    def start(self):
        print('Open animwatch ...')

    def watch(self):
        print('watch 30 eps...')

    def sleep(self):
        print('good night........')

class AniFan:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        t=input('enter the name of anime : ')
        g=input('enter the genre of anime : ')
        e=input('enter the no of eps of anime : ')

        ani = Anime(t,g,e)
        self.anime=ani

    def watching(self):
        print(f'{self.name} has wished to watch an anime ')
        self.anime.start()
        self.anime.watch()
        self.anime.sleep()

raji = AniFan('Rajeshwari',22)
raji.watching()