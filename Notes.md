# Estimator Results
## Building the Database
The goal of this project was to create a predictor that could take in the statistics of an NHL player and the duration of their contract 
and predict the average annual value of the contract. 
The first step in this was to build a database of players and contracts signed in the salary cap era. 
This was done by retrieving data from CapFriendly and ESPN (GetData.py). 
Retrieving this data can take considerable time and requires the user to have constant internet connection. 
For convenience, the option was also added to store this data into a file and automatically retrieve it on startup. 
This can be configured in the "GetInputsUI" function by setting **LoadDefaults** to **True**. 
Note that by default, this setting is on **False**. 
The default UI will then prompt the user to enter a filename or retrieve the data from the internet. 

## Building Contract List
The relevent database captured in the first step contains three portions: an active player list, a salary cap table and a team statistics list.
All of these are used to create a list of contracts that will serve as the input features of the model. 
This step is done in "CreateContractList" and then converted into a feature matric **X** and an output vector **Y** in "CreateFeatureMatrix". 
Note that this excludes Entry Level Contracts (ELCs) since these follow a specific set of rules. 

## Analyzing Features
For debugging purposes, the feature matrix can be viewed using the "PlotFeatureVector" function. 
This will plot the output (salary in millions of dollars) against the desired input. 
Some examples are shown below:  
<img src="https://user-images.githubusercontent.com/33467901/170896477-1ad7a226-fa61-4406-a010-e558303b10d7.png" alt="image" width="500"/>
<img src="https://user-images.githubusercontent.com/33467901/170896494-f5d4263b-9b3e-4361-b27c-f702e0952f79.png" alt="image" width="492"/>  
These two graphs plot salary against contract duration and player age respectively. 
As can be expected, the highest-valued contracts were on long term deals and for players in their prime (20-30 years old). 
Only a few contracts are longer than 8 years because of the CBA changes put in place a few years ago to restrict contracts to 8 years and less.  

Some features were shown to have a stronger correlation to the output than others. Here are some examples of strongly-correlated features:  
<img src="https://user-images.githubusercontent.com/33467901/170896826-85acbbd8-b0b5-4eac-a232-166c4496c77d.png" alt="image" width="470"/>
<img width="500" alt="image" src="https://user-images.githubusercontent.com/33467901/170896927-9e640e09-f05e-4fcc-be6b-fd238951705b.png">
<img src="https://user-images.githubusercontent.com/33467901/170896866-63e25209-e3d5-4da2-a8fd-7f509bf078d4.png" alt="image" width="500"/>  

And here are some examples where the salary and the features were less strongly correlated:  
<img src="https://user-images.githubusercontent.com/33467901/170896999-85c6eaf4-4711-4499-9dac-2baf0a9ae5ef.png" alt="image" width="500"/>
<img src="https://user-images.githubusercontent.com/33467901/170897002-840a1366-940f-4fb4-bbd9-b95112ee5b87.png" alt="image" width="500"/>  

These are only a few of the features used but it should be as expected that obvious features such as goals, 
assists and time-on-ice have a large impact on the salary of a player while more subtle features such as +/- and Corsi don't appear to have much impact.  

## Linear Regression Model

With the input and output data created, the next step was to build a model that could predict the outputs based on the inputs. 
The first model evaluated was a simple linear regression model with a *ReLU* activation function. 
With 10000 iterations and a learning rate of 0.001, this converged to a model with an average training error of 748,066\$ 
and a dev error of 760,177\$. 
Here is the cost function for that model:  

![image](https://user-images.githubusercontent.com/33467901/170897052-43557ee8-45f8-4068-b22b-ea403c94cb62.png)  

This model can be used to predict contract values for current players. Here are a few examples: 
- Connor McDavid (25 years old):
	- 8 years: 17,309,761\$	
	- 4 years: 14,415,362\$	
	- 1 year: 12,244,563\$
- Joe Pavelski (37 years old):
	- 8 years: 8,599,054\$	
	- 4 years: 5,704,655\$	
	- 1 year: 3,533,856\$
- Nick Suzuki (22 years old):
	- 8 years: 7,139,449\$	
	- 4 years: 4,245,051\$	
	- 1 year: 2,074,252\$  

These values are ok in some cases in outlandish in others. 
For example, Connor McDavid is the current highest-paid player in the league at 12,500,000\$. 
Yes, he has improved since then and the salary cap has gone up a bit but you wouldn't expect him to command over 17 million dollars on a long-term deal. 
The other values are more reasonable. Joe Pavelski, at 37 years old, would realistically never get more than a 1 or 2-year contract. 
The amount attributed to long term deals here is unrealistic. Likewise, the amount for a 1-year deal is too low. 
As a young player, Nick Suzuki's 8 year deal at that figure makes sense. 
This is very close to the actual contract he just signed (7,975,000\$). 
However, once again, the short-term values are much too low.  

One interesting aspect to note here is the linear nature of the weights. In this case, no matter what age the player is, the salary difference based on contract length is always the same (5,065,198\$) 
between a 1-year deal and an 8-year deal. This is obviously unrealistic and highlights the limitations of single-layer linear regression for this particular problem.  

As seen, the linear regression model can estimate some contracts correctly but is much too prone to error to be of any real use. 
Likewise, the training and dev set errors of around 750,000$ seem ok but in reality are not very good. 
Being 750,000$ off on a large contract, for example a 10 million dollar contract, might seem quite good. 
However, most contracts in the training set are quite low, usually around 1 or 2 million. 
Therefore, being 750,000\$
off on those is actually quite a large error. In fact, the average player salary of the entire data set is only 1,502,214\$ 
above minimum salary so the error values here are just around half of that. 

## Neural Network Model

The next model evaluated was a custom-built neural network. 
This was arbitrarily picked to have 2 hidden layers, all using the *ReLU* activation function. 
The first layer was assigned 100 hidden units and the second one was assigned 50 units. 
As before, this was run with 10,000 iterations and a learning rate of 0.001. 
This resulted in a training error of 302,642\$, 
a dev error of 468,238\$ 
and a test error of 512,997\$. 
Here is the cost function of this:  

![image](https://user-images.githubusercontent.com/33467901/170897274-cc53fa24-07ec-4fb5-8029-c144c2f8f16a.png)  

The same values as before were used to make a few predictions. Here are the results: 
- Connor McDavid (25 years old): 
	- 8 years: 13,691,061\$	 
	- 4 years: 12,540,279\$	 
	- 1 year: 11,689,378\$
- Joe Pavelski (37 years old): 
	- 8 years: 8,494,686\$	
	- 4 years: 6,756,505\$	
	- 1 year: 5,457,928\$
- Nick Suzuki (22 years old): 
	- 8 years: 7,370,716\$	
	- 4 years: 5,381,573\$	
	- 1 year: 3,907,046\$  

These results make a lot more sense, especially for McDavid and Suzuki. 
Pavelski's 1-year contract also seems fair. 
As before, the 4-year and 8-year contracts for Pavelski are completely wrong. 
This could be due to the model or also possibly to the lack of data itself. 
For obvious reasons, no player of that age has signed long-term contracts before so it's possible that the model isn't able to project this kind of data. 
With the dev and test sets being much higher than the training set, it's also possible this model is suffering from overfitting. 
That would make it worse at generalizing to new examples, such as the contracts attempted above.  

Here, the non-linear nature of the model can also be seen. Previously, salary difference between a 1-year deal and an 8-year deal were always the same. In this case however, the behavior is much different. For 25-year old Connor McDavid, the difference is very small (2,001,683\$)
while for 22-year old Nick Suzuki, the difference is much larger (3,463,670\$).
This shows that the non-linear approach is adding benefit as expected.  

## Simple TensorFlow Model

This model was built using a similar architecture to the custom-built neural network. As before, this network used 2 hidden layers of 100 and 50 units respectively. 
Once again, this used batch gradient descent with 10000 iterations. In this case, the Adam optimization was added to speed up convergence. The cost function and metric used to evaluate the model were both set to use mean-squared error since the output layer contained a *ReLU* activation function. For this model, the learning rate was set to 0.0001. The results of this were a training error of 31,027\$, 
a dev error of 532,813\$, 
and a test error of 594,692\$.
Note that this model had a much better training error than the custom-built one but a slightly larger dev and test error. This is likely due to this model overfitting the training set. No regularization was used for this model either so this is no major surprise. It is however quite interesting to see how much the Adam optimization helped improve convergence speed. 
Here is a view of the resulting cost function:  

![image](https://user-images.githubusercontent.com/33467901/172021968-2d0f382e-ee27-44af-9e25-c873b30a57e4.png)  

Note that the cost function is now based on the pre-built tensorflow *MeanSquaredError* metric instead of the custom-built cost function used in the previous networks. Therefore, the values plotted for the cost function no longer correspond to the final training error. However, the trend of the data is still valid. 

As before, the same player predictions were made. Here are the results: 
- Connor McDavid (25 years old): 
	- 8 years: 16,132,630\$	 
	- 4 years: 14,948,495\$	 
	- 1 year: 14,018,498\$
- Joe Pavelski (37 years old): 
	- 8 years: 9,203,255\$	
	- 4 years: 6,999,432\$	
	- 1 year: 5,507,911\$
- Nick Suzuki (22 years old): 
	- 8 years: 7,879,461\$	
	- 4 years: 5,399,962\$	
	- 1 year: 3,448,613\$  

These are fairly comparable to the custom network results. The values for Connor McDavid are quite a bit higher than before which seems a little less realistic. On the other hand, Nick Suzuki's numbers are closer to the actual contract he signed. In general, this seems like similar performance, which is to be expected since the dev set accuracy is similar to the custom model. 


## Regularizing TensorFlow Model

The same model from the previous section was trained with regularization. In this case, L2 regularization with a regularization constant of 0.07 was used. All other parameters were kept the same. This yielded a training error of 407,477\$,
a dev error of 465,301\$ 
and a test error of 513,246\$.
Here, the training error was quite a bit worse than the previous model but the dev error was reduced by around 67,000\$ 
which means the model is generalizing better to new examples than before. 
Here are the results from the same player predictions: 
- Connor McDavid (25 years old): 
	- 8 years: 11,743,089\$	 
	- 4 years: 10,433,278\$	 
	- 1 year: 9,276,291\$
- Joe Pavelski (37 years old): 
	- 8 years: 7,718,580\$	
	- 4 years: 5,768,960\$	
	- 1 year: 4,292,509\$
- Nick Suzuki (22 years old): 
	- 8 years: 6,916,112\$	
	- 4 years: 5,106,769\$	
	- 1 year: 3,865,311\$  

In general, these are considerably lower than the unregrularized model. While the unregularized model seemed to predict values that were slightly too high, this seems to predict values that are slightly too low. 


## Hyperparameter Tuning

Different hyperparameters were tuned to attempt to improve performance. First, different regularization constants were tuned. Here are the resulting errors for a few different values:  

| L1 Regularization | L2 Regularization | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :---------------- | :---------------- | -------------------: | -----------------: | ------------------: |
|                 0 |              0.01 |              147,979 |            496,666 |             567,323 |
|                 0 |              0.03 |              283,631 |            458,783 |             504,995 |
|            0.0025 |              0.01 |              295,365 |            450,420 |             502,607 |
|            0.0025 |             0.015 |              330,331 |            450,981 |             498,568 |
|             **0.005** |              **0.01** |              **349,350** |            **440,466** |             **482,269** |
|             0.005 |              0.03 |              409,033 |            462,220 |             497,111 |
|            0.0075 |              0.01 |              404,768 |            448,414 |             491,605 |
|              0.01 |              0.01 |              420,997 |            453,759 |             485,026 |

Based on this, the regularization constants were set to L1 = 0.005 and L2 = 0.01 respectively since that combination gave the lowest dev set error.
Tuning the regularization fixed the overfitting problem but resulted in a model with a dev set error of around 440,000\$,
which was still quite high. Next, the number of feature units in each layer were tuned to try to reduce the error further. Here are the results: 

| Layer 1 Units | Layer 2 Units | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :------------ | :------------ | -------------------: | -----------------: | ------------------: |
|            50 |            25 |              356,576 |            447,867 |             489,767 |
|           200 |           100 |              376,400 |            443,548 |             485,994 |
|           400 |           100 |              342,123 |            434,596 |             491,848 |
|           **500** |           **250** |              **353,019** |            **427,664** |             **471,498** |
|           700 |           350 |              362,664 |            435,821 |             483,617 |
|          1000 |           500 |              358,342 |            454,832 |             484,152 |

It seems here like the best option was the model with 500 units in the first layer and 250 units in the second layer. Note that all of these models have used a decreasing structure where the second layer had half of the units of the first layer. This was arbitrarily decided. To test this assumption, the following models were used. 

| Layer 1 Units | Layer 2 Units | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :------------ | :------------ | -------------------: | -----------------: | ------------------: |
|           250 |           500 |              364,481 |            463,884 |             498,928 |
|           500 |           500 |              350,332 |            437,408 |             479,601 |

Both of these test cases were worse than the original case with 500 units in Layer 1 and 250 units in Layer 2. Therefore, the original structure of decreasing the units every layer was kept. The next step was to test with an extra *ReLU* layer and see if that improved performance.

| Layer 1 Units | Layer 2 Units | Layer 2 Units | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :------------ | :------------ | :------------ | -------------------: | -----------------: | ------------------: |
|           500 |           250 |           125 |              277,371 |            483,578 |             514,586 |
|           500 |           400 |           250 |              261,671 |            444,010 |             518,988 |

Neither model was an improvement on the original so the 2-layer *ReLU* structure was kept. Next, a *tanh* layer was inserted in a similar way to see if this would act any differently.  

| Layer 1 Units | Layer 2 Units | Layer 2 Units | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :------------ | :------------ | :------------ | -------------------: | -----------------: | ------------------: |
| *tanh*   1000 | *ReLU*    500 | *ReLU*    250 |              305,061 |            486,866 |             517,904 |
| *ReLU*    500 | *tanh*    325 | *ReLU*    250 |              311,867 |            465,769 |             521,623 |
| *ReLU*    500 | *ReLU*    250 | *tanh*    125 |              269,197 |            465,675 |             514,931 |

None of these models were an improvement so no *tanh* layer was added.  

Next, a variable learning rate was introduced. In this case, exponential decay was used to generate the learning rate. Here are the results for various configurations: 

| Initial Learning Rate | Decay Steps | Decay Rate | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :-------------------- | :---------- | :--------- | -------------------: | -----------------: | ------------------: |
|                0.0001 |        1000 |       0.95 |              355,342 |            428,278 |             472,366 |
|                0.0001 |       10000 |        0.9 |              352,229 |            426,886 |             470,533 |
|                **0.0001** |       **10000** |       **0.75** |              **354,049** |            **425,121** |             **472,232** |
|                0.0001 |       10000 |        0.5 |              357,035 |            428,832 |             473,486 |
|                0.0002 |        1000 |       0.95 |              345,761 |            438,599 |             475,074 |
|                0.0002 |        1000 |       0.75 |              367,040 |            434,584 |             475,297 |
|                0.0002 |        1000 |        0.5 |              403,909 |            446,395 |             497,046 |
|                0.0005 |        1000 |       0.95 |              362,105 |            463,917 |             499,570 |
|                0.0005 |        1000 |       0.75 |              356,124 |            465,338 |             497,143 |
|                0.0005 |        1000 |        0.5 |              394,083 |            462,229 |             498,247 |
|                0.0005 |        1000 |        0.3 |              405,644 |            455,352 |             498,801 |
|                0.0005 |        1000 |        0.1 |              436,330 |            458,058 |             498,455 |
|                0.001  |        1000 |       0.95 |              372,525 |            474,271 |             493,834 |
|                0.001  |        1000 |       0.75 |              364,623 |            448,092 |             485,484 |
|                0.001  |        1000 |        0.5 |              382,125 |            458,376 |             491,301 |
|                0.001  |        1000 |        0.1 |              351,941 |            463,638 |             509,688 |
|                0.001  |        1000 |       0.03 |              366,959 |            457,626 |             498,690 |
|                0.001  |        1000 |       0.01 |              379,849 |            452,895 |             494,326 |
|                0.001  |        1000 |      0.003 |              382,460 |            453,000 |             488,972 |
|                0.003  |        1000 |      0.003 |              391,493 |            445,450 |             498,492 |
|                0.003  |        1000 |      0.001 |              391,728 |            445,197 |             499,952 |
|                0.003  |        1000 |     0.0003 |              391,816 |            445,650 |             499,486 |
|                0.01   |        1000 |        0.5 |              349,823 |            463,792 |             510,400 |
|                0.01   |        1000 |        0.1 |              359,636 |            459,602 |             509,302 |
|                0.01   |        1000 |       0.05 |              328,232 |            458,313 |             505,140 |
|                0.01   |        1000 |       0.01 |              336,955 |            469,936 |             502,201 |


None of these offered a major improvement over the static learning rate of 0.0001. The best outcome was with an initial learning rate of 0.0001 as used before and a decay rate of 0.75 over 10000 iterations  (dev error of 425,121\$ 
instead of 427,664\$).
This is the learning rate that was chosen. 

## Hand-Engineering Features

The next step was to hand-engineer some features from the available data. Ideally, these are features that the network would have learned. However, with the limited number of examples available, this hand-engineering was tried to obtain better results. First, the following features were added: 
- Points-per-game
- Ratio of games played (player GP / team GP)
- Ratio of team offense generated (player points / team goals)
- Difference between player +/- and team +/-

Adding these features resulted in a training error of 333,920\$
and a dev error of 398,131\$
which was a noticeable improvement. 

## Testing PCA

With the new features added, there were now a lot of features with very strong correlation (i.e. points and points-per-game). PCA was attempted with different thresholds of variance retained to see if this would offer any improvement on performance. Here are the results: 

| PCA threshold (\%) | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :----------------- | -------------------: | -----------------: | ------------------: |
|  100               |              350,528 |            445,090 |             485,030 |
|  99                |              582,674 |            646,264 |             684,800 |

These results were considerably worse than the non-PCA version so PCA was dropped for now. 

## Getting More Data and Fixing Normalization

I wanted to add more features and see if this would improve performance. In order to make that work, I had to re-fetch the data from CapFriendly and add these new features to the player info. This included features like player height, weight, draft position and various career stats such as total career points, earnings, etc. I also added the "team" feature but made this one optional. Ideally, the network would predict player value regardless of what team he signed for but I was curious to see how much the team would affect the model performance. In the process of doing this, I also fixed a bug in the normalization of the data where the mean of the data was not getting subtracted properly. Adding all of these changes yieled the following results: 

| Team Info Included | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :----------------- | -------------------: | -----------------: | ------------------: |
|  No                |              225,161 |            475,476 |             504,744 |
|  Yes               |              219,056 |            508,023 |             509,862 |

It seems as though the team variable did not significantly affect the results. It reduced the training error slightly and increased the dev error slightly. The **UseTeamsInfo** will be kept to **True** for now but can probably be reverted to **False** later without significantly affecting the results. It's also important to note that the overall dev set error went up from before (398,131\$)
but the training error is noticeably lower than the previous value (333,920\$). 
Another important thing to note is that fetching this new data also changed the contract examples grabbed from CapFriendly. This includes adding the contracts signed since the last data fetch. Unfortunately, this also caused all currently pending unrestricted free agents to be removed from the active player list, meaning that those players and their previous contracts no longer show up in the dataset. This caused a significant change in the distribution of data. The average contract salary is now 2,014,599\$ 
above minimum salary which is noticeably higher than before (1,502,214\$).
With the large difference between the dev error and the training error, it seems like the model is starting to overfit the data again. More tuning is likely required. 

## Re-Fetching Data from CapFriendly

The last tests were missing a significant amount of examples from CapFriendly because of all of the players who had become unrestricted free agents. This time, the data was re-fetched and changed to include those free agents as well. This gave an average contract salary of 1,480,275\$ 
which is more in line with the previous value and the following error results: 

| Team Info Included | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :----------------- | -------------------: | -----------------: | ------------------: |
|  No                |              276,827 |            383,759 |             356,408 |
|  Yes               |              271,550 |            376,723 |             353,583 |

Now, the dev error is much lower while the training error has gone up a bit. This makes sense because this is including more examples. Therefore, overfitting is less likely. One interesting thing to note here is that including the teams information now has a noticeable change on the dev error. 

## Hyperparameter Tuning Round 2

With the new features added, I wanted to retry some of the previous attempts to improve performance. First, I re-inserted the *tanh* layer to see if it would behave any differently now. Here are the results: 

| Layer 1 Units | Layer 2 Units | Layer 2 Units | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :------------ | :------------ | :------------ | -------------------: | -----------------: | ------------------: |
| *tanh*   1000 | *ReLU*    500 | *ReLU*    250 |              199,924 |            412,843 |             435,815 |
| *ReLU*    500 | *tanh*    325 | *ReLU*    250 |              179,375 |            433,290 |             417,434 |
| ***ReLU*    500** | ***ReLU*    250** | ***tanh*    125** |              **193,428** |            **401,829** |             **399,579** |

The last test had a slightly higher dev set error than the previous architecture (25,000\$ 
higher) but a much lower training set error (80,000\$
lower). This seemed promising so this model was selected for another run through the regularization tuning. Here are the results from that: 

| L1 Regularization | L2 Regularization | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :---------------- | :---------------- | -------------------: | -----------------: | ------------------: |
|            0.0025 |             0.015 |              172,770 |            411,472 |             397,240 |
|            0.0025 |              0.03 |              229,696 |            387,542 |             393,191 |
|             0.005 |              0.03 |              265,318 |            386,270 |             366,272 |
|            0.0075 |              0.01 |              253,727 |            401,669 |             364,153 |
|              0.01 |              0.01 |              286,464 |            393,733 |             363,142 |  

None of these dev errors were better than the 376,723\$
achieved with the previous architecture so the *tanh* layer was removed and the original architecture was re-introduced. This was once again run through the regularization tuning to give the following results: 

| L1 Regularization | L2 Regularization | Train Set Error (\$) | Dev Set Error (\$) | Test Set Error (\$) |
| :---------------- | :---------------- | -------------------: | -----------------: | ------------------: |
|            0.0025 |             0.015 |              233,543 |            380,069 |             374,406 |
|            0.0025 |              0.03 |              276,281 |            380,407 |             355,103 |
|             0.005 |              0.03 |              311,665 |            371,876 |             354,835 |
|            **0.0075** |              **0.01** |              **293,919** |            **366,970** |             **362,060** |
|            0.0075 |              0.03 |              323,342 |            376,740 |             362,604 |  

This produced a slightly better dev error of 366,970\$
with an L1 regularization factor of 0.0075 and a L2 regularization factor of 0.01 so this is the combination that was used going forward. 


## Conclusion
With a dev error of 366,970\$,
this model was deemed acceptable. The test error is 362,060\$
so this is a reasonable estimate of the typical error that the model might encounter. This model is the one that was used to generate the results in Analysis.md.  
