# USA-airlines-statistics-1994-2008
*Big data analytics performed with Spark and Hadoop on RITA airlines dataset (1.3 GB)*

## Project assignment

The goal of the project is to infer qualitative data regarding USA flights during the years 1994-2008. The data can be downloaded from [stat-computing.org].

Using both [Hadoop] and [Spark] provide the following information:

1. The percentage of canceled flights per day, throughout the entire data set
2. Weekly percentages of delays that are due to weather, throughout the entire data set
3. The percentage of flights belonging to a given "distance group" that were able to halve their departure delays by the time they arrived at their destinations. Distance groups assort flights by their total distance in miles. Flights with distances that are less than 200 miles belong in group 1, flights with distances that are between 200 and 399 miles belong in group 2, flights with distances that are between 400 and 599 miles belong in group 3, and so on. The last group contains flights whose distances are between 2400 and 2599 miles.
4. A weekly "penalty" score for each airport that depends on both the its incoming and outgoing flights. The score adds 0.5 for each incoming flight that is more than 15 minutes late, and 1 for each outgoing flight that is more than 15 minutes late.
5. Also provide an additional data analysis defined by your group.

Use charts to present the information that you have extracted from the data sets.


## Our solution

We address the problem exploiting [Spark] framework to manage the high volume of the available data. To display our analysis in an effective way, we make use of [Jupyter Notebooks], enabling us to show the flow of data transformations to extract our analytics, together with the data visualization.


## Reports

Checkout the [reports](reports) to look at the performed analytics.


## Documentation

Checkout the [documentation](docs) to initialize and run this analytics.

## Project context

This project has been developed for the [Middleware Technologies for Distributed Systems course]
(A.Y. 2017/2018) at [Politecnico di Milano]. Look at the [polimi-mt-acg] page for other projects.


[stat-computing.org]: http://stat-computing.org/dataexpo/2009/the-data.html
[Hadoop]: http://hadoop.apache.org/
[Spark]: https://spark.apache.org/docs/2.3.1/index.html
[Jupyter Notebooks]: https://jupyter.org
[Middleware Technologies for Distributed Systems course]: https://www4.ceda.polimi.it/manifesti/manifesti/controller/ManifestoPublic.do?EVN_DETTAGLIO_RIGA_MANIFESTO=evento&aa=2017&k_cf=225&k_corso_la=481&k_indir=T2A&codDescr=090931&lang=EN&semestre=1&idGruppo=3589&idRiga=216904
[Politecnico di Milano]: https://www.polimi.it
[polimi-mt-acg]: https://github.com/polimi-mt-acg

