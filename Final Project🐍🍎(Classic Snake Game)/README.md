# Welcome to the 'Snake Game'!
This is my classic <b> SNAKE GAME
</b>.

Developed this as my Final Project for the <a href=
"https://news.stanford.edu/2021/03/22/famous-stanford-coding-course-free-online/i">'Code In Place-2021'</a>, a remote learning experience offered by the Stanford University under Prof. Mehran Sahami, Prof. Chris Piech and 800+ Section Leaders teaching 10,000 students all over the world!

# About the game
About the Game:
Following is a walk-through showcasing the game:
<ul>
<li>The objective is to keep eating ‘Apple’ that appears in random locations to keep increasing your snake size.</li>
<li>Player has Keyboard controls provided for navigating Snake on the arena
<ul>
<li><strong>Controls: ← ↓ ↑ →   keys</strong></li>
</ul>
</li>
<li>The game goes on until the player's snake is dead. The score will be displayed at the end of the game.
<ul>
<li>Snake can die in any of the following scenarios:
<ul>
<li>Hits the wall / boundary</li>
<li>Hits itself</li>
</ul>
</li>
</ul>
</li>
</ul>
  
       
# Concepts used in the Code
  Code In Place laid down a strong foundation for programming fundamentals and Python. Almost all the concepts learned have been implemented through this code, which includes:

<li>Graphics
<li>Animation
<li>Functions & Decomposition
<li>Contorl Flow
<li>Variables and Expressions
<li>Images
<li>Text Processing </li>


In addition to these, <b>‘Classes’</b> have been utilized for proper code organization and encapsulation.

Exploring the coding techniques for implementing 'Classes' as well as the various <b>'Pygame'</b> features/usage was a fun learning experience! I have implimented object oriented programming concepts.

Libraries used: Pygame, random, time

# Algorithm

<ul>
<li>Snake is <strong>instantiated as a chain of squares</strong> appearing as a single long creature.</li>
<li>Navigating through the controls turns the snake in any of the four directions:
<ul>
<li>The ‘snake head’ is repositioned based on the player controls.</li>
<li>The block following the snake head is programmed to take snake head’s previous position in the subsequent frame. Similarly, the 3rd block takes the 2nd block position and so on.</li>
</ul>
</li>
<li>There is a <strong>provision in the code to modify the speed of the snake</strong>.</li>
<li><strong>Apples appear at random positions</strong> one after the other.</li>
<li><strong>Snake is checked for overlaps</strong> (either with food, itself) and actions are taken accordingly to either eat the food &amp; increase the score OR kill the snake.</li>
</ul>
