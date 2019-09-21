# DystopiaSim
A Dystopian Text Based Management Game

Keep up with us here: [Our Website](https://wredbeard.wixsite.com/website/blog)

Please read everything below before doing anything else!

## What's It About
Players are introduced into a dystopian world where they are a low-level politician. Through tactics and interaction with other characters in the game they gain power and rank in the political system. Players first seek to put their party into controlling power of the government and then later position themselves as a supreme ruler. All of this happens in a world where assassination attempts, bribery, and political crimes occur daily.

This is designed to be a turn-based menu driven console game.

## Why I Am Writing This Game
I created this game to help me learn more about Python programming. I am pretty new to it so I can assure you than any seasoned programmer will get nauseous looking at my code. I was incredibly inspired by the game Warsim: The Realm of Aslona and that encouraged me to get back into programming. I have an interest in Dystopian worlds. It all just came together.

I chose Python for the game because I haven't quite wrapped my head around a language like C++. I've barely gotten Python!

The game does broach some sensitive topics like murder, suicide, etc. It is not written for children or the faint of heart.It is a dystopian game and bad things go on in dystopias.

## Current Features
So far I have implemented the following features into the game:

- Menu System - The menu system utilizes the console-menu library for keeping things neat and orderly. Due to the limitations of console-menu some dialogues have to be done outside of the console-menu
- Event Engine - I created a basic event engine that has descriptions and uses variables stored in the events.json file to modify values in the config.json(stores player/game data) file.
- Basic Saving - Saving is currently accomplished by writing the modified variables into the config.json file. While this is nice, it only allows the player to make one save at a time.
- Banking System - There is a banking system for players to use that allows them to deposit money and gain interest as well as take out loans. The loans and bank accounts accrue interest on a turn-by-turn basis.
- Persistent Status Bar - This status bar contains information about the player and their party. Things like money, power, etc. This, of course, has to work within the limitations of console-menu which has caused issues.

## Current Problems
There are many problems with the game in it's current state. It is playable up to some point but it is under construction. If you're doing some hunting just to find an open source game to play, this may not be the right place if you do not have experience with Python. If you do. Do not feel shy about opening up an issue.

Current problems include:
- Incomplete Game - The game is not a complete game that needs features added to it. It is an incomplete game with incomplete features.
- Saving System - The saving system is pretty rough. I am currently using JSON files for the game saves. All player related variables are stored in this file. If there's a better way to do it, I want to know.
- Menu System - some menus are not complete and will exit the game or have a placeholder. console-menu has broken some of the visuals of the game. That's okay for now because there's not much going on but these issues will need to be fixed. I would ideally like to write a better GUI but I don't want to lose sight of the actual game for now.
-Other Problems I Haven't Thought Of-

## Future Plans
My main goal here is to provide something fun to play and give the players a sense of power with lots of unique events to take advantage of.

Here are the things I would like to do as far as the actual coding of the game is concerned:

- Better Organization - Functions need to be seperated into different files based on the things they do and reduce the use of imports.
- Implement Better Coding Practices - This is number one. I am painfully aware that there are much better ways to accomplish the things I need the program to do. However, I am limited in my knowledge and have implemented features to the best of my abilities. It is my hope that by introducing the code to this game to the community we might find better ways to do things and make the game more efficient and fun for players. I want this game to be a community project built around user input.
- Platform Independent - I want the game to be playable by the public at large. I've done everything I can so far to make the game as platform independent as possible. I've utilized libraries that do not explicitly rely on platform dependent packages. In addition to this, if there is some way to make the game one-click install I would like to do so.
- User Built - If enough of the community agrees on a gameplay feature, I want to implement it. The story and gameplay should please the people who will ultimately be playing the game.
- Better Notation And Commenting - I will personally be working on this. Most of the functions are now explained!

## Future Features
With the goal of making this game as extensible and flexible as possible, I would like to continue to implement new gameplay features over time. Of course, getting the basics down is the first goal. Everything should be in a dystopian style.

- Laws - Implementation of laws and their effects on the game. I haven't implemented this feature yet. The laws can range from silly to detrimental. For instance, a law could place limitations on the time people can be out. However, this may have an effect on tax income.
- Map Exploration - Players should be able to navigate around the game world and interact with NPCs, discover things, visit ministries, go to the bar, etc.
- Economy - There should be at least a basic modifiable economy that can be affected by events in the game. It doesn't need to be overly complex.
- Government - I haven't built the government system out. It should include things such a it's own money, record of laws, involved characters, etc. In essence, the game should transition from player-centric to government-centric.
- Rival - Players should have a rival party that they have to take out of power. This is partially implemented.
- Political System - There should be a political system that players can move up in. It should track laws, seats in the congress, relationships to other members, chances on votes passing, and so on.
- Affinity System - There should be an affinity system between players and important characters in the game. Being good friends with a member of the opposing party may get the player some much needed dirt.

This list will be added and reduced as we further develop the game.

## Packages Needed To Run
-colorama - soon to be removed
-We highly recommend using python 3.7 to run the game

## A Warning
This game is in pre-pre-alpha. It is not designed to be playable yet as it is not complete. However, a lot of the framework has been coded and needs to be made more efficient. It is hot garbage right now. But that will change.

If you are viewing the code leave me some feedback or by all means contribute. I could use the help.
