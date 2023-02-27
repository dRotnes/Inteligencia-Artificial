import java.util.Arrays;
import java.util.Scanner;
import java.util.Stack;

public class GameOfFifteen {

    public static void main(String[] args) {

        int[][] initial_table = new int[4][4]; // default definition of a game of 15(4x4)
        

        int num_inversions = 0; // counter for the number of inversions
        int last_num = -1; // initialize last_num as -1 so that its always lower than the initial number of the matrix
        int blank_row = 0; // initialize blank_row as 0
        int blank_col = 0; // inititalize blank_col as 0

        // Scanner reading initital sequence and setting initial_table
        try(Scanner scanner = new Scanner(System.in)){
            for(int i = 0; i<initial_table.length; i++){
                for(int j = 0; j<initial_table.length; j++){
                    int num = scanner.nextInt();
                    initial_table[i][j] = num;
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

        if(checkIfSolution(initial_table)){
            System.out.println("Initial value is already solution");
            return;
        }

        Board initial_Board = new Board(initial_table, blank_row, blank_col);

        Stack<Board> next_moves = calculateNextPossibilites(initial_Board);
        
        while(!next_moves.isEmpty()){
            Board b = next_moves.pop();
            System.out.print("-----------\n");
            for(int j = 0; j<b.getTable().length;j++){
                for(int l = 0; l<b.getTable().length;l++){
                    System.out.print(b.getTable()[j][l] + " ");
                }
                System.out.print('\n');
            }
        }

    }

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

    static boolean checkIfSolution(int[][] board){
        int last_num = -1;
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board.length; j++){
                if(last_num > board[i][j]){
                    return false;
                }
                last_num = board[i][j];
            }
        }
        return true;
    }

    static Stack<Board> calculateNextPossibilites(Board board){
        
        Stack<Board> stack = new Stack<Board>(); // stack to be used on depth searches
        
        int blank_col = board.getBlankCol();
        int blank_row = board.getBlankRow();

        if(blank_col + 1 <= 3){ //if it can be moved right
            int[][] new_table = new int[4][4];
        
            for(int i = 0; i < board.getTable().length; i++){
                for(int j = 0; j < board.getTable().length; j++){
                    new_table[i][j] = board.getTable()[i][j];
                }
            }

            int moveRight = new_table[blank_row][blank_col + 1];
            new_table[blank_row][blank_col + 1] = 0;
            new_table[blank_row][blank_col] = moveRight;
            stack.add(new Board(new_table, blank_row, blank_col + 1));
        }
        if(blank_col - 1 >=0){ //if it can be moved left
            int[][] new_table = new int[4][4];
        
            for(int i = 0; i < board.getTable().length; i++){
                for(int j = 0; j < board.getTable().length; j++){
                    new_table[i][j] = board.getTable()[i][j];
                }
            }

            int moveLeft = new_table[blank_row][blank_col - 1];
            new_table[blank_row][blank_col - 1] = 0;
            new_table[blank_row][blank_col] = moveLeft;
            stack.add(new Board(new_table, blank_row, blank_col - 1));
        }
        if(blank_row + 1 <=3){ //if it can be moved up
            int[][] new_table = new int[4][4];
        
            for(int i = 0; i < board.getTable().length; i++){
                for(int j = 0; j < board.getTable().length; j++){
                    new_table[i][j] = board.getTable()[i][j];
                }
            }

            int moveUp = new_table[blank_row + 1][blank_col];
            new_table[blank_row + 1][blank_col] = 0;
            new_table[blank_row][blank_col] = moveUp;
            stack.add(new Board(new_table, blank_row + 1, blank_col));
            
        }
        if(blank_row - 1 >=0){ //if it can be moved down
            
            int[][] new_table = new int[4][4];
        
            for(int i = 0; i < board.getTable().length; i++){
                for(int j = 0; j < board.getTable().length; j++){
                    new_table[i][j] = board.getTable()[i][j];
                }
            }
            int moveDown = new_table[blank_row - 1][blank_col];
            new_table[blank_row - 1][blank_col] = 0;
            new_table[blank_row][blank_col] = moveDown;
            stack.add(new Board(new_table, blank_row - 1, blank_col));
        }

        return stack;
    }

}

