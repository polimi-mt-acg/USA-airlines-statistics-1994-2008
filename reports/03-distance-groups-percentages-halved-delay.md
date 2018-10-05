
# Percentages of flights belonging to a distance group that halved a delay

In this notebook we compute the percentage of flights belonging to a given "distance group" that were able to halve their departure delays by the time they arrived at their destinations. Distance groups assort flights by their total distance in miles. Flights with distances that are less than 200 miles belong in group 1, flights with distances that are between 200 and 399 miles belong in group 2, flights with distances that are between 400 and 599 miles belong in group 3, and so on. The last group contains flights whose distances are between 2400 and 2599 miles.


So basically:

- By the _Distance_ attribute we can infer the flight group:

![png](images/03-distance-groups-percentages-halved-delay/00_01.png)

- For each flight we can say if it has halved or not its delay:

![png](images/03-distance-groups-percentages-halved-delay/00_02.png)


- So, for each flight group we can create two sets of flight: those that have halved their delays and the others

### Assumptions

- The last group, as the assignment states, is group ( 2599 // 200 ) + 1 = 13
- Each flight not belonging to a valid group is not considered

# Data visualization

## Data exluded from visualization

### Missing values

The following chart show the percentage of dropped rows due to missing values.


```python
show_missing_pie_chart()
```


![png](images/03-distance-groups-percentages-halved-delay/31_0.png)


## Invalid group value

The following chart show the percentage of dropped rows due to group value exceeding the last valid group (13).


```python
show_group_invalid_pie_chart()
```


![png](images/03-distance-groups-percentages-halved-delay/33_0.png)


### Summary of excluded data

The following chart show the summary of dropped rows


```python
show_dropped_summary_pie_chart()
```

![png](images/03-distance-groups-percentages-halved-delay/35_0.png)


## Percentages of flights belonging to a distance group that halved a delay

### Delay per group

The following chart show the percentage of halved delay per group

![png](images/03-distance-groups-percentages-halved-delay/40_01.png)
![png](images/03-distance-groups-percentages-halved-delay/40_02.png)
![png](images/03-distance-groups-percentages-halved-delay/40_03.png)
![png](images/03-distance-groups-percentages-halved-delay/40_04.png)
![png](images/03-distance-groups-percentages-halved-delay/40_05.png)
![png](images/03-distance-groups-percentages-halved-delay/40_06.png)
![png](images/03-distance-groups-percentages-halved-delay/40_07.png)
![png](images/03-distance-groups-percentages-halved-delay/40_08.png)
![png](images/03-distance-groups-percentages-halved-delay/40_09.png)
![png](images/03-distance-groups-percentages-halved-delay/40_10.png)
![png](images/03-distance-groups-percentages-halved-delay/40_11.png)
![png](images/03-distance-groups-percentages-halved-delay/40_12.png)
![png](images/03-distance-groups-percentages-halved-delay/40_13.png)


## Comparison of halved delay percentages

The following stack bar chart compares the percentages of halved delay for all groups


```python
show_percetages_comparison_horizontal_stack_chart()
```


![png](images/03-distance-groups-percentages-halved-delay/40_0.png)

