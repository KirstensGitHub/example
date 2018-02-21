import random
from .helpers import first_phrase

class chatter:
    """
    This class is used to generate lab chatter and conversations
    """
    def make(gender, category=None):

    """
        generates chatter from a lab member meeting the specified parameters

        Parameters
        ----------
        gender : str
            gender of lab member ('m'/'f')

        category : str
            type of lab member ('post_doc', 'student', 'PI')

        Returns
        ----------
        utterance : string
            phrase simulating cdl chit chat

    """

        males = ['jeremy', 'andy', 'paxton']
        females = ['lucy', 'gina', 'kirsten', 'emily']

        if category == 'PI':
            name = 'jeremy'

        elif gender == 'm':
            if category == 'post_doc':
                name = 'andy'
            elif category == 'student':
                name = 'paxton'
            else:
                name = random.choice(males)

        else :
            if category == 'post_doc':
                name = 'gina'
            elif category == 'student':
                name = random.choice(['lucy', 'kirsten'])
            else:
                name = random.choice(females)

        # output #
        utterance = first_phrase(name)
        return(utterance)

    def add_valence(phrase, mood):
        """
            adds valence to inputted utterance

            Parameters
            ----------
            phrase : str
                any desired string, can be passed from chatter.make()

                mood : str
                    desired valence ('+', '-')

            Returns
            ----------
            mood_phrase : string
                phrase with valence clause
        """

        if mood == '+':
            mood_phrase = phrase + 'it\'s AWESOME!!'
        else:
            mood_phrase = phrase + 'it\'s terrible.'

        return(mood_phrase)

class convo:
    def make(gender1, gender2, valence1, valence2):
        """
        input:
        + gender1: str - gender of lab member ('m'/'f')
        + gender2: str - gender of lab member ('m'/'f')
        + valence1: str - ('+', '-')
        + valence2: str - ('+', '-')
        """
        sentence1 = chatter.add_valence(chatter.make(gender1), valence1)
        sentence2 = chatter.add_valence(chatter.make(gender2), valence2)

        conversation = 'Hey! ' + sentence1 + '.       Oh really? Well, ' + sentence2

        return(conversation)

class other:
    """
    This class is designed to return random lab phrases about various topics
    """
    def food():
        """
            returns random food phrase

            Parameters
            ----------


            Returns
            ----------
            food_phrase : string
                string about food
        """
        return(random.choice(['hungry for Zahav cauliflower',
                              'who\'s on milk this week?',
                              'Weirdo Lady is selling delicious soup']))

    def furniture():
        """
            returns random food phrase

            Parameters
            ----------


            Returns
            ----------
            furniture_phrase : string
                string about furniture
        """
        return(random.choice(['you may fall off the stool and die',
                              'how many lamps can we fit in the reading nook?',
                              'Party Parrot Pillow Alliteration!']))

    def travel():
        """
            returns random travel phrase

            Parameters
            ----------

            Returns
            ----------
            travel_phrase : string
                string about travel
        """
        return(random.choice(['I hear that if you fly out of Lebanon, you will die',
                              'Dartmouth Coach at 6am unless I oversleep and miss it..',
                              'I\'m going to start ice skating into work',
                              'maybe Jeremy secretly drives to school, but parks somewhere we can\'t see']))
