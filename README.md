# NHL Contract Estimator - NHLContractEST

The purpose of this project is to create a salary predictor for NHL contract values. Because of the salary cap structure of the NHL, player salaries are a huge part of team success.
When a team signs a player to a contract, many factors go into the value of that contract. These factors represent how effective the player is and how effective he is projected 
to be for the duration of the contract. This problem can be represented by a simple machine learning representation. In this case, the player's statistics are used as input features. 
This represents as much information about the player as possible (age, position, individual statistics from previous years, team statistics from previous years, etc.). 
Additionally, the length of the contract is also passed in as a feature. This will also determine the salary of the player for the duration of his contract. 

The project is set up with the following files: 
* NHLContractEST: 
This is the main high-level script that runs the project

* UI: 
This houses the necessary functions to present the console UI and give the user the option to fetch required data from the internet or from stored files. This will also give the user the option to store the retrieved data into a file.

* GetData: This contains the functions required to retrieve the necessary information from different websites (namely CapFriendly and ESPN). The data is returned as lists of classes. 

* ContractStructure: This will convert the various information contained in the lists returned by GetData into a single list of contract entries. These contract entries represent all contracts that will be used as inputs to the model. The number of contract entries will correspond to "m", the number of examples used by the training model.

* FormatData: This will take the contract entries created in ContractStructure and convert them into "n" x 1 feature vectors where "n" is the number of features to be used by the training model. The contract list will be formatted into an "n" x "m" matrix X that will correspond to the training and cross-validation sets used by the model. The contract salaries will be converted to a 1 x "m" vector Y. 

* Util: This houses various small utility functions such as file IO, feature plotting,  etc. 
