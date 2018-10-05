##### NOTICE

> This reports has the goal to show **some of the results**. It was **not** possible to export **all the feasible combinations** of analytics performed because they were too many.
>
> Moreover, most of the parts of the notebook containing code have been omitted.
>
> Please, have a look at the notebook corresponding to this report ([notebooks](../notebooks) folder) and run it to perform any desired combination of the analytics.


# Airport weekly penalty for arrivals and departures delays 

In this notebook we compute a weekly "**penalty**" score for each airport that depends on both the its incoming and outgoing flights. The score adds `0.5` for each incoming flight that is more than _15 minutes_ late, and `1` for
each outgoing flight that is more than _15 minutes_ late.

Formally speaking, let _w = {1, 2, ..., 52}_ be the _week number_ in a year _y_ and _f_ be a flight _leaving from_ or _arriving to airport_ on week _w_ of year _year_. Then we compute the weekly penalties as the following:

![png](images/04-weekly-airport-penalty/00_01.png)

![png](images/04-weekly-airport-penalty/00_02.png)

![png](images/04-weekly-airport-penalty/00_03.png)


## Data Visualization

Analytics for airports weekly penalty are reported below.

### Missing values and valid data


```python
plot_missing_values_stacked_bar(df_missing)
```


![png](images/04-weekly-airport-penalty/40_0.png)


### Airports weekly penalty

A **line plot** is used to display penalties as a time series. On the `x` axis the week number is reported, while on the `y` axis we show the weekly penalty.

Moreover, a **bar plot** is chosen to display the *yearly average* weekly-penalty of a given airport.


```python
display(ui, out)
```

> Interactive widgets screenshot

![png](images/04-weekly-airport-penalty/widgets_screenshot.png)

> Since the produced charts would have been too many, they are dynamically generated in the notebook based on the parameters the user choose.
>
> The followings **some samples** of the notebook _dynamically generated charts_. Please, run the notebook to be able to select parameters of interest and so generate any chart.

![png](images/04-weekly-airport-penalty/airport-ABE.png)
![png](images/04-weekly-airport-penalty/airport-AEX.png)
![png](images/04-weekly-airport-penalty/airport-ATL.png)
![png](images/04-weekly-airport-penalty/airport-BGM.png)
![png](images/04-weekly-airport-penalty/airport-BOS.png)
![png](images/04-weekly-airport-penalty/airport-BUR.png)
![png](images/04-weekly-airport-penalty/airport-CHS.png)
![png](images/04-weekly-airport-penalty/airport-CMX.png)
![png](images/04-weekly-airport-penalty/airport-DAB.png)
![png](images/04-weekly-airport-penalty/airport-DRO.png)
![png](images/04-weekly-airport-penalty/airport-ERI.png)
![png](images/04-weekly-airport-penalty/airport-FCA.png)
![png](images/04-weekly-airport-penalty/airport-GEG.png)
![png](images/04-weekly-airport-penalty/airport-GSP.png)
![png](images/04-weekly-airport-penalty/airport-HNL.png)
![png](images/04-weekly-airport-penalty/airport-IDA.png)
![png](images/04-weekly-airport-penalty/airport-ITO.png)
![png](images/04-weekly-airport-penalty/airport-LAN.png)
![png](images/04-weekly-airport-penalty/airport-LIH.png)
![png](images/04-weekly-airport-penalty/airport-MAF.png)
![png](images/04-weekly-airport-penalty/airport-MFE.png)
![png](images/04-weekly-airport-penalty/airport-MLI.png)
![png](images/04-weekly-airport-penalty/airport-MSY.png)
![png](images/04-weekly-airport-penalty/airport-OME.png)
![png](images/04-weekly-airport-penalty/airport-PFN.png)
![png](images/04-weekly-airport-penalty/airport-PMD.png)
![png](images/04-weekly-airport-penalty/airport-RAP.png)
![png](images/04-weekly-airport-penalty/airport-ROA.png)
![png](images/04-weekly-airport-penalty/airport-SBP.png)
![png](images/04-weekly-airport-penalty/airport-SJC.png)
![png](images/04-weekly-airport-penalty/airport-SPN.png)
![png](images/04-weekly-airport-penalty/airport-TEX.png)
![png](images/04-weekly-airport-penalty/airport-TWF.png)
