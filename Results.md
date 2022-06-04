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
The first model evaluated was a simple linear regression model with a "relu" activation function. 
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

As seen, the linear regression model can estimate some contracts correctly but is much too prone too error to be of any real use. 
Likewise, the training and dev set errors of around 750,000$ seem ok but in reality are not very good. 
Being 750,000$ off on a large contract, for example a 10 million dollar contract, might seem quite good. 
However, most contracts in the training set are quite low, usually around 1 or 2 million. 
Therefore, being 750,000$ off on those is actually quite a large error.  

## Neural Network Model

The next model evaluated was a custom-built neural network. 
This was arbitrarily picked to have 2 hidden layers, all using the "ReLU" activation function. 
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

