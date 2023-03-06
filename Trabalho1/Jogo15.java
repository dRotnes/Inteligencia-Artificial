import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

class Board{
    int[][] table;
    int blank_row;
    int blank_col;
    String string_table;

    Board(int[][] t,int br, int bc, String st){
        table = t;
        blank_row = br;
        blank_col = bc;
        string_table = st;
    }
    boolean compareBoard(Board boardToCompare){
        return string_table.equals(boardToCompare.getStringTable());
    }
    int[][] getTable(){
        return table;
    }

    int getBlankRow(){
        return blank_row;
    }
    
    int getBlankCol(){
        return blank_col;
    }

    String getStringTable(){
        return string_table;
    }
}

class BoardNode{
    Board board;
    ArrayList<Board> children;

    BoardNode(Board b, ArrayList<Board> c){
        board = b;
        children = c;
    }
    ArrayList<Board> getChildren(){
        return children;
    }
    Board getBoard(){
        return board;
    }

}
class Jogo15{


    // test solvability of initial board
    static boolean testSolvability(int blank_row, int num_inversions){
        if(blank_row%2 != 0 && num_inversions%2 != 0){
            return true;
        }
        else if(blank_row%2 == 0 && num_inversions%2 == 0){
            return true;
        }
        else{
            return false;
        }
    }

    static boolean checkIfSolution(Board board){
        String solution = "1234567891011121314150";
        return board.getStringTable().equals(solution);
        
        // int last_num = -1;
        // if(table[table.length-1][table.length-1] == 0){
        //     for(int i = 0; i<table.length - 1; i++){
        //         for(int j = 0; j<table.length; j++){
        //             if(last_num > table[i][j] && table[i][j] != 0){
        //                 return false;
        //             }
        //             last_num = table[i][j];
        //         }
        //     }
        //     return true;
        // }
        // return false;
    }

    static String getStringTable(int[][] table){
        String string_matrix = "";
        for(int i = 0; i < table.length; i++){
            for(int j = 0; j < table.length; j++){
                string_matrix += Integer.toString(table[i][j]);
            }
        }
        return string_matrix;
    }

    static int[][] createNewTable(int[][] table){
        int[][] new_table = new int[4][4];
        
        for(int i = 0; i < table.length; i++){
            for(int j = 0; j < table.length; j++){
                new_table[i][j] = table[i][j];
            }
        }
        return new_table;
    }

    static Board moveRight(int[][] table, int blank_row, int blank_col){

        int[][] new_table = createNewTable(table);
        
        int moveRight = new_table[blank_row][blank_col + 1];
        new_table[blank_row][blank_col + 1] = 0;
        new_table[blank_row][blank_col] = moveRight;

        return new Board(new_table, blank_row, blank_col + 1, getStringTable(new_table));
    }

    static Board moveLeft(int[][] table, int blank_row, int blank_col){

        int[][] new_table = createNewTable(table);

        int moveLeft = new_table[blank_row][blank_col - 1];
        new_table[blank_row][blank_col - 1] = 0;
        new_table[blank_row][blank_col] = moveLeft;

        return new Board(new_table, blank_row, blank_col - 1, getStringTable(new_table));
    }

    static Board moveUp(int[][] table, int blank_row, int blank_col){

        int[][] new_table = createNewTable(table);

        int moveUp = new_table[blank_row - 1][blank_col];
        new_table[blank_row - 1][blank_col] = 0;
        new_table[blank_row][blank_col] = moveUp;
    
        return new Board(new_table, blank_row - 1, blank_col, getStringTable(new_table));
    }

    static Board moveDown(int[][] table, int blank_row, int blank_col){

        int[][] new_table = createNewTable(table);

        int moveUp = new_table[blank_row + 1][blank_col];
        new_table[blank_row + 1][blank_col] = 0;
        new_table[blank_row][blank_col] = moveUp;

        return new Board(new_table, blank_row + 1, blank_col, getStringTable(new_table));
    }

    static BoardNode calculateNextPossibilites(Board board){

        int blank_col = board.getBlankCol();
        int blank_row = board.getBlankRow();

        ArrayList<Board> children = new ArrayList<Board>();
        
        if(blank_col + 1 <= 3){ //if it can be moved right
            Board new_board = moveRight(board.getTable(), blank_row, blank_col);
            // System.out.println("RIGHT: " + new_board.getStringTable());
            children.add(new_board);            
        }
        if(blank_col - 1 >=0){ //if it can be moved left
            Board new_board = moveLeft(board.getTable(), blank_row, blank_col);
            // System.out.println("LEFT: " +new_board.getStringTable());
            children.add(new_board);              
        }
        if(blank_row - 1 >=0){ //if it can be moved up
            Board new_board = moveUp(board.getTable(), blank_row, blank_col);
            // System.out.println("TOP: "+new_board.getStringTable());
            children.add(new_board);               
        }
        if(blank_row + 1 <=3){ //if it can be moved down
            Board new_board = moveDown(board.getTable(), blank_row, blank_col);
            // System.out.println("DOWN: "+new_board.getStringTable());
            children.add(new_board);             
        }
        BoardNode node = new BoardNode(board, children);
        return node;
    }

    // static void DepthFirstSearchRec(Stack<Board> stack, ArrayList<String> visited_nodes, int depth){
    //     if(stack.isEmpty()){
    //         System.out.println("\nEmpty Stack");
    //     }
    //     Board current_node = stack.pop();
        
    // }

    static void DepthFirstSearch(Board initial_board){
        BoardNode root = calculateNextPossibilites(initial_board);
        Stack<BoardNode> stack = new Stack<BoardNode>();
        ArrayList<String> visited_nodes = new ArrayList<String>();
        int depth = 0;
        stack.add(root);
        while(!stack.isEmpty()) {
            BoardNode node = stack.pop();
            Board current_board = node.getBoard();
            if(checkIfSolution(current_board)){
                System.out.println("Solution Found in: " + depth + " movements");
                return;
            }
            if(!visited_nodes.contains(current_board.getStringTable())){
                visited_nodes.add(current_board.getStringTable());
                if(node.getChildren().size() > 0  ){
                    for(Board child : node.getChildren()){
                        BoardNode new_node = calculateNextPossibilites(child);
                        stack.add(new_node);
                    }
                    depth++;      
                }
            }
        } 
        System.out.println("No solution found");
    }

    public static void main(String[] args) {

        int[][] initial_table = new int[4][4]; // default definition of a game of 15(4x4)
        
        int num_inversions = 0; // counter for the number of inversions
        int last_num = -1; // initialize last_num as -1 so that its always lower than the initial number of the matrix
        int blank_row = 0; // initialize blank_row as 0
        int blank_col = 0; // inititalize blank_col as 0
        String string_matrix = "";

        // Scanner reading initital sequence and setting initial_table
        try(Scanner scanner = new Scanner(System.in)){
            for(int i = 0; i<initial_table.length; i++){
                for(int j = 0; j<initial_table.length; j++){
                    int num = scanner.nextInt();
                    initial_table[i][j] = num;
                    string_matrix += Integer.toString(num);
                    if(num  == 0){ // get row of the 0 (blank) value
                        blank_row = i;
                        blank_col = j; 
                    }
                    if(last_num>num && num != 0 && last_num != 0){ // check for inversion
                        num_inversions++; // add inversion in true case
                    }
                    last_num = num; // define last_num for next iteration
                }
            }
            
        }
        catch(Error err){
            throw new Error(err);
        }

        if(!testSolvability(blank_row + 1, num_inversions)){ // blank_row + 1 because to check is rows from 1 to 4
            throw new Error("Unsolvable board");
        }
        
        Board initial_board = new Board(initial_table, blank_row, blank_col, string_matrix);

        // System.out.println(checkIfSolution(initial_board));
        DepthFirstSearch(initial_board);
    }

}