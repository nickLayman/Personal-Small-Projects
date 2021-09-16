package Blackjack;

/**
 * Write a description of class allCards here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class cardBuilder{
    private Card[] allCards;
    
    private Card[] deck;
    
    private final int NUM_SUITS = 4;
    
    private final int NUM_VALUES = 13;
    
    private final int NUM_DECKS = 3;
    
    private int currDecks;
    
    private final int CARDS_PER_DECK = NUM_SUITS * NUM_VALUES;
    
    private final int NUM_CARDS = NUM_DECKS * CARDS_PER_DECK;
    
    public cardBuilder(){
        currDecks = 0;
        allCards = new Card[NUM_CARDS];
        for (int i = 0; i < NUM_DECKS; i++){
            addDeck();
            currDecks++;
        }
    }
    
    private void addDeck(){
        deck = new Card[CARDS_PER_DECK];
        
        for(int s = 0; s < NUM_SUITS; s++){
            for(int v = 0; v < NUM_VALUES; v++){
                int pos = (s * NUM_VALUES) + v;
                deck[pos] = new Card(s + 1, v + 1);
            }
        }
        
        for (int p = 0; p < deck.length; p++){
            allCards[p + CARDS_PER_DECK * currDecks] = deck[p];
        }
    }
    
    public Card[] getAllCards(){
        return allCards;
    }
    
    public int getNumDecks(){
        return NUM_DECKS;
    }
}
