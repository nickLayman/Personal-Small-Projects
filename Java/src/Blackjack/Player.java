package Blackjack;

import java.util.*;
/**
 * Makes player to be used for blackjack
 *
 * @author Nick Layman
 * @version 12/16/2018
 */
public class Player{
    private int moneyLeft;
    
    private String name;
    
    private ArrayList<Card> cards;
    
    private int score;
    
    public Player(String pName){
        name = pName;
        moneyLeft = 100;
        cards = new ArrayList<Card>();
        score = 0;
    }
    
    public Player(String pName, int pMoneyLeft){
        name = pName;
        moneyLeft = pMoneyLeft;
    }
    
    public void setName(String pName){
        name = pName;
    }
    
    public String getName(){
        return name;
    }
    
    public void setMoneyLeft(int pMoneyLeft){
        moneyLeft = pMoneyLeft;
    }
    
    public int getMoneyLeft(){
        return moneyLeft;
    }
    
    public void addCard(Card c){
        cards.add(c);
    }
    
    public ArrayList<Card> getCards(){
        return cards;
    }
    
    public int getScore(){
        int score = 0;
        
        for (Card c : cards){
            if (c.getValue() < 10){
                score += c.getValue();
            }else{
                score += 10;
            }
        }
        
        return score;
    }
}
