Flash Card Game using Tkinter

![image](https://user-images.githubusercontent.com/80412098/124786866-f0529180-defc-11eb-9e4c-91bf8037a185.png)


![image](https://user-images.githubusercontent.com/80412098/124786894-f47eaf00-defc-11eb-9c68-53f4a0d908c5.png)

UI Setup 

- First thing I did is to setup the User Interface of my flash card. I basically used a 2 x 2 grid (split the columns in two). Then I added the necessary widgets on the front side of the card such as the check and cross (wrong) buttons.

Generate the translation words

- Function that flips the card and displays the English translation word
I used PANDAS to read the csv file where I stored the different French and English translation words. Then, I created a function to generate random words from the csv file using the random function. The random French word that is being returned from the generate_random_word() function will be displayed on the screen. User have 3 seconds to guess what the English translation word is before the card is flipped to the back side. In order to achieve this 3 seconds delay, I used Tkinter’s “window.after()” function. If the user knows the correct English translation, the user must click the check button within 3 seconds before it flips to the back showing the correct answer. If the user does not know the correct translation, then the user must click the ‘X’ button or basically just wait until the card flips.

Correct Translation
-When the user knows the correct English translation word and clicks on the check button, the clicked_check() function will be called because this particular function is passed as an argument in the check button’s command. When the clicked_check() function is called, the current random word (both French and English) will be removed from the original_data csv file. Then the updated csv data will be saved to a new csv file called words_to_learn.csv. So that the next time the program is run, it should check if words_to_learn.csv file exists. If it exists, the program should use those words to be displayed on the flashcards. If the words_to_learn.csv does not exist (i.e., the first time the program is run), then it should use the words in the french_words.csv (original_data).
