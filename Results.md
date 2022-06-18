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
- L1 = 0, L2 = 0.01: 
	- Train Set: 147,979\$	 
	- Dev Set: 496,666\$	 
	- Test Set: 567,323\$ 
- L1 = 0, L2 = 0.03: 
	- Train Set: 283,631\$	 
	- Dev Set: 458,783\$	 
	- Test Set: 504,995\$  
- L1 = 0.0025, L2 = 0.01: 
	- Train Set: 295,365\$	 
	- Dev Set: 450,420\$	 
	- Test Set: 502,607\$  
- L1 = 0.0025, L2 = 0.015: 
	- Train Set: 330,331\$	 
	- Dev Set: 450,981\$	 
	- Test Set: 498,568\$  
- **L1 = 0.005, L2 = 0.01:** 
	- **Train Set: 349,350\$**	 
	- **Dev Set: 440,466\$**	 
	- **Test Set: 482,269\$**  
- L1 = 0.005, L2 = 0.03: 
	- Train Set: 409,033\$	 
	- Dev Set: 462,220\$	 
	- Test Set: 497,111\$  
- L1 = 0.0075, L2 = 0.01: 
	- Train Set: 404,768\$	 
	- Dev Set: 448,414\$	 
	- Test Set: 491,605\$  
- L1 = 0.01, L2 = 0.01: 
	- Train Set: 420,997\$	 
	- Dev Set: 453,759\$	 
	- Test Set: 485,026\$  

Based on this, the regularization constants were set to L1 = 0.005 and L2 = 0.01 respectively since that combination gave the lowest dev set error.
Tuning the regularization fixed the overfitting problem but resulted in a model with a dev set error of around 440,000\$,
which was still quite high. Next, the number of feature units in each layer were tuned to try to reduce the error further. Here are the results: 
- Layer 1 = 50 units, Layer 2 = 25 units: 
	- Train Set: 356,576\$	 
	- Dev Set: 447,867\$	 
	- Test Set: 489,767\$  
- Layer 1 = 200 units, Layer 2 = 100 units: 
	- Train Set: 376,400\$	 
	- Dev Set: 443,548\$	 
	- Test Set: 485,994\$  
- Layer 1 = 400 units, Layer 2 = 200 units: 
	- Train Set: 342,123\$	 
	- Dev Set: 434,596\$	 
	- Test Set: 491,848\$  
- **Layer 1 = 500 units, Layer 2 = 250 units:** 
	- **Train Set: 353,019\$**	 
	- **Dev Set: 427,664\$**	 
	- **Test Set: 471,498\$**  
- Layer 1 = 700 units, Layer 2 = 350 units: 
	- Train Set: 362,664\$	 
	- Dev Set: 435,821\$	 
	- Test Set: 483,617\$  
- Layer 1 = 1000 units, Layer 2 = 500 units: 
	- Train Set: 358,342\$	 
	- Dev Set: 454,832\$	 
	- Test Set: 484,152\$  

It seems here like the best option was the model with 500 units in the first layer and 250 units in the second layer. Note that all of these models have used a decreasing structure where the second layer had half of the units of the first layer. This was arbitrarily decided. To test this assumption, the following models were used. 
- Layer 1 = 250 units, Layer 2 = 500 units: 
	- Train Set: 364,481\$	 
	- Dev Set: 463,884\$	 
	- Test Set: 498,928\$  
- Layer 1 = 500 units, Layer 2 = 500 units: 
	- Train Set: 350,332\$	 
	- Dev Set: 437,408\$	 
	- Test Set: 479,601\$  

Both of these test cases were worse than the original case with 500 units in Layer 1 and 250 units in Layer 2. Therefore, the original structure of decreasing the units every layer was kept. The next step was to test with an extra *ReLU* layer and see if that improved performance.
- Layer 1 = 500 units, Layer 2 = 250 units,  Layer 3 = 125 units: 
	- Train Set: 277,371\$	 
	- Dev Set: 483,578\$	 
	- Test Set: 514,586\$  
- Layer 1 = 500 units, Layer 2 = 400 units,  Layer 3 = 250 units: 
	- Train Set: 261,671\$	 
	- Dev Set: 444,010\$	 
	- Test Set: 518,988\$  

Neither model was an improvement on the original so the 2-layer *ReLU* structure was kept. Next, a *tanh* layer was inserted in a similar way to see if this would act any differently.  
- Layer 1 (*tanh*) = 1000 units, Layer 2 (*ReLU*) = 500 units,  Layer 3 (*ReLU*) = 250 units: 
	- Train Set: 305,061\$	 
	- Dev Set: 486,866\$	 
	- Test Set: 517,904\$  
- Layer 1 (*ReLU*) = 500 units, Layer 2 (*tanh*) = 325 units,  Layer 3 (*ReLU*) = 250 units: 
	- Train Set: 311,867\$	 
	- Dev Set: 465,769\$	 
	- Test Set: 521,623\$  
- Layer 1 (*ReLU*) = 500 units, Layer 2 (*ReLU*) = 250 units,  Layer 3 (*tanh*) = 125 units: 
	- Train Set: 269,197\$	 
	- Dev Set: 465,675\$	 
	- Test Set: 514,931\$  

None of these models were an improvement so no *tanh* layer was added.  

Next, a variable learning rate was introduced. In this case, exponential decay was used to generate the learning rate. Here are the results for various configurations: 

- Inital learning rate = 0.0001, Decay steps = 1000, Decay rate = 0.95:
	- Train Set: 355,342\$	 
	- Dev Set: 428,278\$	 
	- Test Set: 472,366\$
- Inital learning rate = 0.0001, Decay steps = 10000, Decay rate = 0.9:
	- Train Set: 352,229\$	 
	- Dev Set: 426,886\$	 
	- Test Set: 470,533\$
- **Inital learning rate = 0.0001, Decay steps = 10000, Decay rate = 0.75**:
	- **Train Set: 354,049\$**	 
	- **Dev Set: 425,121\$**	 
	- **Test Set: 472,232\$**
- Inital learning rate = 0.0001, Decay steps = 10000, Decay rate = 0.5:
	- Train Set: 357,035\$	 
	- Dev Set: 428,832\$	 
	- Test Set: 473,486\$
- Inital learning rate = 0.0002, Decay steps = 1000, Decay rate = 0.95:
	- Train Set: 345,761\$	 
	- Dev Set: 438,599\$	 
	- Test Set: 475,074\$    
- Inital learning rate = 0.0002, Decay steps = 1000, Decay rate = 0.75:
	- Train Set: 367,040\$	 
	- Dev Set: 434,584\$	 
	- Test Set: 475,297\$    
- Inital learning rate = 0.0002, Decay steps = 1000, Decay rate = 0.5:
	- Train Set: 403,909\$	 
	- Dev Set: 446,395\$	 
	- Test Set: 497,046\$    
- Inital learning rate = 0.0005, Decay steps = 1000, Decay rate = 0.95:
	- Train Set: 362,105\$	 
	- Dev Set: 463,917\$	 
	- Test Set: 499,570\$  
- Inital learning rate = 0.0005, Decay steps = 1000, Decay rate = 0.75:
	- Train Set: 356,124\$	 
	- Dev Set: 465,338\$	 
	- Test Set: 497,143\$  
- Inital learning rate = 0.0005, Decay steps = 1000, Decay rate = 0.5:
	- Train Set: 394,083\$	 
	- Dev Set: 462,229\$	 
	- Test Set: 498,247\$  
- Inital learning rate = 0.0005, Decay steps = 1000, Decay rate = 0.3:
	- Train Set: 405,644\$	 
	- Dev Set: 455,352\$	 
	- Test Set: 498,801\$  
- Inital learning rate = 0.0005, Decay steps = 1000, Decay rate = 0.1:
	- Train Set: 436,330\$	 
	- Dev Set: 458,058\$	 
	- Test Set: 498,455\$  
- Inital learning rate = 0.001, Decay steps = 1000, Decay rate = 0.95:
	- Train Set: 372,525\$	 
	- Dev Set: 474,271\$	 
	- Test Set: 493,834\$  
- Inital learning rate = 0.001, Decay steps = 1000, Decay rate = 0.75:
	- Train Set: 364,623\$	 
	- Dev Set: 448,092\$	 
	- Test Set: 485,484\$  
- Inital learning rate = 0.001, Decay steps = 1000, Decay rate = 0.5:
	- Train Set: 382,125\$	 
	- Dev Set: 458,376\$	 
	- Test Set: 491,301\$  
- Inital learning rate = 0.001, Decay steps = 10000, Decay rate = 0.1:
	- Train Set: 351,941\$	 
	- Dev Set: 463,638\$	 
	- Test Set: 509,688\$  
- Inital learning rate = 0.001, Decay steps = 10000, Decay rate = 0.03:
	- Train Set: 366,959\$	 
	- Dev Set: 457,626\$	 
	- Test Set: 498,690\$  
- Inital learning rate = 0.001, Decay steps = 10000, Decay rate = 0.01:
	- Train Set: 379,849\$	 
	- Dev Set: 452,895\$	 
	- Test Set: 494,326\$  
- Inital learning rate = 0.001, Decay steps = 10000, Decay rate = 0.003:
	- Train Set: 382,460\$	 
	- Dev Set: 453,000\$	 
	- Test Set: 488,972\$  
- Inital learning rate = 0.003, Decay steps = 10000, Decay rate = 0.003:
	- Train Set: 391,493\$	 
	- Dev Set: 445,450\$	 
	- Test Set: 498,492\$  
- Inital learning rate = 0.003, Decay steps = 10000, Decay rate = 0.001:
	- Train Set: 391,728\$	 
	- Dev Set: 445,197\$	 
	- Test Set: 499,952\$  
- Inital learning rate = 0.003, Decay steps = 10000, Decay rate = 0.0003:
	- Train Set: 391,816\$	 
	- Dev Set: 445,650\$	 
	- Test Set: 499,486\$  
- Inital learning rate = 0.01, Decay steps = 1000, Decay rate = 0.5:
	- Train Set: 349,823\$	 
	- Dev Set: 463,792\$	 
	- Test Set: 510,400\$  
- Inital learning rate = 0.01, Decay steps = 10000, Decay rate = 0.1:
	- Train Set: 359,636\$	 
	- Dev Set: 459,602\$	 
	- Test Set: 509,302\$ 
- Inital learning rate = 0.01, Decay steps = 10000, Decay rate = 0.05:
	- Train Set: 328,232\$	 
	- Dev Set: 458,313\$	 
	- Test Set: 505,140\$   
- Inital learning rate = 0.01, Decay steps = 10000, Decay rate = 0.01:
	- Train Set: 336,955\$	 
	- Dev Set: 469,936\$	 
	- Test Set: 502,201\$   

None of these offered a major improvement over the static learning rate of 0.0001. The best outcome was with an initial learning rate of 0.0001 as used before and a decay rate of 0.75 over 10000 iterations  (dev error of 425,121\$ 
instead of 427,664\$).
This is the learning rate that was chosen. 
