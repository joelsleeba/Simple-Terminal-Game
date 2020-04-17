# coding: utf-8
import time, random, sys, string, hashlib


def simtype(text, *, end = '\n', sep = '', sltime = 0.07):
    """Simulate typing in desired sleeptime"""
    text = list(text)
    text.append(end)
    for i in text:
        sys.stdout.write(i)
        sys.stdout.write(sep)
        sys.stdout.flush()
        time.sleep(sltime)




class Scene():
    
    def enter(self):
        print("Hello")
        return True




class Engine():
    """Heart of the Game. Controls Scenes, Victory and Death, This is the command station to run scenes according to the output of last scene"""
    
    
    def __init__(self, map):
        self.map = map
    
    def play(self):
        while self.map.current_scene < 6:
            if self.map.nextscene(self.map.current_scene):
                self.map.current_scene += 1
            else:
                self.map.current_scene = 0
        self.map.nextscene(self.map.current_scene)




class Death(Scene):
    """Death Class. Output a random deathnote, to the wounded bounty hunter"""
    
    deathnote = ["You died. You kinda suck at this.",
                 "Your Mom would be proud...if she were smarter.",
                 "Maranam Varumoru naal Orkkuka marthya nee....",
                 "I have a small puppy that's better at this.",
                 "Enthutt koppada panni kanikkane?",
                 "Chettanu ithinepatti vellya dharana onnum illalle."]
    
    def enter(self):
        simtype(random.choice(Death.deathnote))
        simtype("You're Dead")
        print('\n'*2)
        time.sleep(1)
        simtype('Auto Restarting', end = '')
        simtype('....', sltime = 0.9, sep = ' ', end = '')
        return True




class LoadingScreen(Scene):
    
    def enter(self):
        simtype('Welcome to the Game', sltime = 0.4, end = '')
        time.sleep(3)
        return True




class Initiation(Scene):
    """First Scene of the Game. The bounty hunter is given a very different job"""
    
    content1 = 'After years of pollution, when the planet was on the verge of distruction, came the alien species, \"Timer\". They carried many inhabitants of the planet to Azog C-135, an earth like planet in the Pleidas Starcluster. Though the Timerians didn\'t inhabit Azog, they were constantly there for trade and work. Among work done in Azog, construction and cultivation were given top priority. Blessed farmers and skilled craftsmen made their marks in the new planet. Unlike earth it was too early in Azog for an established system of commerce. Among the jobs, the ambitious one was that of the bounty hunter. It promised good pay and people liked the thrill of it.'
    content2 = 'A new Timerian pod have arrived at the base. This seems special. Also you are asked to be immediately at the base. You have to rush. There might be a big fish to fry.'
    content3 = 'Welcome Mando, the tales of your valour and your creed is well known in the Empire. You have made a very good fortune as a bounty hunter. The King know all about that and appreciate you for your amazing work.'
    content4 = 'Word have come to us that the prince of Timer have been captured by a long forgotten enemy, Roh. We first planned to send our army to Roh, but soon discovered that it won\'t end well. The King want you to go in secret without the knowledge of the enemy and rescue the Prince. The king have offered you 20 baskars, so huge a reward for a seemingly small task. Also the king insists upon the good health of the prince. You will find help from our spies in Roh'
    content11 = 'You are the best bounty hunter in Azog, People of Azog, humans and timeriains call you Mando. Impressed by your fighting skills, timerians made you the leader of the bounty hunter\'s guild. You are now bound by the guild code and the responsibility of keeping the code in the guild is now in your shoulders'
    
    def enter(self):
        simtype(Initiation.content1)
        print('\n ')
        time.sleep(2)
        simtype(Initiation.content11)
        print('\n\n')
        time.sleep(4)
        simtype(Initiation.content2)
        print('\n')
        time.sleep(2)
        print('Timerian Captain:')
        simtype(Initiation.content3)
        time.sleep(2)
        print('\nTimerian Captain:')
        simtype(Initiation.content4)
        time.sleep(2)
        input('\nPress any key to contiue >')
        return True




class Fight(Scene):
    """Third Scene. Rearranged for the Rescue scene to uses its class variables."""
    
    content1 = 'You manage to get inside the building. You searched for a while but managed to find prince in good health. Now you must get out of that building safely. But you can\'t do it alone. You need help from the Timerian spies outside the building. You find the signal to call them encoded in runes. You need to decode it and alert them for rescue. '
    
    wordlist = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward',
                'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper',
                'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful',
                'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords',
                'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle',
                'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves',
                'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook',
                'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby',
                'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy',
                'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly',
                'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen',
                'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice',
                'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx',
                'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy',
                'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte',
                'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths',
                'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave',
                'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull',
                'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo',
                'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche',
                'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz',
                'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw',
                'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk',
                'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied',
                'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz',
                'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth',
                'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen',
                'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave',
                'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever',
                'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern',
                'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr',
                'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']
    
    def enter(self):
        simtype(Fight.content1)
        time.sleep(2)
        return Fight.Hangman()
    
    @staticmethod
    def Hangman():
        word = random.choice(Fight.wordlist).upper()
        guess = ['-' for k in range(len(word))]
        j , limit = 0, len(set(word))+8
        while j < limit:
            print('\n')
            print(' '.join(guess))
            print(f'{limit-j} attempts remaining')
            temp1 = input('Guess the letter: ')
            if temp1.isalpha():
                temp = temp1.upper()
                j += 1
                time.sleep(1)
                if temp in list(word):
                    print('HURRAY!, Letter in Word')
                    for i in range(len(word)):
                        if word[i] == temp:
                            guess[i] = temp
                else:
                    print("Letter not in Word")
            else:
                print("Not a valid letter")
            if ''.join(guess) == word:
                print(f'Rune Decoded: {word}')
                time.sleep(2)
                return True
        print(f'\n\nRune was {word} \n You Lose')
        time.sleep(2)
        return False




class Rescue(Scene):
    """Second Scene. Player goes to rescue the prince from Roh."""

    content1 = 'You reached Roh. With the help of the tacking fob, you managed to find the safekeep where the prince is kept. But you notice that it is guarded heavily by Rohians, and you need the house password to get inside the building. So, you decide to eavesdrop on the soldiers going inside. '
    content2 = 'The trick worked. You managed to get almost all of the password, but it is now in a scrambled order. You need to unscramble it and get a reasonable word as password'    
    
    def enter(self):
        simtype(Rescue.content1)
        time.sleep(2)
        simtype(Rescue.content2)
        time.sleep(2)
        word = random.choice(Fight.wordlist).upper()
        wordscram = Rescue.scramble(word)
        for i in range(5):
            print('\n')
            print(wordscram)
            print(f'{5-i} attempts remaining')
            temp = input("Guess the scrambled password: ").upper()
            time.sleep(1)
            if temp == word:
                print(f'You Guessed it right. Password is {word}')
                time.sleep(2)
                return True
            else:
                print('Pling! Wrong Word.')
        print(f'\n\nPassword was : {word} \n You Lose')
        time.sleep(2)
        return False
    
    @staticmethod
    def scramble(word):
        word = list(word.upper())
        temp = ''
        for i in range(len(word)):
            index = random.randint(0,len(word)-1)
            temp += word.pop(index)
        return temp




class Escape(Scene):
    
    content1 = 'Good job. You managed to inform Temerian spies outside the safekeep. It was just a matter of seconds after skilled Temeriain spies rushed in and massacred every enemy soldier. You and the prince got out of the building. You must now quikly escape from there. You need a pod to get out of there. One of the spies inform you of a a nearby spybase. You and the prince rush to there.'
    content2 = 'You managed to reach at the base quickly. But, alas!, no pod there is now in a working condition. All the working pods are already in use. You must now quickly do something.'
    content3 = 'The One who programmed this game (@joel.sleeba), wasn\'t expecting this situation. So, it seems like you need to edit the code of the game and programme a rescue method. But this wicked One have encrypted this game with a password. You can\'t change any part of the code unless you can find that passcode. Here\'s a little help. This game seems to follow the structure of a recent T.V series. He might\'ve used the name of that T.V series as the pasSword to encrypt the game. Try your best.'
    
    def enter(self):
        simtype(Escape.content1)
        print('')
        time.sleep(2)
        simtype(Escape.content2)
        print('')
        time.sleep(2)
        simtype(Escape.content3)
        print('')
        time.sleep(2)
        return Escape.series()
    
    
    @staticmethod
    def series():
        lshash = [b'K\x136\xf8\xd0\x9aC\x90c\x1d<\x7fH\xcf\x8c\x16', b'\xc4\xf7X\xa2"\xf9\xf4^\xfc\xa4\xf2F\x92N\x11\xae', b'\x97:V\x0b\x02i\x8e7c\x051O\xb9-\xd3\x15']
        for i in range(5):
            print('\n')
            print(f'{5-i} attempts remaining')
            guess = hashlib.md5(input("Guess the password of the game: ").upper().encode()).digest()
            time.sleep(1)
            if guess in lshash:
                print('Good! You have decrypted the code!')
                time.sleep(2)
                return True
            else:
                print('Wrong Guess')
        print('\nYou Lose')
        time.sleep(2)
        return False




class Victory(Scene):
    
    content1 = 'You won! all of Timeria and Azog sing your praises. In gratitude, the King made you the chief of Azog. Your valor and courage will be sung in many songs all across Timer for a thouasand years.'
    
    def enter(self):
        simtype(Victory.content1)
        print('')
        time.sleep(3)
        quit()




class Map():
    
    data = [Death(), LoadingScreen(), Initiation(), Rescue(), Fight(), Escape(), Victory()]
    
    def __init__(self):
        self.current_scene = 1

    def nextscene(self, current_scene):
        self.scene = Map.data[self.current_scene]
        print('\n'*100)
        simtype('Loading', end = '')
        simtype('....', sltime = 1, sep = ' ', end = '')
        print('\n'*100)
        return self.scene.enter()



a = Map()
game = Engine(a)
game.play()