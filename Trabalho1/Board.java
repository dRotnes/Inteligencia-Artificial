public class Board {
    private int[][] table;
    private int blank_row;
    private int blank_col;

    Board(int[][] b, int br, int bc){
        table = b;
        blank_row = br;
        blank_col = bc;
    }

    int getBlankRow(){
        return blank_row;
    }

    int getBlankCol(){
        return blank_col;
    }

    int[][] getTable(){
        return table;
    }

    // void setBlankRow(int br){
    //     blank_row = br;
    // }

    // void setBlankCol(int bc){
    //     blank_col = bc;
    // }
}
