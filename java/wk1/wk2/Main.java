package java.wk1.wk2;

import java.util.Random;

/**
 * Main
 */
public class Main {

        public static void main(String[] args) {
              // Loop to print 6 sentences with prepositional phrases in past, present, and future tense
        for (int i = 1; i <= 6; i++) {
            int quantity = (i < 3) ? 1 : 2;  // single or plural
            String tense;

            switch (i % 3) {
                case 1:
                    tense = "past";
                    break;
                case 2:
                    tense = "present";
                    break;
                default:
                    tense = "future";
                    break;
            }

            System.out.println(makeSentence(quantity, tense));
        }
    }

    public static String makeSentence(int quantity, String tense) {
        // Build and return a sentence with a determiner, noun, verb, and prepositional phrase
        String sentence = capitalize(getDeterminer(quantity)) + " " +
                          getNoun(quantity) + " " +
                          getVerb(quantity, tense) + " " +
                          getPrepositionalPhrase(quantity) + ".";
        return sentence;
    }
    public static String getNoun(int quantity) {
        // Return a randomly chosen noun
        String[] nounsSingular = {"bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"};
        String[] nounsPlural = {"birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"};
        
        String[] nouns = (quantity == 1) ? nounsSingular : nounsPlural;
        return randomChoice(nouns);
    }

    public static String getVerb(int quantity, String tense) {
        // Return a randomly chosen verb based on tense
        String[] pastVerbs = {"drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"};
        String[] presentVerbs = {"drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"};
        String[] futureVerbs = {"will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"};
        
        String[] verbs;
            switch(tense) {
                case "past":
                    verbs = pastVerbs;
                    break;
                case "present":
                    verbs = presentVerbs;
                    break;
                default:
                    verbs = futureVerbs;
                    break;
            }
        
        return randomChoice(verbs);
    }

    public static String getDeterminer(int quantity) {
        // Return a randomly chosen determiner
        String[] singularDeterminers = {"a", "one", "the"};
        String[] pluralDeterminers = {"some", "many", "the"};
        
        String[] determiners = (quantity == 1) ? singularDeterminers : pluralDeterminers;
        return randomChoice(determiners);
    }

    public static String getPreposition() {
        // Return a randomly chosen preposition
        String[] prepositions = {"about", "above", "across", "after", "along", "beyond", "by", "despite", "except", "for",
                                 "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to",
                                 "under", "with", "without"};
        return randomChoice(prepositions);
    }

    public static String getPrepositionalPhrase(int quantity) {
        // Build and return a prepositional phrase with a preposition, determiner, and noun
        return getPreposition() + " " + getDeterminer(quantity) + " " + getNoun(quantity);
    }

    public static String capitalize(String str) {
        // Capitalize the first letter of a string
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }

    public static String randomChoice(String[] choices) {
        // Return a randomly chosen string from an array
        Random random = new Random();
        int index = random.nextInt(choices.length);
        return choices[index];
    }
}