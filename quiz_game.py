print('Welcome to my computer parts quiz! 🖥️')

playing = input('Do you want to play (Yes/No)?: ')

if playing.lower() == 'yes':
    print("Okay! Let's play 👀")
else:
    print('Bye! 😢')
    quit()

score = 0

answer = input('What does CPU stand for?: ')
if answer.lower() == 'central processing unit':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does GPU stand for?: ')
if answer.lower() == 'graphics processing unit':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does RAM stand for?: ')
if answer.lower() == 'random access memory':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does PSU stand for?: ')
if answer.lower() == 'power supply unit':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does HDD stand for?: ')
if answer.lower() == 'hard disk drive':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does SSD stand for?: ')
if answer.lower() == 'solid state drive':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does AIO stand for?: ')
if answer.lower() == 'all in one':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does VRAM stand for?: ')
if answer.lower() == 'video random access memory':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does BIOS stand for?: ')
if answer.lower() == 'basic input output system':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does VR stand for?: ')
if answer.lower() == 'virtual reality':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does RGB stand for?: ')
if answer.lower() == 'red green blue':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does HDMI stand for?: ')
if answer.lower() == 'high definition multimedia interface':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

answer = input('What does USB stand for?: ')
if answer.lower() == 'universal serial bus':
    print('Correct! 🎉')
    score += 1
else:
    print('Incorrect! 😢')

print('You got ' + str(score) + ' questions correct! 🎉')
print('You got ' + str((score / 5) * 100) + '%.')
