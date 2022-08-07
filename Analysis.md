# Model Predictions

## Predicting Upcoming Free Agents
With the model built from a data set acquired just before the NHL 2022 Free Agency window, I wanted to run some salary predictions on upcoming free agents.
In order to make the predictions, I had to also select a team and a contract length for each free agent. To keep things simple, I selected each free agent's current
team and an arbitrary number of years based on my own personal intuition. This could change the salary slightly but the predicted number should still be relatively close as long as the number of years is within a reasonable range. Here are the results: 

| Player Name        | Number of Years | Predicted Salary (\$)|
| :----------------- | :-------------- | -------------------: |
| Matthew Tkachuk    |               8 |           10,687,435 |
| Johnny Gaudreau    |               8 |           10,665,861 |
| Filip Forsberg     |               8 |            9,317,346 |
| Patrik Laine       |               8 |            8,338,588 |
| John Klingberg     |               8 |            8,243,446 |
| Pierre-Luc Dubois  |               8 |            8,034,573 |
| Jason Robertson    |               8 |            7,983,898 |
| Jesper Bratt       |               8 |            7,677,048 |
| Noah Dobson        |               8 |            6,829,473 |
| Nazem Kadri        |               5 |            6,764,480 |
| Brock Boeser       |               6 |            6,708,962 |
| Vincent Trocheck   |               6 |            6,650,706 |
| Ryan Strome        |               5 |            6,529,021 |
| Anthony Deangelo   |               5 |            6,468,697 |
| Andrew Copp        |               6 |            6,173,133 |
| Evgeni Malkin      |               3 |            6,141,986 |
| Claude Giroux      |               2 |            6,082,915 |
| Evander Kane       |               5 |            6,035,253 |
| Kris Letang        |               2 |            5,971,721 |
| Patrice Bergeron   |               1 |            5,711,189 |
| Valeri Nichushkin  |               6 |            5,697,164 |
| Andrew Mangiapane  |               6 |            5,561,766 |
| Adrian Kempe       |               4 |            5,160,096 |
| Josh Norris        |               6 |            5,092,355 |
| Ondrej Palat       |               3 |            5,045,128 |
| David Perron       |               2 |            4,885,797 |
| Dylan Strome       |               4 |            4,572,534 |
| Phil Kessel        |               1 |            4,433,701 |
| Artturi Lehkonen   |               4 |            4,251,189 |
| Max Domi           |               3 |            4,077,223 |
| Kailer Yamamoto    |               5 |            3,708,541 |
| Oliver Kylington   |               5 |            3,513,194 |
| Jesse Puljujarvi   |               5 |            3,479,555 |
| P.K. Subban        |               1 |            3,415,392 |
| Ben Chiarot        |               4 |            3,301,250 |
| Nikita Zadorov     |               2 |            2,850,423 |
| Mason Marchment    |               3 |            2,764,651 |
| Alexander Romanov  |               2 |            1,813,480 |


## Updated Predictions and Comparisons
Now that most of the notable free agents have signed a new deal, I re-ran the same model with the correct team and number of years that the players ended up actually signing for. Here are the results based on that: 

| Player Name        | Team                   | Number of Years | Predicted Salary (\$)| Actual Salary (\$)| Difference (\$)|
| :----------------- | :--------------------- | :-------------- | -------------------: |  ---------------: |  ------------: | 
| Matthew Tkachuk    | Florida Panthers       |               8 |           10,573,105 |         9,500,000 |      1,073,105 |
| Johnny Gaudreau    | Columbus Blue Jackets  |               7 |           10,118,556 |         9,750,000 |        368,556 |
| Filip Forsberg     | Nashville Predators    |               8 |            9,317,346 |         8,500,000 |        817,346 |
| Patrik Laine       | Columbus Blue Jackets  |               4 |            6,622,471 |         8,700,000 |      2,077,529 |
| John Klingberg     | Anaheim Ducks          |               1 |            5,119,032 |         7,000,000 |      1,880,968 |
| Pierre-Luc Dubois  | Winnipeg Jets          |               1 |            5,069,740 |         6,000,000 |        930,260 |
| Jesper Bratt       | New Jersey Devils      |               1 |            4,728,332 |         5,450,000 |        721,668 |
| Brock Boeser       | Vancouver Canucks      |               3 |            5,438,557 |         6,650,000 |      1,211,443 |
| Vincent Trocheck   | New York Rangers       |               7 |            7,072,030 |         5,625,000 |      1,447,030 |
| Ryan Strome        | Anaheim Ducks          |               5 |            6,410,731 |         5,000,000 |      1,410,731 |
| Anthony Deangelo   | Philadelphia Flyers    |               2 |            3,849,968 |         5,000,000 |      1,150,032 |
| Andrew Copp        | Detroit Red Wings      |               5 |            5,760,228 |         5,625,000 |        135,228 |
| Evgeni Malkin      | Pittsburgh Penguins    |               4 |            6,590,423 |         6,100,000 |        490,423 |
| Claude Giroux      | Ottawa Senators        |               3 |            6,534,062 |         6,500,000 |         34,062 |
| Evander Kane       | Edmonton Oilers        |               4 |            5,675,754 |         5,125,000 |        550,754 |
| Kris Letang        | Pittsburgh Penguins    |               6 |            7,674,904 |         6,100,000 |      1,574,904 |
| Valeri Nichushkin  | Colorado Avalanche     |               8 |            6,599,085 |         6,125,000 |        474,085 |
| Andrew Mangiapane  | Calgary Flames         |               3 |            4,312,605 |         5,800,000 |      1,487,395 |
| Adrian Kempe       | Los Angeles Kings      |               4 |            5,174,495 |         5,500,000 |        325,505 |
| Josh Norris        | Ottawa Senators        |               8 |            5,950,970 |         7,950,000 |      1,999,030 |
| Ondrej Palat       | New Jersey Devils      |               5 |            5,762,359 |         6,000,000 |        237,641 |
| David Perron       | Detroit Red Wings      |               2 |            4,810,154 |         4,750,000 |         60,154 |
| Dylan Strome       | Washington Capitals    |               1 |            3,141,666 |         3,500,000 |        358,334 |
| Artturi Lehkonen   | Colorado Avalanche     |               5 |            4,705,405 |         4,500,000 |        205,405 |
| Max Domi           | Chicago Blackhawks     |               1 |            3,342,427 |         3,000,000 |        342,427 |
| Kailer Yamamoto    | Edmonton Oilers        |               2 |            2,466,280 |         3,100,000 |        633,720 |
| Oliver Kylington   | Calgary Flames         |               2 |            2,262,911 |         2,500,000 |        237,089 |
| Jesse Puljujarvi   | Edmonton Oilers        |               1 |            2,216,218 |         3,000,000 |        783,782 |
| Ben Chiarot        | Detroit Red Wings      |               4 |            3,331,353 |         4,750,000 |      1,418,647 |
| Nikita Zadorov     | Calgary Flames         |               2 |            2,852,979 |         3,750,000 |        897,021 |
| Mason Marchment    | Dallas Stars           |               4 |            3,048,939 |         4,500,000 |      1,451,061 |

Looking at these numbers, the average error was 864,043\$.
At first glance, this seems much worse than the expected test set error of 362,532\$
calculated by the model. However, it's worth noting that these exampels represent the highest-valued contracts signed so it would be expected that these would have the most error as well. Looking at this table above, the average player salary is 4,500,031\$
and the average error is 864,043\$.
This gives an average error of 19.2\%.
The data in the entire set has an average value of 1,480,275\$ 
above minimum salary. For 2022-2023, this would mean an average salary of 2,230,275\$
which means the test error of 362,532\$
amounts to around 16.3\%
of that. Given that context, having 19.2\% 
error on the data set above seems more reasonable. 

## Sorting Current Contracts From Best to Worst
Another application for this model is to evaluate current contracts in the NHL. This can be done by looking at every player with a contract for next year and beyond and predicting that player's salary if they were to sign a contract today with the same number of years as the remaining term on their current contract. The difference between the player's actual salary and predicted salary is what was used to evaluate the contract. If the player is making less than he is worth, this was deemed a "good" contract. 
In other words, these players are ranked based on how team-friendly their contracts are. Note that this is only looking at salary, not contract length. Another important thing to note is that this model has no awareness of LTIR rules. Therefore, some of the worst contracts will be for players that are known to be on LTIR for the rest of their careers
(for example, Brent Seabrook and Shea Weber). Here is the list: 

| Rank | Player Name        | Contract Salary (\$) | Predicted Salary (\$)| Number of Years Left | Salary Difference (\$)|
| :--- | :----------------- | :------------------- | :------------------- | :------------------- | ---------------------: |
|    1 | Nathan MacKinnon   |            6,300,000 |            9,418,023 |                    1 |              3,118,023 | 
|    2 | Mark Giordano      |              800,000 |            3,683,330 |                    2 |             2,883,330 | 
|    3 | Leon Draisaitl     |            8,500,000 |           11,286,996 |                    3 |             2,786,996 | 
|    4 | Gabriel Landeskog  |            7,000,000 |            9,535,521 |                    7 |             2,786,996 | 
|    5 | Devon Toews        |            4,100,000 |            6,364,061 |                    2 |             2,264,061 | 
|    6 | Jordan Kyrou       |            2,800,000 |            5,049,123 |                    1 |             2,249,123 | 
|    7 | Troy Terry         |            1,450,000 |            3,652,695 |                    1 |             2,202,695 |
|    8 | Roope Hintz        |            3,150,000 |            5,340,322 |                    1 |             2,190,322 | 
|    9 | Tage Thompson      |            1,400,000 |            3,580,933 |                    1 |             2,180,933 |
|   10 | Ryan Hartman       |            1,700,000 |            3,879,691 |                    2 |             2,179,691 |
|  ... | ...                |            ...       |            ...       |                  ... |             ...       |
|  506 | Nicklas Bäckström  |            9,200,000 |            5,203,438 |                    3 |            -3,996,561 | 
|  507 | Jamie Benn         |            9,500,000 |            5,373,897 |                    3 |            -4,126,102 | 
|  508 | Jack Eichel        |           10,000,000 |            5,803,566 |                    4 |            -4,196,433 | 
|  509 | Milan Lucic        |            6,000,000 |            1,779,763 |                    1 |            -4,220,236 | 
|  510 | Erik Karlsson      |           11,500,000 |            7,128,250 |                    5 |            -4,371,749 | 
|  511 | Bryan Little       |            5,291,666 |              800,988 |                    2 |            -4,490,677 | 
|  512 | Andrew Ladd        |            5,500,000 |              795,737 |                    1 |            -4,704,262 |
|  513 | Shea Weber         |            7,857,142 |            2,981,110 |                    4 |            -4,876,031 | 
|  514 | Brent Seabrook     |            6,875,000 |            1,110,408 |                    2 |            -5,764,591 |
|  515 | Jonathan Toews     |           10,500,000 |            3,530,325 |                    1 |            -6,969,674 |
