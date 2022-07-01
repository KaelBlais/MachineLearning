# Model Predictions

## Predicting Upcoming Free Agents
With the model built from a data set acquired just before the NHL 2022 Free Agency window, I wanted to run some salary predictions on upcoming free agents.
In order to make the predictions, I had to also select a team and a contract length for each free agent. To keep things simple, I selected each free agent's current
team and an arbitrary number of years based on my own personal intuition. This could change the salary slightly but the predicted number should still be relatively close
regardless of these two variables. Here are the results: 

| Player Name        | Number of Years | Predicted Salary (\$)|
| :----------------- | :-------------- | -------------------: |
| Evgeni Malkin      |               3 |            0,000,000 |



## Sorting Current Contracts From Best to Worst
Another application for this model is to evaluate current contracts in the NHL. This can be done by looking at every player with a contract for next year and beyond and
predicting that player's salary if they were to sign a contract today with the same number of year as the remaining term on their current contract. The difference between 
the player's actual salary and predicted salary is what was used to evaluate the contract. If the player is making less than he is worth, this was deemed a "good" contract. 
In other words, these players are ranked based on how team-friendly their contracts are. Note that this is only looking at salary, not contract length. Another important thing
to note is that this model has no awareness of LTIR rules. Therefore, some of the worst contracts will be for players that are known to be on LTIR for the rest of their careers
(for example, Brent Seabrook and Shea Weber). Here is the list: 

| Rank | Player Name        | Contract Salary (\$) | Predicted Salary (\$)| Salary Difference (\$)|
| :--- | :----------------- | :------------------- | :------------------- |---------------------: |
|    1 | Nathan MacKinnon   |            6,300,000 |            9,418,023 |             3,118,023 | 
|    2 | Mark Giordano      |              800,000 |            3,683,330 |             2,883,330 | 
|    3 | Leon Draisaitl     |            8,500,000 |           11,286,996 |             2,786,996 | 
|    4 | Gabriel Landeskog  |            7,000,000 |            9,535,521 |             2,786,996 | 
|    5 | Devon Toews        |            4,100,000 |            6,364,061 |             2,264,061 | 
|    6 | Jordan Kyrou       |            2,800,000 |            5,049,123 |             2,249,123 | 
|    7 | Troy Terry         |            1,450,000 |            3,652,695 |             2,202,695 |
|    8 | Roope Hintz        |            3,150,000 |            5,340,322 |             2,190,322 | 
|    9 | Tage Thompson      |            1,400,000 |            3,580,933 |             2,180,933 |
|   10 | Ryan Hartman       |            1,700,000 |            3,879,691 |             2,179,691 |
|  ... | ...                |            ...       |            ...       |             ...       |
|  506 | Nicklas Bäckström  |            9,200,000 |            5,203,438 |            -3,996,561 | 
|  507 | Jamie Benn         |            9,500,000 |            5,373,897 |            -4,126,102 | 
|  508 | Jack Eichel        |           10,000,000 |            5,803,566 |            -4,196,433 | 
|  509 | Milan Lucic        |            6,000,000 |            1,779,763 |            -4,220,236 | 
|  510 | Erik Karlsson      |           11,500,000 |            7,128,250 |            -4,371,749 | 
|  511 | Bryan Little       |            5,291,666 |              800,988 |            -4,490,677 | 
|  512 | Andrew Ladd        |            5,500,000 |              795,737 |            -4,704,262 |
|  513 | Shea Weber         |            7,857,142 |            2,981,110 |            -4,876,031 | 
|  514 | Brent Seabrook     |            6,875,000 |            1,110,408 |            -5,764,591 |
|  515 | Jonathan Toews     |           10,500,000 |            3,530,325 |            -6,969,674 |
