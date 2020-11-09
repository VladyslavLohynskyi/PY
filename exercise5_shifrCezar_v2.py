import alphabet

encrypt = input("Enter your massage: ")
key=3
encrypted=""
for letter in encrypt:
        if letter in alphabet.latin:
                position= alphabet.latin.find(letter)
                newposition= position+key
                if letter in alphabet.latin:
                        encrypted = encrypted + alphabet.latin[newposition]
                else:
                        continue
        elif letter in alphabet.kyrylica:
                position = alphabet.kyrylica.find(letter)
                newposition = position + key
                if letter in alphabet.kyrylica:
                        encrypted = encrypted + alphabet.kyrylica[newposition]
                else:
                     continue

        elif letter in alphabet.numbers:
                position = alphabet.numbers.find(letter)
                newposition = position + key
                if letter in alphabet.numbers:
                        encrypted = encrypted + alphabet.numbers[newposition]
                else:
                        continue
        else:
                encrypted = encrypted + letter



print("Encrypted massage is: "+ encrypted)

