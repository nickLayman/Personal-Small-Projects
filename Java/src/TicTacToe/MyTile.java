package TicTacToe;

import java.util.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.*;
/**
 * Write a description of class MyTiles here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class MyTile extends JPanel implements MouseListener, Comparable{
    /** current value of the tile, 0 = clear, 1 = X, 2 = O */
    private int myValue; 

    /** is the dice currently selected? submitted? */
    private boolean selected, submitted;

    /** tile's drawing size in pixels */
    private int mySize;
    
    /** full tile size, drawing size + border */
    private int fullSize;
    
    /** larger radius for O */
    private int bigDiameter;
    
    /** smaller radius for O */
    private int smallDiameter;
    
    /** start for smaller circle in O */
    private int smallerStart;
    
    /** border of tile width */
    private int border;

    /** color of the dice when selected */
    private Color SELECTED_COLOR = Color.pink;

    /** color of the dice when scored */
    private Color SUBMITTED_COLOR = Color.gray;

    /** default color of dice */
    private Color BACKGROUND = Color.white;
    
    /** default color of Xs and Os */
    private Color DRAW_COLOR = Color.black;
    
    int xOverlap;
    
    
    
    public MyTile(int size){
        // initialize the tile and determine display characteristics 
        fullSize = size;
        border = 4;
        mySize = size - border * 2;
        selected = false;
        submitted = false;
        bigDiameter = mySize;
        smallDiameter = mySize - mySize / 4;
        smallerStart = (bigDiameter - smallDiameter) / 2 + border;
        xOverlap = size / 10;
        setBackground(BACKGROUND);
        setForeground(Color.black);
        setSize(size,size); 
        setPreferredSize(new Dimension(size, size));
        setMinimumSize(new Dimension(size, size));
        setMaximumSize(new Dimension(size, size));

        //create the fancy border
        Border raised = BorderFactory.createRaisedBevelBorder();
        Border lowered = BorderFactory.createLoweredBevelBorder();
        Border compound = BorderFactory.createCompoundBorder(raised, lowered);
        setBorder(compound);

        setValue(0);
        addMouseListener(this);
    }
    
    public MyTile(){
        this(100);
    }
    
    public int getValue(){
        return myValue;
    }
    
    public void resetTile(){
        setSelected(false);
        setSubmitted(false);
        setValue(0);
    }
    
    public void setValue(int value){
        myValue = value;
        repaint();
    }
    
    public boolean isSelected(){
        return selected;
    }
    
    public void setSelected(boolean b){
        selected = b;
    }
    
    public boolean getSubmitted(){
        return submitted;
    }
    
    public void setSubmitted(boolean b){
        submitted = b;
        setBackground(BACKGROUND);
    }
    
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        g.setColor(DRAW_COLOR);

        // paint tile
        switch (myValue){   
            case 0:
            break;
            
            case 1:
            int[] firstxx = 
                {0, xOverlap, fullSize, fullSize,
                fullSize - xOverlap, 0, 0};
            int[] firstxy = 
                {0, 0, fullSize - xOverlap, fullSize,
                fullSize, xOverlap, 0};
            int[] secondxx =
                {fullSize, fullSize - xOverlap, 0, 
                0, xOverlap, fullSize, fullSize};
            int[] secondxy = firstxy;
            
            g.fillPolygon(firstxx, firstxy, 7);
            g.fillPolygon(secondxx, secondxy, 7);
            break;
            
            case 2:
            g.fillOval(border, border, bigDiameter, bigDiameter); 
            g.setColor(BACKGROUND);
            g.fillOval(smallerStart, smallerStart, smallDiameter, smallDiameter);
            break;
        }   

    }
    
    public void mouseClicked(MouseEvent e){

        // do not allow submitted tile to be selected
        if(submitted){
            return;
        }
        
        if(selected){
            selected = false;
            setBackground(BACKGROUND);
        }else{
            selected = true;
            setBackground(SELECTED_COLOR);
        }
        
        repaint();
    }

    public void mousePressed(MouseEvent e){}

    public void mouseReleased(MouseEvent e){}

    public void mouseExited(MouseEvent e){}

    public void mouseEntered(MouseEvent e){}
    
    public int compareTo(Object o){
        MyTile t = (MyTile) o;
        return getValue() - t.getValue();
    } 
}
