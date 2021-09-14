Important :

->df ; loads data from csv file
->lst ; copies record of all gold medal fields from df
->lsts ; copies data of all indian athletes from lst
->ls ; copies data of all females from lst
->data ; list store data and respective frequencies to plot the graph


Question and the approach to solve them

1. In how many cities Summer Olympics is held so far?

Ans: using len() and unique() function to display all the  unique city names and total them.


2.Which sport is having most number of Gold Medals so far? (Top 5)

Ans: Copying data of the sports in which gold medal was won by the players to a list and then counting the number of times the sport was repeated in the list and plotting graph


3.Which sport is having most number of medals so far? (Top 5)

Ans Directly counting the number of times sport was repeated from the csv file that is loaded into df and plotting graph


4. Which player has won most number of medals? (Top 5)

Ans Directly counting the number of times an athlete name was repeated from the csv file that is loaded into df and plotting bar graph


5. Which player has won most number Gold Medals of medals? (Top 5)

Ans Copying data of the sports in which gold medal was won by the players to a list and then counting the number of times an athlete namewas repeated in the list and plotting graph


6. In which year India won first Gold Medal in Summer Olympics?

Ans Copying data of the sports to a list in which gold medal was won by the players and their nationality was Indian and using min() function to display the smallest year from the list 


7.Which event is most popular in terms on number of players? (Top 5)

Ans Directly counting the number of times an event name was repeated from the csv file that is loaded into df and plotting bar graph


8. Which sport is having most female Gold Medalists?

Ans Copying data of the sports to a list in which gold medal was won by the players and the Gender was Female and plotting bar graph
