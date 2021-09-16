package TicTacToe;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.text.*;
import java.util.*;

/**
 * Write a description of class TTTGUI here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class TTTGUI2Player extends JFrame implements ActionListener, KeyListener{
    /** Tic Tac Toe game rules and gameplay */
    private TTT theGame;

    /** the current player's value, X's or O's, 1 or 2 */
    private int playerVal;

    JButton submitButton;

    /** get the dice Array from the game */
    MyTile[][] theTiles;

    /** the current turn, X or O, 1 or 2 */
    int currTurn;

    /** menu items, new game and quit */
    JMenuItem resetGame, quit;

    public TTTGUI2Player(){
        int rows = Integer.parseInt(JOptionPane.showInputDialog(this, "how many rows"));

        theGame = new TTT(rows);

        /** sets up all menus - helper method */
        setupMenu();

        /** set layout manager and font */
        setLayout(new GridBagLayout());
        GridBagConstraints position = new GridBagConstraints();

        /** get the tile Array from the game */
        theTiles = theGame.getTiles();

        int x = 0;
        int y = 0;
        position.gridx = x;
        position.gridy = y;
        for (int i = 0; i < theTiles.length; i++){
            for (int j = 0; j < theTiles.length; j++){
                add(theTiles[i][j], position);
                x++;
                y++;
                position.gridx = x % theTiles.length;
                position.gridy = y / theTiles.length;
            }
        }

        currTurn = 1;
        
        /** create and place the submit button */
        submitButton = new JButton("Submit");
        position.gridx = theTiles.length / 2;
        position.gridy = theTiles.length;
        add(submitButton, position);
        submitButton.addActionListener(this);
        submitButton.setEnabled(true);
        submitButton.addKeyListener(this);
    }

    private void setupMenu(){
        JMenuBar menuBar = new JMenuBar();
        setJMenuBar(menuBar);

        JMenu fileMenu = new JMenu("File");
        menuBar.add(fileMenu);

        resetGame = new JMenuItem("Reset Game");
        fileMenu.add(resetGame);
        resetGame.addActionListener(this);

        quit = new JMenuItem("Quit");
        fileMenu.add(quit);
        quit.addActionListener(this);
    }

    public int numSelected(){
        int countSelected = 0;

        for (MyTile[] a : theTiles){
            for (MyTile t : a){
                if (t.isSelected()){
                    countSelected++;
                }
            }
        }

        return countSelected;
    }

    private boolean oneSelected(){
        return numSelected() == 1;
    }

    private void submit(){
        for (MyTile[] a : theTiles){
            for (MyTile t : a){
                if (t.isSelected()){
                    t.setSubmitted(true);
                    t.setSelected(false);
                    t.setValue(currTurn);
                    removeMouseListener(t);
                }
            }
        }

        if (theGame.winningGameOver()){
            JOptionPane.showMessageDialog(this, "WIN");
            //submitButton.setEnabled(false);
        }else if(theGame.losingGameOver()){
            JOptionPane.showMessageDialog(this, "LOSE");
        }else{
            currTurn = currTurn % 2 + 1;
        }
    }

    private void cantSubmit(){
        JOptionPane.showMessageDialog(this,"Please select one and only one tile");
    }

    public void actionPerformed(ActionEvent event){

        if (!theGame.winningGameOver() && !theGame.losingGameOver()){
            if (event.getSource() == submitButton && !oneSelected()){
                cantSubmit();
            }

            if (event.getSource() == submitButton && oneSelected()){
                submit();
            }
        }

        if (event.getSource() == resetGame){
            theGame.resetGame();
            submitButton.setEnabled(true);
            currTurn = 1;
        }

        if (event.getSource() == quit){
            System.exit(0);
        }
    }

    public void keyPressed(KeyEvent e){
        if (e.getKeyCode() == KeyEvent.VK_ENTER){
            submitButton.doClick();
        }
    }

    public void keyTyped(KeyEvent e){}

    public void keyReleased(KeyEvent e){}

    public static void main(String[] args){
        TTTGUI2Player frame = new TTTGUI2Player();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }  
}
