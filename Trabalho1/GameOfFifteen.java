import java.util.HashMap;
import java.util.Scanner;

public class GameOfFifteen {
    
    public static void main(String[] args) {

        int[][] initial_table = new int[4][4]; //default definition of a game of 15(4x4)

        int num_inversions = 0; //counter for the number of inversions
        int last_num = -1; // initialize last_num as -1 so that its always lower than the initial number of the matrix
        int blank_row= 1; // initialize blank_row as 1 so that the verification goes from 1 to 4 (2 odds and 2 even row numbers)

        // Scanner reading initital sequence and setting initial_table
        try(Scanner scanner = new Scanner(System.in)){
            for(int i = 0; i<initial_table.length; i++){
                for(int j = 0; j<initial_table.length; j++){
                    int num = scanner.nextInt();
                    initial_table[i][j] = last_num;
                    if(num  == 0){ // get row of the 0 (blank) value
                        blank_row+= i; 
                    }
                    if(last_num>num && num != 0 && last_num != 0){ // check for inversion
                        num_inversions++; // add inversion in true case
                    }
                    last_num = num; //define last_num for next iteration
                }
            }
        }
        catch(Error err){
            throw new Error(err);
        }

        // small tests
        // System.out.println(num_inversions);
        // System.out.println(blank_row);
        // System.out.println(testSolvability(blank_row, num_inversions));
        // end small tests
    }

    //test sovability of initial board
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

}

