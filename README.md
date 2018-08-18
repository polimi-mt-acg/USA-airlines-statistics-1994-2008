# USA-airlines-statistics-1994-2008

## Project assignment

The goal of the project is to infer qualitative data regarding USA flights during the years
1994-2008. The data can be downloaded from <http://stat-computing.org/dataexpo/2009/the-data.html>.

**Variables descriptions**

|     | Name              | Description                                                               |
| --- | ----------------- | ------------------------------------------------------------------------- |
| 1   | Year              | 1987-2008                                                                 |
| 2   | Month             | 1-12                                                                      |
| 3   | DayofMonth        | 1-31                                                                      |
| 4   | DayOfWeek         | 1 (Monday) - 7 (Sunday)                                                   |
| 5   | DepTime           | actual departure time (local, hhmm)                                       |
| 6   | CRSDepTime        | scheduled departure time (local, hhmm)                                    |
| 7   | ArrTime           | actual arrival time (local, hhmm)                                         |
| 8   | CRSArrTime        | scheduled arrival time (local, hhmm)                                      |
| 9   | UniqueCarrier     | unique carrier code                                                       |
| 10  | FlightNum         | flight number                                                             |
| 11  | TailNum           | plane tail number                                                         |
| 12  | ActualElapsedTime | in minutes                                                                |
| 13  | CRSElapsedTime    | in minutes                                                                |
| 14  | AirTime           | in minutes                                                                |
| 15  | ArrDelay          | arrival delay, in minutes                                                 |
| 16  | DepDelay          | departure delay, in minutes                                               |
| 17  | Origin            | origin IATA airport code                                                  |
| 18  | Dest              | destination IATA airport code                                             |
| 19  | Distance          | in miles                                                                  |
| 20  | TaxiIn            | taxi in time, in minutes                                                  |
| 21  | TaxiOut           | taxi out time in minutes                                                  |
| 22  | Cancelled         | was the flight cancelled?                                                 |
| 23  | CancellationCode  | reason for cancellation (A = carrier, B = weather, C = NAS, D = security) |
| 24  | Diverted          | 1 = yes, 0 = no                                                           |
| 25  | CarrierDelay      | in minutes                                                                |
| 26  | WeatherDelay      | in minutes                                                                |
| 27  | NASDelay          | in minutes                                                                |
| 28  | SecurityDelay     | in minutes                                                                |
| 29  | LateAircraftDelay | in minutes                                                                |


Using both [Hadoop] and [Spark] provide the following information:

1. The percentage of canceled flights per day, throughout the entire data set
2. Weekly percentages of delays that are due to weather, throughout the entire data set
3. The percentage of flights belonging to a given "distance group" that were able to halve their departure delays by the time they arrived at their destinations. Distance groups assort flights by their total distance in miles. Flights with distances that are less than 200 miles belong in group 1, flights with distances that are between 200 and 399 miles belong in group 2, flights with distances that are between 400 and 599 miles belong in group 3, and so on. The last group contains flights whose distances are between 2400 and 2599 miles.
4. A weekly "penalty" score for each airport that depends on both the its incoming and outgoing flights. The score adds 0.5 for each incoming flight that is more than 15 minutes late, and 1 for each outgoing flight that is more than 15 minutes late.
5. Also provide an additional data analysis defined by your group.

Use charts to present the information that you have extracted from the data sets.

## Documentation

Checkout the [documentation](docs) to initialize and run this analytics.

## Project context

This project has been developed for the [Middleware Technologies for Distributed Systems course]
(A.Y. 2017/2018) at [Politecnico di Milano].

[Hadoop]: http://hadoop.apache.org/
[Spark]: https://spark.apache.org/
[Middleware Technologies for Distributed Systems course]: https://www4.ceda.polimi.it/manifesti/manifesti/controller/ManifestoPublic.do?EVN_DETTAGLIO_RIGA_MANIFESTO=evento&aa=2017&k_cf=225&k_corso_la=481&k_indir=T2A&codDescr=090931&lang=IT&semestre=1&idGruppo=3589&idRiga=216904
[Politecnico di Milano]: https://www.polimi.it