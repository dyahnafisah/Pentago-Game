# Pentago-Game
Pentago Game with  various levels of computer bots with different methods of decision-making including Minimax Algorithm with Alpha-Betha Pruning

## Description
Pentago is a board game designed by Tomas Flodén and developed and sold by Mindtwister. The rules are given below. Like chess and go, pentago is a two player, deterministic, perfect knowledge, zero sum game: there is no random or hidden state, and the goal of the two players is to make the other player lose (or at least tie).

Pentago is played on a 6 by 6 board, divided into four 3 by 3 quadrants. There are two players, black and white, who alternate turns. The goal of each player is to get five stones of their color in a row, either horizontally, vertically, or diagonally. Each turn, a player places a stone in an empty space in some quadrant, then chooses a possibly different quadrant to rotate 90 degrees left or right. If both players get five in a row at the same time, or the last move is played with no five in a row, the game is a tie. If a player makes five a row by placing a stone, there is no need to rotate a quadrant: the player wins immediately.

## Features
- Two playes
- Computer bots with various levels

Various levels of computer bots :
1. Easy (randomly pick a position)
2. Medium (if there is a possible position to win in one turn or to block the opponent from winning, then computer will choose that position. otherwise, random position will be chosen)
3. Hard (computer bot will decide position by using scoring system)
4. Super hard (computer bot will decide by using Minimax algorithm with alpha-betha pruning)
