package Blackjack;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
// import java.text.*;
import java.util.*;
/**
 * Write a description of class BlackjackGUI here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class BlackjackGUI extends JFrame implements ActionListener{
    private Blackjack game;

    private Player dealer;
    
    private Player gambler;
    
    private Card[] cards;

    private Random rand = new Random();
    
    JButton hitButton, standButton;
    
    JMenuItem resetGame, quit;

    public BlackjackGUI(){
        game = new Blackjack();
        setUpGUI();

        dealer = new Player("Dealer");
        gambler = new Player("Gambler");
        
        cards = game.getAllCards();
        shuffleCards(cards);
        
        newRound();
    }
    
    public void setUpGUI(){
        setLayout(new GridBagLayout());
        GridBagConstraints position = new GridBagConstraints();
        
        hitButton = new JButton("Hit");
        hitButton.addActionListener(this);
        standButton = new JButton("Stand");
        standButton.addActionListener(this);
        
        position.gridx = 0;
        position.gridy = 0;
        add(hitButton, position);
        
        position.gridx = 1;
        add(standButton, position);
    }

    public void newRound(){
        giveCard(dealer);
        giveCard(gambler);
        giveCard(dealer);
        giveCard(gambler);
    }
    
    public void shuffleCards(Card[] pCards){
        Card[] initialCards = cards;
        Card[] shuffled = new Card[cards.length];
        
        for(Card c : initialCards){
            int pos;
            
            do{
                pos = rand.nextInt(cards.length);
            } while (shuffled[pos] != null);
            
            shuffled[pos] = c;
        }
        
        cards = shuffled;
    }

    public void giveCard(Player p){
        p.addCard(cards[0]);
        
        Card first = cards[0];
        for (int i = 0; i < cards.length - 1; i++){
            cards[i] = cards[i + 1];
        }
        cards[cards.length - 1] = first;
    }
    
    public void showAllCards(){
        System.out.println();
        
        for (Card c : dealer.getCards()){
            System.out.println("Dealer: " + c);
        }
        
        for (Card c : gambler.getCards()){
            System.out.println("Gambler: " + c);
        }
    }
    
    public void showAllScores(){
        int dealerScore = 0;
        int gamblerScore = 0;
        
        for (Card c : dealer.getCards()){
            dealerScore += c.getValue();
        }
        
        for (Card c : gambler.getCards()){
            gamblerScore += c.getValue();
        }
        
        System.out.println();
        System.out.println("Dealer: " + dealerScore);
        System.out.println("Gambler: " + gamblerScore);
    }
    
    public void actionPerformed(ActionEvent event){
        if (event.getSource() == hitButton){
            giveCard(gambler);
            showAllScores();
        }
        
        if(game.isBusted(gambler)){
            System.out.println("BUSTED");
        }
    }

    public static void main(String[] args){
        BlackjackGUI GUI = new BlackjackGUI();
        GUI.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        GUI.pack();
        GUI.setVisible(true);
        GUI.showAllScores();
    }
}
