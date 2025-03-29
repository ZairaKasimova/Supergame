# Суперигра

+ **supergame.py** - игра, созданная по мотивам телеигры "Поле Чудес", в основе игры лежит механика открытия символов: пользователь должен угадывать слова или словосочетания, являющиеся ответами на задания над табло, по одному символу (необязательно вводить символы по порядку). При запуске данной программы как основной (не как библиотеки) запускается игра с 4 заданиями о графиках функций. При введении символа, который есть в слове и который раньше не вводился, на табло выводится данный символ во всех местах, в которых он есть в слове. В ходе игры пользователю выводятся сообщения о введении правильного ответа, о введении неправильного ответа, о том, что ответ должен состоять из одного символа, если введено несколько, об угадывании слова (если нужно было угадать одно слово), об угадывании словосочетания (если нужно было угадать словосочетание), о проигрыше, о победе. Некоторые сообщения содержат обращение к пользователю по имени, которое он ввёл до вывода заданий и табло (до нажатия на кнопку "Начать игру"), если он ничего не ввёл, то в сообщениях будет использоваться слово "Инкогнито" при обращении к пользователю. Если участник ошибётся (введёт символ неправильно) 5 раз в одном слове, то он проигрывает, появляются сообщение о проигрыше и на экране кнопка "Играть ещё раз",  при нажатии на которую игра начинается заново, если участник назовёт правильно все слова, то выигрывает. Чтобы запустить данную программу, нужно установить библиотеки tkinter и pillow, а также поместить изображение с названием supergame.gif из данного репозитория в папку с данной программой, оставляя название изображения прежним (supergame.gif). Данная программа может также использоваться как библиотека для быстрого создания игры с другими заданиями и словами (возможно, с другим количеством заданий и слов).
+ **supergame.gif** - изображение на фоне игры.
+ **new_game.py** - пример использования программы supergame.py как библиотеки. Чтобы запустить данный пример, нужно, чтобы он находился в той же папке, что и программа supergame.py с изображением supergame.gif (названия у программы и изображения в папке должны быть такими же, как и в данном репозитории (supergame.py и supergame.gif соответственно)).

 
# Supergame

+ **supergame.py** - a game based on the TV game "Pole Chudes", the game is based on the mechanics of opening symbols: the user must guess words or phrases that are answers to tasks above the board, one symbol at a time (it is not necessary to enter the symbols in order). When you run this program as the main one (not as a library), a game starts with 4 tasks about function graphs. When you enter a character that is in a word and that has not been entered before, this symbol is displayed on the scoreboard in all the places where it is in the word. During the game, messages are displayed to the user about entering the correct answer, about entering the wrong answer, that the answer should consist of one character if several are entered, about guessing a word (if it was necessary to guess one word), about guessing a phrase (if it was necessary to guess a phrase), about losing, about winning. Some messages contain an address to the user by the name that he entered before the tasks and the scoreboard were displayed (before clicking on the "Начать игру"("Start game") button), if he did not enter anything, the word "Инкогнито"("Incognito") will be used in the messages when addressing the user. If the participant makes a mistake (enters a character incorrectly) 5 times in one word, he loses, a loss message appears and the "Играть ещё раз"("Play again") button appears on the screen, when clicked, the game starts over, if the participant names all the words correctly, he wins. To run this program, you need to install the tkinter and pillow libraries, as well as place an image with the name supergame.gif from this repository to the folder with this program, leaving the name of the image the same (supergame.gif). This program can also be used as a library for quickly creating a game with other tasks and words (possibly with a different number of tasks and words).
+ **supergame.gif** - the image on the background of the game.
+ **new_game.py** - an example of using the program supergame.py as a library. To run this example, you need it to be in the same folder as the program supergame.py with the image supergame.gif (the names of the program and the image in the folder must be the same as in this repository (supergame.py and supergame.gif, respectively)).
