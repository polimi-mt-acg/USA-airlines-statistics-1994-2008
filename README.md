# USA Airlines - Data Analytics
The goal of the project is to infer qualitative data regarding USA flights during the years 1994-2008. The data can be downloaded from [stat-computing.org](http://stat-computing.org/dataexpo/2009/the-data.html).

We address the problem exploiting [Spark](https://spark.apache.org/docs/2.3.1/index.html) framework to manage the high volume of the available data. To display our analysis in an effective way, we make use of [Jupyter Notebooks](https://jupyter.org/index.html), enabling us to show the flow of data transformations to extract our analytics, together with the data visualization.

## Dependencies
The following list of packages is assumed to be installed on your machine:
 - Java, version 1.8
 - [Apache Spark](https://spark.apache.org/), any version supporting Spark Dataframes
 - [Conda](https://conda.io/docs/), any version

## Setup
Data analytics are provided as Jupyter Notebooks running Python 3 kernels.

To successfully run them, a script to set up the dependencies is available, making the following steps:
 - download the [RITA airlines dataset](http://stat-computing.org/dataexpo/2009/the-data.html) from 1994 to 2008
 - create a `conda` environment named `bd-mt-project`
 - install Python dependencies
 - install the Jupyter Lab extensions
 
```bash
chmod -R +x script
script/setup.sh
```

## Run
To run the Jupyter Notebooks, load the `conda` environment.

```bash
source activate bd-mt-project
```

Then launch Jupyter Lab

```bash
jupyter-lab .
```

or Jupyer Notebook

```bash
jupyter notebook .
```