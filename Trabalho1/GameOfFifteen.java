import java.util.HashMap;
import java.util.Scanner;

public class GameOfFifteen {
    
    public static void main(String[] args) {

        int[][] initial_table = new int[4][4]; //default definition of a game of 15(4x4)

        int num_inversions = 0;
        int last_num = -1;
        int blank_row=1;
        // Scanner reading initital sequence and setting initial_table
        try(Scanner scanner = new Scanner(System.in)){
            for(int i = 0; i<initial_table.length; i++){
                for(int j = 0; j<initial_table.length; j++){
                    int num = scanner.nextInt();
                    initial_table[i][j] = last_num;
                    if(num  == 0){
                        blank_row+= i;
                    }
                    if(last_num>num && num != 0 && last_num != 0){
                        num_inversions++;
                    }
                    last_num = num;
                }
            }
        }
        System.out.println(num_inversions);
        System.out.println(blank_row);
        System.out.println(testSolveability(blank_row, num_inversions));
    }

    static boolean testSolveability(int blank_row, int num_inversions){
        if(blank_row%2 != 0 && num_inversions%2!=0){
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

