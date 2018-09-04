# Reports

Analytics performed:

1. The percentage of canceled flights per day, throughout the entire data set
2. Weekly percentages of delays that are due to weather, throughout the entire data set
3. The percentage of flights belonging to a given "distance group" that were able to halve their departure delays by the time they arrived at their destinations. Distance groups assort flights by their total distance in miles. Flights with distances that are less than 200 miles belong in group 1, flights with distances that are between 200 and 399 miles belong in group 2, flights with distances that are between 400 and 599 miles belong in group 3, and so on. The last group contains flights whose distances are between 2400 and 2599 miles.
	
	[03 Distance groups percentages halved delay.md](03-distance-groups-percentages-halved-delay.md)

4. A weekly "penalty" score for each airport that depends on both the its incoming and outgoing flights. The score adds 0.5 for each incoming flight that is more than 15 minutes late, and 1 for each outgoing flight that is more than 15 minutes late.
5. Also provide an additional data analysis defined by your group.

The above linked reports are a graphical synthesized version of python notebooks present in the [../notebooks](../notebooks) folder.

---

For further details about the analytics and the date, please refer to the [repository main page](../).