
import numpy as np

class SlotMachine:
    def __init__(self):
        self.credit = 1000  # Total funds
        self.cash = 20  # Cost of one game
        self.total_won = 1000  # Initialize total_won
        self.emoji = ['7️⃣', '🍒', '🍏', '🔔']  # Slot symbols
        
    def check_credit(self):
        """Check if the user has enough credit to play."""
        if self.credit < self.cash:
            return False, "You don't have enough credit to play."
        return True, ""
    
    def play_game(self):
        """Main function to play the slot machine game."""
        is_playable, message = self.check_credit()
        if not is_playable:
            return message
        
        self.credit -= self.cash  # Deduct cost of the game
        self.total_won = self.credit  # Update total won
        lines = np.random.randint(0, 4, (3, 3))  # Generate random numbers for the slot machine
        output = ""
        
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                output += self.emoji[lines[i][j]] + " "
            output += '\n'
        
        for row in lines:
            if len(set(row)) == 1:
                self.credit += self.get_reward(row[0])
        
        for col in range(3):
            if len(set(lines[:, col])) == 1:
                self.credit += self.get_reward(lines[0, col])
        
        if len(set(np.diag(lines))) == 1:
            self.credit += self.get_reward(lines[0, 0])
        if len(set(np.diag(np.fliplr(lines)))) == 1:
            self.credit += self.get_reward(lines[0, 2])
        
        return output

    def get_reward(self, symbol_index):
        """Calculate reward based on the symbol."""
        reward_multipliers = [5, 3, 1.5, 1]  # Corresponding to '7️⃣', '🍒', '🍏', '🔔'
        return self.cash * reward_multipliers[symbol_index]
