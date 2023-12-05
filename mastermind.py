import random


class Mastermind:

    def __init__(self, number,position):
        self.number = number
        self.position = position
        self.secret_code = []

        self.game_over = False
        self.round = 0
        self.generate_secret_code()


    def generate_secret_code(self):
        self.secret_code = []
        number_of_position = self.position  # จำนวนของตัวเลข (ตำแหน่ง) ที่ user เลือกเล่น
        for i in range(number_of_position):
            random_number = random.randint(1, self.number)  # สุ่มตั้งแต่เลข 1 ไปจนถึง เลขที่userเลือก
            self.secret_code.append(random_number)  # เอาเลขที่สุ่มมาได้ จับเข้า list

    def users_guess(self):  # ให้คนเล่นลองเดาตัวเลข
        while True:
            guess = input(f"Enter your guess ({self.position} digits) or x to quit: ")
            if guess == 'x': # สร้างเงื่อนไขดักไว้ก่อนเพราะปกติจะให้คนเล่นใส่ int
                self.dump_game()
            elif len(guess) == self.position:
                converted_guess = [] # คอยupdate user เพราะ hint ต้องคอยอัพเดตกับ user guess ทุกครั้ง
                for i in guess:
                    converted_guess.append(int(i)) #ต้องเปน int เพราะว่า random มันให้ค่าออกมาเปนตัวเลข

                return converted_guess #ส่งค่าที่เรา update ออกไป

    def hint(self,guess):  # มีคำใบ้ให้คนเล่น , มี parameter guess มารอรับ convert_gues อยู่เพื่อเอามาใช้ต่อใน def hint
        correct_position = 0
        correct_number = 0
        tempo_code = self.secret_code.copy()
        tempo_guess = guess[:] # [:] เป็นการ copy โดยใช้ slicing
        print(tempo_code)
        print(tempo_guess)
        # checking correct number (ถูกเลข ไม่ถูกตำแหน่ง)
        for i in range(self.position):
            if tempo_guess[i] == tempo_code:
                correct_number += 1


        # checking correct position (ถูกตำแหน่ง ไม่ถูกเลข)
            elif tempo_guess[i] in self.secret_code:
                correct_position += 1

        return '*' * correct_position + 'o' * correct_number

    def dump_game(self):  # สำหรับคนเล่นที่กดยอมแพ้
        if not self.game_over:
            print(self.secret_code)
            print(self.round)
            exit() #ยอมแพ้แล้วให้โปรแกรมหยุดเลย

    def playing(self):

        while not self.game_over:
            guess = self.users_guess() # ต้องมี var มารับเพราะว่า def user_guess return ค่าออกมา
            if guess == 'x':
                self.dump_game()
            hint = self.hint(guess) # ต้องมี argument เพราะว่า def hint มี parameter
            self.round += 1
            self.generate_secret_code()
            print(f'Hint {hint}')


playing_game = Mastermind(6,4)
guess = playing_game.users_guess()
# playing_game.playing()
# playing_game.dump_game()
playing_game.hint(guess)
