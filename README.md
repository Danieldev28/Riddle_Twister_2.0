         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!

" 9 Say my name and I dsiapear? What am I?" , " 10 I am always hungry, I must always be fed the finger I touch will soon turn red?" , "11 Forward im heavy but backword im not. What am I?" ,"12 I know a word of letters three, add two,and fewer there will be" 
# , "13 When young I am sweet in the sun.  When middle aged, I make you gay. When old I am valued more then ever." , " 14 When set loose I fly away Never so cursed, as when I go astray. What am I?" , "15 I drive men mad for love of me. Easliy beaten . Never free." ," 16 I reach for the sky but clutch to the ground, Sometimes I leave but I’m always around. What am I?" , "17 Always in you , sometimes on you. If I surround you I can kill you what am I?" , "18 What can point in everysingle direction but can reach the destination by itself?" 
# ,"19 When you give me to others you have to keep me What am I?", "Which letter of the alphabet has the most water?)

("What gets wetter as it dries?\n What do you get when you cross an automobile with a household animal?\nWhat has a ring, but no finger?\nThree lives have I gentle enough to sooth the skin,light enough to caress the sky, hard enough to crack rocks\nThe one who makes it sells it,the one who buys it never uses it, the one who uses it never knows they use it. What is it?\nThe more you have of it the less you see. What is it?\n I am lighter then what I am made of, more of me is hidden then seen? What am I?\nWhen you have me, you feel like sharing me. But, if you do share me, you don't have me. What am I\nSay my name and I dsiapear? What am I?\n I am always hungry, I must always be fed the finger I touch will soon turn red?\nForward im heavy but backword im not. What am I?\nI know a word of letters three, add two,and fewer there will be?\nWhen young I am sweet in the sun.  When middle aged, I make you gay. When old I am valued more then ever.\nWhen set loose I fly away Never so cursed, as when I go astray. What am I?\nI drive men mad for love of me. Easliy beaten . Never free.\nI reach for the sky but clutch to the ground, Sometimes I leave but I’m always around. What am I?\nAlways in you , sometimes on you. If I surround you I can kill you what am I?\n18 What can point in everysingle direction but can reach the destination by itself?\nWhen you give me to others you have to keep me What am I?\nWhich letter of the alphabet has the most water?")

https://a1cf5fddf9204e8c8bced47b6ad6c607.vfs.cloud9.us-east-1.amazonaws.com/get_riddle_api
"https://a1cf5fddf9204e8c8bced47b6ad6c607.vfs.cloud9.us-east-1.amazonaws.com/get_username_and_score_api?username=" + username +  "&score=" + score

<a name="top"></a>
# Daniel Smith Portfolio 

Welcome to my portfolio interactive front end development application! 
My name is Daniel, and through this project I am excited present to you roughly 
six weeks of app development in the making.

# Technologies

1.HTML
2.CSS
3.Bootstrap v4.3.2
4.Javascript
5.Fontawsome
6.Jquery library
7.Emailjs
8.Google Api
9.Merriam dictionary Api

# Features
This project has a very simple design with a navigation menu along the top
and subcategory menu, that reveals professionally once clicked by the user.I
am very proud of the fact that the html and css markup came together and was 
designed to be simple on the surface. But have depth when the user wants to 
engage and have more options for their match, thus improving user experience.
## Features Left To Implement

The features which I would like to implement, would be to add a short tutorial
at the beginning of the game. This would introduce the games speacial features
and allow smoother gameplay for a new user. Also a modal to display best score 
to the user in a modal box after restart of their current match. As well as 
coloring the random category button, vocabulary button, and god mode button 
differently to distinguish them as special categories to the player. Finally to 
place the app in the google playstore store with my logo <a href ="assets/images/wordbeatit-yellow.jpg">
here.<a> Intial testing of the game as an app was very successful
and the game displayed very well on the android device.

# UX

My goal with ux design was to make sure that my application was as user friendly 
and easy to navigate as possible. I strived to make a user interface that could 
be up and running with as little as 1-2 clicks. I belive that I have achieved this 
through default mode of the game, which starts with a five second timer
to input the correct word shown.

Through this project I strived to demonstrate the basics of user friendly 
interface by adding interaction where people expect it,ie. a modal popup 
that prompts the user to follow the steps prior to clickng start match for 
a more meaningful experience. As well as using colors that were appealing to the 
eyes, that kept the application sleek but at the same time provided 
a unique gameplay style and feel from other games in the same category. This in 
my opinion is what seperates my game from the competators; and makes it stand out
as a clear winner in the marketplace.

# Testing
Some of the trials I encountered while testing and updating, were ranging from
the very basic to difficult. I seemed have trouble in the beginning articulating
my ideas into actual code that I wanted to implement into the project(the logic). 
Through use of javascript logic and pseudocoding I was able to define a path for the 
game application and as a result, address the events that would happen during gameplay 
and when they would happen. This logic formed the basics of the algorithmn for the 
application. 
These events include:
#### Algorithmn

1.click start match else game starts
2. category selection onclick appears and rest appear inactive
3. countdown timer 3 seconds on start of game
4. add a stopwatch to start the match
5. from data set selected he should see a random word from that category selected.
6. game starts
7. from word selected show the word to user and start timer at the same time
8. when timer ends check text against correct answer stored
9. if win, clear users text bring another random word and display it to the user
10. Save the correct user inputs in an array and save the level in a variable
11. if lose, check the length of array that contains the right words-- if empty
display-- you didnt get the word correct try again
12. switch and case through each array category selection (iterate) EXCLUDING 
VOCABULARY fetch the meaning from my own dictionary of terms.
14. in case, of vocabulary get definition from api call
15. display at the bottom (table style) word and definition in a row and column
16. on.document load set value to 0 after that the scores should add up.If 
refreshing everything loads to a fresh page.
17.make a function for else contained in the function initiate -game
then call the function in the else statement

Sources:
https://www.codecademy.com/articles/glossary-html
https://www.w3schools.com/tags/
stackoverflow.com
jsfiddle.com
(github repository) https://bousbissikouceila.github.io/speedTypingGame/


# Deployment

This cite is hosted from Github directly from the master branch.
You may access the file through,

https://danieldev28.github.io/Wordbeatit_Typing_Game/

During my class and while working in a small group we were able to bring
testers in to test the game. They  provided valuable feedback, in order upgrade 
the games capabilities in order to match real world demands of a player. I 
enjoyed this process because I could see how a person would interact, when,
and why they did certain things live in person. I even tried breaking the game
after this to ensure that all the bugs from the previous verson were 
fixed and that my logic was not flawed.

# Credits 
I would like to credit numerous cites for inspiration in ux design as I could 
not have done this with inspiration and at times a little persperation. Cites 
used for application inspiration <a href="https://www.typing.com/">here.</a> 
I would also like to credit the stackoverflow community for any methods and 
code snippets used, it was a really awesome resource to roll up my sleeves and 
learn on the website.

# Media 

Any media you see inside this web application was created by yours truly
a.k.a me. Fonts were borrowed and inspired by <a href ="https://zeraxas.github.io/Word-Beater/">
here.</a> Many challenges were faced during the creation of this application 
but I learned that there is almost always a solotion for everything or a 
workaround. I overcame many of them through the help of my mentor Abhay Barthwal. 
My countdown timer uses digtal-7 webfont kit to give it a very nice digital 
display from <a href ="https://www.dafont.com/digital-7.font">here.</a>

## Acknowledgements

I would like to acknowledge the use of bootstrap components. As well as 
w3schools.com for when I got stuck. I also searched stackoverflow.com countless
times for more information to solve problems with my application when I was stuck 
on the harder portions. I am thankful that my project is finally exactly as I  
had envsioned, if not better.  Thank you for viewing this presentation of my HTML,
CSS, Bootstrap, and javascript practical application to a real project I enjoyed 
making it and sharing it and hope to present more to you in the future.Until then 
that wraps up my skills as as a brand new front-end web developer.
                                                <a href="#top">Back to top</a>
### This is for educational use.
