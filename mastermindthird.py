class MM:

    def __init__(self,number,pos):
        self.number = number
        self.position = pos
        self.end_game = False
        self.guess = []
        self.secret_code = []
        self.round = 0


    def generate_secret_code(self):
        import random

        self.secret_code = []
        for i in range(self.position):
            code = random.randint(1,self.number)
            self.secret_code.append(code)
            # print(code)
        # print(self.secret_code)


    def user_guess(self):
        while True:

            guess = input(f"Enter your guess ({self.position} digits) or q to quit: ")

            if guess == 'q':
                print(self.secret_code)
                print(self.round)
                exit()
            elif len(guess) == self.position:
                self.guess = []
                for i in guess:
                    self.guess.append(int(i))
                self.round +=1
                return self.guess
                # print(self.guess)


    # def hint(self):
    #     correct_pos = 0
    #     correct_num = 0
    #     secret_codes = self.secret_code.copy()
    #     guess = self.guess[:]
    #
    #     print(secret_codes)
    #     print(guess)
    #     #checking correct position
    #     for i in range(self.position):
    #         # print(j)
    #         if guess in secret_codes:
    #             correct_pos += 1
    #             print('o')
    #
    #     #checking correct number
    #
    #     for j in range(self.position):
    #         # print(j)
    #         if guess == secret_codes:
    #             correct_num += 1
    #             print('*')
    #
    #     # print(correct_num)
    #     # print(correct_pos)
    #
    #     # return '*'*correct_pos + 'o'*correct_num

    def hint(self, guess):
        correct_pos = 0
        correct_num = 0
        self.generate_secret_code()
        secret_codes = self.secret_code.copy()
        guessing = guess[:]

        # Checking correct position
        for i in range(self.position):
            if guessing[i] == secret_codes[i]:
                correct_pos += 1
                # print('o')
                # Remove the correctly guessed digit to avoid counting it again
                secret_codes[i] = None

        # Checking correct number
        for j in range(self.position):
            if guessing[j] in secret_codes and guessing[j] != secret_codes[j]:
                correct_num += 1
                # print('*')
                # Remove the correctly guessed digit to avoid counting it again
                secret_codes.remove(guessing[j])

        return '*' * correct_pos + 'o' * correct_num

    def user_end_game(self):
        if not self.end_game:
            print(self.guess)
            print(self.round)

            exit()

    def playing(self):
        # self.generate_secret_code()
        # guess = self.user_guess()
        # self.hint(guess)
        self.generate_secret_code()

        while True:
            guess = self.user_guess()
            hint = self.hint(guess)

            print(f"Your guess is {''.join(map(str, guess))}")
            print(f"hint: {hint}")

            if hint == '*' * self.position:
                print(f"You solved it after {self.round} rounds")
                break





play = MM(6,4)
# play.generate_secret_code()
# guess = play.user_guess()
# play.hint(guess)
play.playing()