package Blackjack;

/**
 * Makes a single card
 * integer suit value, integer face values
 *
 * @author Nick layman
 * @version 12/12/2018
 */

public class Card{
    /***************************************************************
     * suit of card 1, 2, 3, 4
     * club, diamond, heart, spade
     **************************************************************/
    private int suit;
    
    /**************************************************************
     * value of card 1 - 13
     * ace - king
     *************************************************************/
    private int value;
    
    /*************************************************************
     * Constructor, sets card's value to given values
     * @param suitp the suit of the card
     * @param valuep the value of the card
     *************************************************************/
    public Card(int psuit, int pvalue){
        suit = psuit;
        value = pvalue;
    }
    
    public void setSuit(int psuit){
        suit = psuit;
    }
    
    public int getSuit(){
        return suit;
    }
    
    public void setValue(int pvalue){
        value = pvalue;
    }
    
    public int getValue(){
        return value;
    }
    
    public String toString(){
        String printCard = "";
        printCard = value + " of " + suit;
        return printCard;
    }
}
