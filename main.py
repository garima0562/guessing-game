secret_word = 'beautifull'
guess =""
guess_count = 0
guess_limit = 3
out_of_guesses = False
print('''welcome in this game!
here you need to guess the word
hint: some albhabet that used in word are "a,u,e,t"''')

while guess != secret_word and not(out_of_guesses):
  if guess_count < guess_limit:
    guess = input('enter a guess word:')
    guess_count += 1
  else:
    out_of_guesses = True
if out_of_guesses:
  print('out of guesses, you lose ! ')
else:
  print('you won!')