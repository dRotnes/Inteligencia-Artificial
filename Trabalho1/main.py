from board import Board
from shared import FINAL_TABLE, BLANK_ROW_FINAL, NUM_INVERSIONS_FINAL
from depthFirstSearch import DFS
from iterativeDepthFirstSearch import IDFS
from breadthFirstSearch import BFS
from aStar import A_star
from greedy import greedy
import time

def testSolvability(blank_row, num_inversions):
    return (num_inversions%2 == 0) == (blank_row%2 == 1)
    
# MAIN()
tables = []
initial_table = []
blank_row = 0
blank_col = 0

with open("config.txt") as fileIn:
    for line in fileIn:
        tables.append(list(map(int, line.split())))

while tables[0] != []:
    initial_table.append(tables[0][:4])
    tables[0] = tables[0][4:]

while tables[1] != []:
    FINAL_TABLE.append(tables[1][:4])
    tables[1] = tables[1][4:]

num_inversions = 0
last_num = -1
for i in range(len(initial_table)):
    for j in range(len(initial_table)):
        if(last_num>initial_table[i][j] and initial_table[i][j]!=0 and last_num!=0):
            num_inversions+=1
        if(initial_table[i][j] == 0):
            blank_row = i
            blank_col = j
        last_num = initial_table[i][j]

last_num = -1
for i in range(len(FINAL_TABLE)):
    for j in range(len(FINAL_TABLE)):
        if(last_num>FINAL_TABLE[i][j] and FINAL_TABLE[i][j]!=0 and last_num!=0):
            NUM_INVERSIONS_FINAL+=1
        if(FINAL_TABLE[i][j] == 0):
            BLANK_ROW_FINAL = i
        last_num = FINAL_TABLE[i][j]

if(testSolvability(4 - blank_row,num_inversions) == (testSolvability(4 - BLANK_ROW_FINAL , NUM_INVERSIONS_FINAL))):

    initial_board = Board(initial_table, blank_row, blank_col)

    algorithm_to_run = int(input("Please input which algorithm you want to run:\n0: DFS\n1: IDFS\n2: BFS\n3: A*\n4: GREEDY\n"))

    total_time = 0
    total_memory = 0

    match algorithm_to_run:
        case 0:
            print("---------- STARTING DFS ----------\n")
            start = time.time()
            dfs, num_nods_gen = DFS(initial_board)
            end = time.time()
            total_time = end - start
            if(dfs is not None):
                total_memory = num_nods_gen
                for i in dfs:
                    print(str(i) + " =>" )
            print("---------- END OF DFS ----------\n")
        case 1:
            print("---------- STARTING IDFS ----------\n")
            start = time.time()
            idfs, num_nods_gen = IDFS(initial_board)
            end = time.time()
            total_memory = num_nods_gen
            total_time = end - start
            for i in idfs:
                print(str(i) + " =>" )
            print("\n---------- END OF IDFS ----------\n")
        case 2:
            print("---------- STARTING BFS ----------\n")
            start = time.time()
            bfs, depthBfs, pathBfs, num_nodes_gen = BFS(initial_board)
            end = time.time()
            total_memory = num_nodes_gen
            total_time = end - start
            if(bfs):
                for i in pathBfs:
                    print(str(i) + " =>" )
                print("\n---------- SOLUTION FOUND ON DEPTH "+str(depthBfs)+" ----------")
            else:
                print("BFS DID NOT FIND ANY SOLUTION") 
            print("\n---------- END OF BFS ----------\n")  
        case 3:
            heu = int(input("\nWhich heuristic you want?\n0: Manhattan heuristic\n1: Sum of wrong places heuristic\n"))
            if(heu == 0):
                print("---------- STARTING A* MANHATTAN HEURISTIC ----------\n")
                start = time.time()
                astar_Man, depth_Astar_Man, num_nodes_gen = A_star(initial_board, "MAN")
                end = time.time()
                total_memory = num_nodes_gen
                total_time = end - start
                if(astar_Man is not None):
                    print("---------- SOLUTION FOUND ON DEPTH "+str(depth_Astar_Man)+" ----------")
                    for i in astar_Man:
                        print(str(i) + " =>" )
                else:
                    print("---------- NO SOLUTION FOUND ----------\n")
                print("\n---------- END A* MANHATTAN HEURISTIC ----------\n")
            else:
                print("---------- STARTING A* SUM WRONG PLACES HEURISTIC ----------\n")
                start = time.time()
                astar_Sum , depth_Astar_Sum, num_nodes_gen= A_star(initial_board, "SUM")
                end = time.time()
                total_memory = num_nodes_gen
                total_time = end - start
                if(astar_Sum is not None):
                    print("---------- SOLUTION FOUND ON DEPTH "+str(depth_Astar_Sum)+" ----------")
                    for i in astar_Sum:
                        print(str(i) + " =>" )
                else:
                    print("---------- NO SOLUTION FOUND ----------\n")
                print("\n---------- END A* SUM WRONG PLACES HEURISTIC ----------\n")
        case 4:
            heu = int(input("\nWhich heuristic you want?\n0: Manhattan heuristic\n1: Sum of wrong places heuristic\n"))
            if(heu == 0):
                print("---------- STARTING GREEDY MANHATTAN HEURISTIC ----------\n")
                start = time.time()
                greedy_Man , depth_greedy_Man, num_nodes_gen = greedy(initial_board, "MAN")
                end = time.time()
                total_memory = num_nodes_gen
                total_time = end - start
                if(greedy_Man is not None):
                    print("---------- SOLUTION FOUND ON DEPTH "+str(depth_greedy_Man)+" ----------")
                    for i in greedy_Man:
                        print(str(i) + " =>" )
                else:
                    print("---------- NO SOLUTION FOUND ----------\n")
                print("\n---------- END GREEDY MANHATTAN HEURISTIC ----------\n")
            else:
                print("---------- STARTING GREEDY SUM WRONG PLACES HEURISTIC ----------\n")
                start = time.time()
                greedy_Sum , depth_greedy_Sum, num_nodes_gen = greedy(initial_board, "SUM")
                end = time.time()
                total_memory = num_nodes_gen
                total_time = end - start
                if(greedy_Sum is not None):
                    print("---------- SOLUTION FOUND ON DEPTH "+str(depth_greedy_Sum)+" ----------")
                    for i in greedy_Sum:
                        print(str(i) + " =>" )
                else:
                    print("---------- NO SOLUTION FOUND ----------\n")
                print("\n---------- END GREEDY SUM WRONG PLACES HEURISTIC ----------\n")
        case _:
            print("NO ALGORITHM WAS CHOSEN, EXITING")
            exit()         
    print("TOTAL TIME SPENT: " + str(total_time))
    print("TOTAL MEMORY SPENT: " + str(total_memory))
else:
    raise Exception("UNSOLVABLE BOARD: the initial configuration can't take you to the final configuration")


