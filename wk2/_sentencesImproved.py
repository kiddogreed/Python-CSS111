#Author JOHN RUSSELLE DOMINGO
#version 2
"""Write a Python program named sentences.py that generates simple English sentences. During this prove milestone, you will write functions that generate sentences with three parts:
    a determiner (sometimes known as an article)
    a noun
    a verb
main
make_sentence
get_determiner
get_noun
get_verb
get_preposition
get_prepositional_phrase
"""
import random
def main():
    #using loop to print 6 sentence+prepositional phrase with past,present.future
    for i in range(1, 7):
        quantity = 1 if i < 3 else 2 #single or plural
        if i % 3 == 1:
            tense = "past"
        elif i % 3 == 2:
            tense = "present"
        else:
            tense = "future"
        print(make_sentence(quantity, tense))
        
        #    if i < 3:
        #     quantity = 1
        #     if i == 1:
        #         tense = "past"
        #     elif i == 2:
        #         tense = "present"
        #     else:
        #         tense = "future"
        # else:
        #     quantity = 2  # plural
        #     if i == 4:
        #         tense = "past"
        #     elif i == 5:
        #         tense = "present"
        #     else:
        #         tense = "future"
   
    # print(make_sentence(1,"past"))
    # print(make_sentence(1,"present"))
    # print(make_sentence(1,"future"))
    # print(make_sentence(2,"past"))
    # print(make_sentence(3,"present"))
    # print(make_sentence(4,"future"))
    
def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    sentence = f"{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_verb(quantity,tense)} {get_prepositional_phrase(quantity)}."
    #sentence = f"{get_prepositional_phrase(quantity)} {get_noun(quantity)} {get_verb(quantity,tense)}."
    return sentence

def get_noun(quantity):
    """Return a randomly chosen noun. """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun
        

def get_verb(quantity, tense):
    """Return: a randomly chosen verb."""
    if tense == "past":
        verbs = [ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
            verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    else :
            verbs = [ "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    verb = random.choice(verbs)
    return verb            


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".
    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_preposition():
  """Return a randomly chosen preposition"""
  prepositions = [ "about", "above", "across", "after", "along", "about", "above", "across", "after", "along",
                     "beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of",
                      "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
  preposition = random.choice(prepositions)
  return preposition

def get_prepositional_phrase(quantity):
  """Build and return a prepositional phrase composed
  of three words: a preposition, a determiner, and a
  noun by calling the get_preposition, get_determiner,
  and get_noun functions.
  Parameter
      quantity: an integer that determines if the
          determiner and noun in the prepositional
          phrase returned from this function should
          be single or pluaral.
  Return: a prepositional phrase.
  """  
  return f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}"
  
main()

"""explanation
    1.The program will execute the main() method
    2.The main will call make_sentence() 
    3.inside the make_sentence() function, program will execute getnoun,getverb,and getdeterminer.
    4.The get_noun(), get_verb(), get_determiner() has an examples depends on the value which will passed to them
    will return result using random.choice.
    5.Using f string to combine the results of 
    get_noun(), get_verb(), get_determiner() to format in a desired output
    6.call the str.capitalized inside the f sting
    7.repeat for seven times as the number of make_sentence is called
    8.display output
"""