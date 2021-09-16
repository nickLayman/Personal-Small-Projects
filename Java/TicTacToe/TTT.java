package TicTacToe;

/**
 * Write a description of class TTT here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class TTT{
    private MyTile[][] theTiles;

    private int numRows;

    private int winningInARow;

    public TTT(){
        numRows = 3;
        theTiles = new MyTile[numRows][numRows];
        for (int i = 0; i < numRows; i++){
            for (int j = 0; j < numRows; j++){
                theTiles[i][j] = new MyTile();
            }
        }
    }
    
    public TTT(int rows){
        numRows = rows;
        theTiles = new MyTile[numRows][numRows];
        for (int i = 0; i < numRows; i++){
            for (int j = 0; j < numRows; j++){
                theTiles[i][j] = new MyTile();
            }
        }
    }

    public MyTile[][] getTiles(){
        return theTiles;
    }

    public void resetGame(){
        for (MyTile[] a : theTiles){
            for (MyTile t : a){
                t.resetTile();
            }
        }
    }

    public boolean winningGameOver(){
        winningInARow = numRows;
        int inARow;

        //check rows for win
        for (int r = 0; r < numRows; r++){
            inARow = 0;

            for (int c = 0; c < numRows; c++){
                if (theTiles[r][c].getValue() == 0){
                    inARow--;
                }else if (theTiles[r][c].getValue() == theTiles[r][0].getValue()){
                    inARow++;
                }
            }

            if (inARow == winningInARow){
                return true;
            }
        }
        
        //check columns 
        for (int c = 0; c < numRows; c++){
            inARow = 0;
            
            for (int r = 0; r < numRows; r++){
                if (theTiles[r][c].getValue() == 0){
                    inARow--;
                }else if (theTiles[r][c].getValue() == theTiles[0][c].getValue()){
                    inARow++;
                }
            }
            
            if (inARow == winningInARow){
                return true;
            }
        }
        
        //check first diagonal
        inARow = 0;
        for (int n = 0; n < numRows; n++){
            if (theTiles[n][n].getValue() == 0){
                    inARow--;
                }else if (theTiles[n][n].getValue() == theTiles[0][0].getValue()){
                    inARow++;
                }
                
            if (inARow == winningInARow){
                return true;
            }
        }
        
        //check second diagonal
        inARow = 0;
        for (int r = 0; r < numRows; r++){
            if (theTiles[r][numRows - r - 1].getValue() == 0){
                inARow--;
            }else if (theTiles[r][numRows - r - 1].getValue() == theTiles[0][numRows - 1].getValue()){
                inARow++;
            }
                
            if (inARow == winningInARow){
                return true;
            }
        }
        
        return false;
    }
    
    public boolean losingGameOver(){
        int numTilesLeft = 0;
        
        for (MyTile[] a : theTiles){
            for (MyTile t : a){
                if (!t.getSubmitted())
                    numTilesLeft++;
            }
        }
        
        return numTilesLeft == 0;
    }
}
