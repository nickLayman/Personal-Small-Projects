package Blackjack;

/**
 * rules and background of Blackjack game
 *
 * @author Nick Layman 
 * @version 12/12/2018
 */
public class Blackjack{
    private Card[] allCards;
    
    private cardBuilder builder;
    
    public Blackjack(){
        builder = new cardBuilder();
        allCards = builder.getAllCards();
    }
    
    public Card[] getAllCards(){
        return allCards;
    }
    
    public boolean isBusted(Player p){
        return p.getScore() > 21;
    }
    
    public static void main(){
        Blackjack game = new Blackjack();
        for (Card c : game.allCards){
            System.out.println(c);
        }
    }
}
