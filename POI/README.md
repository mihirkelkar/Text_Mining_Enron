First I wrote data sorter .py file. 

I read all the enron data that I downloaded from Kaggle. 
This data set had a field where poi indicated True or False. 

Inorder to truly focus the attention of the ML Algorithm on the text data, I decided to rid the data from very obvious financialdiscrepencies. 
So I made plots:
Then I made a 3D Plot of Salaries vs Bonuses vs Stocks Options
I found one obvious outlier. Duh !

Then to narraow down the process, I made more granular plots. 
I sorted the data, removed the top four outliers based on the sum of their salary stocks and bonus and plotted the rest to see if I have a fairly equal distribution for the purpose of the experiment. I did. The plots are Enron Salaries, No outliers and its 3d variant. 

Next I decided to see the relation between these email messages. Now emails in the corpus were exchaged between POIs and NonPOIs as well. Extending the colloquial concept of Guilt by association, I decided to plot a graph to see what extent of interaction with POIs definitely make you a POI or vice-versa
The graph was plotted. 
I could not see any clear co-realtion, but I definetely saw that sending an Email to the POI is more likely to make you guilty than recieveing an email from one. 

Now, that I have no clear picture of which attributes are affecting the scenario the most. I decided to train a decisoion stump and see which attributes splits it the most.

Then I went ahead and decided to build a decision tree to see what attributes it splits on. I found the top 15 attributes using the script enron features select.py

Once , the top 15 were found. I selected the top 10 and calculated accuracy. Eventually I iterated through various combinations of the top 10 to settle on the following 
1 feature salary (0.384177639216)
2 feature bonus (0.262187377894)
3 feature email_from_poi (0.166033962301)
4 feature email_to_poi (0.0688098248149)
5 feature deferral_payments (0.0642225031606)
6 feature total_payments (0.0545686926131). 

Now I will calculate the accuracy based on only the above 6 features. [script : top_six_dec_tree.py] : The accuracy jumped to 86%

Then I removed bonus from the picture to see how well the from_poi_email and to_poi_email can perform with only one significant financial attribute. 

Without a bonus, the accuracy drops to 73%

Without a salarym the accuracy drops to 77%. 

Now lets try without both, the accuracy drops further to about 68% which is still better than the baseline accuracy of 33% since 1 / 3rd of the people in the corpus were charged. 

Now lets try the same clasification using naive bayes. However, with naive bayes and all features, the accuaracy dropped even below a random picking threshold.

Now, lets just tune and scale the decision Tree algorithm. Descrube what parameter tuning and GRIDcv is. The script is tuned_decision_tree
After the tuning process, the accuracy jumped to 86%. 

Add a k fold cross validation to the picture and the accuracy jumps to 87. 
