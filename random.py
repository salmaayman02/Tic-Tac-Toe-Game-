


##tic tac toe game
import random
class tic_tac_toe:
    
    grid = [["","",""],
            ["","",""],
            ["","",""]]
    
    def is_full(self):
        full = True
        for i in self.grid:
            for j in i:
                if j == "":
                    full = False
        return full

    def print_grid(self):
        for i in self.grid:
            print(i)

    def chooce_position(self):
        self.print_grid() 
        i = int(input("Choose row between 1 and 3: "))
        j = int(input("Choose column between 1 and 3: "))
        if(i > 3 or i < 1 or j > 3 or j < 0):
            return self.chooce_position()

        else:
            return j,i

    def add_X(self):
        j,i = self.chooce_position()
        
        if  self.grid[i-1][j-1] == "":
            self.grid[i-1][j-1] = "X"
        else:
            print("pstion is not empty")
            self.add_x()
            


    def add_O(self):
        j,i = self.chooce_position()
        if  self.grid[i-1][j-1] == "":
            self.grid[i-1][j-1] = "O"
        else:
            print("pstion is not empty")
            self.add_O()

    def add_random(self):
        i =random.randint(1, 3)
        j =random.randint(1, 3)
        if  self.grid[i-1][j-1] == "":
            self.grid[i-1][j-1] = "O"
        else:
            print("pstion is not empty")
            self.add_random()

    def check_row(self):
        for row in self.grid:
            if len(row) == 3:
                if len(set(row)) == 1 :
                    winner = row[0]      
                    return winner  

    def check_column(self):
        for col in range(3):
            column = [row[col] for row in self.grid]
            if len(column) == 3:
                if len(set(column)) == 1 :
                    winner = column[0]     
                    return winner  
            
    def check_digonal(self):
        digonal1 = [self.grid[i][i] for i in range(3)]
        digonal2 = [self.grid[0][2],self.grid[2][0],self.grid[1][1]]
        if len(digonal1) == 3:
            if len(set(digonal1)) == 1 :
                winner = digonal1[0]     
                return winner 

        if len(digonal2) == 3:
            if len(set(digonal2)) == 1 :
                winner = digonal2[0]     
                return winner 

    def winner(self):

        if self.check_row():
            winner = self.check_row()
            return winner
        elif self.check_column():
            winner = self.check_column()
            return winner
        elif self.check_digonal():
            winner = self.check_digonal()
            return winner
        else:
            return None




game = tic_tac_toe()
win =False

print("chooce players number:")
c = int(input("1 Player\t2 Players: "))
    


if c == 2:
    while True:
        if game.winner():
            winner = game.winner()
            win = True
            break
        full = game.is_full()
        if full == True:
            break
        else:
            print("X player turn")
            game.add_X()
            if game.winner():
                winner = game.winner()
                win = True
                break
            full = game.is_full()
            if game.is_full():
                break
            print("O player turn")
            game.add_O()
        
    



if c == 1:
    while True:
        if game.winner():
            winner = game.winner()
            win = True
            break
        full = game.is_full()
        if full == True:
            break
        else:
            print("X player turn")
            game.add_X()
            if game.winner():
                winner = game.winner()
                win = True
                break
            full = game.is_full()
            if game.is_full():
                break
            print("O player turn")
            game.add_random()
    




if c > 2 or c < 1:    
    print("wrong input game exit")




game.print_grid()
if win == True:
    print("The winner is",winner, "player")
else:
    print("No Winner")    







