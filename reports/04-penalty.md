
# Airport weekly penalty for arrivals and departures delays 

In this notebook we are computing a weekly "**penalty**" score for each airport that depends on both the its incoming and outgoing
flights. The score adds `0.5` for each incoming flight that is more than _15 minutes_ late, and `1` for
each outgoing flight that is more than _15 minutes_ late.

Formally speaking, let _w = {1, 2, ..., 52}_ be the _week number_ in a year _y_ and _f_ be a flight _leaving from_ or _arriving to airport_ on week _w_ of year _year_. Then we compute the weekly penalties as the following:

![png](images/04-penalty/00_01.png)

![png](images/04-penalty/00_02.png)

![png](images/04-penalty/00_03.png)

# Data Visualization

Analytics for airports weekly penalty are reported below.

A **line plot** is used to display penalties as a time series. On the `x` axis the week number is reported, while on the `y` axis we show the weekly penalty.

Moreover, a **bar plot** is chosen to display the *yearly average* weekly-penalty of a given airport.

> Since the produced charts would have been too many, they are dynamically generated in the notebook through the parameters chosen by the user.
>
> The followings **are samples** of the notebook _dynamically_ generated charts. Please, run the notebook to be able to select parameters of interest and so generate any chart.

![png](images/04-penalty/airport-ABE.png)
![png](images/04-penalty/airport-AEX.png)
![png](images/04-penalty/airport-ATL.png)
![png](images/04-penalty/airport-BGM.png)
![png](images/04-penalty/airport-BOS.png)
![png](images/04-penalty/airport-BUR.png)
![png](images/04-penalty/airport-CHS.png)
![png](images/04-penalty/airport-CMX.png)
![png](images/04-penalty/airport-DAB.png)
![png](images/04-penalty/airport-DRO.png)
![png](images/04-penalty/airport-ERI.png)
![png](images/04-penalty/airport-FCA.png)
![png](images/04-penalty/airport-GEG.png)
![png](images/04-penalty/airport-GSP.png)
![png](images/04-penalty/airport-HNL.png)
![png](images/04-penalty/airport-IDA.png)
![png](images/04-penalty/airport-ITO.png)
![png](images/04-penalty/airport-LAN.png)
![png](images/04-penalty/airport-LIH.png)
![png](images/04-penalty/airport-MAF.png)
![png](images/04-penalty/airport-MFE.png)
![png](images/04-penalty/airport-MLI.png)
![png](images/04-penalty/airport-MSY.png)
![png](images/04-penalty/airport-OME.png)
![png](images/04-penalty/airport-PFN.png)
![png](images/04-penalty/airport-PMD.png)
![png](images/04-penalty/airport-RAP.png)
![png](images/04-penalty/airport-ROA.png)
![png](images/04-penalty/airport-SBP.png)
![png](images/04-penalty/airport-SJC.png)
![png](images/04-penalty/airport-SPN.png)
![png](images/04-penalty/airport-TEX.png)
![png](images/04-penalty/airport-TWF.png)
