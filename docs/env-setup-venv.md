# Environment setup with Virtualenv

Dependencies assumed to be already installed:

- [Java], version 1.8 or higher
- [Python], version 3.5 or higher


## Project setup

To install dependencies and setup the project

- [1. Install Spark](#1-install-spark)
- [2. Install Python virtualenv](#2-install-python-virtualenv)
- [3. Create virtualenv](#3-create-virtualenv)
- [4. Install Python dependencies](#4-install-python-dependencies)
- [5. Download the RITA airlines dataset](#5-download-the-rita-airlines-dataset)


### 1. Install Spark

Download spark from the [Spark download page] by selecting the latest Spark release, the prebuilt package for Hadoop.

To download the (current) latest version:

```bash
$ cd ~/Downloads

$ wget http://www-eu.apache.org/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
```

Unzip and install it:

```bash
$ tar -xzf spark-2.3.1-bin-hadoop2.7.tgz

$ mv spark-2.3.1-bin-hadoop2.7 /opt/spark-2.3.1-bin-hadoop2.7

# create a symbolic link
$ ln -s /opt/spark-2.3.1-bin-hadoop2.7 /opt/spark
```

Add the following lines in your ~/.bashrc (or ~/.zshrc) file to export the path where to find Spark:

```
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH
```

Restart your shell to make the exports effective.


### 2. Install Python virtualenv

```bash
$ pip install virtualenv
```

### 3. Create virtualenv

Create a new virtual env. At the root of this repository:

```bash
$ python3 -m venv ./venv

# Export spark home variables into virtual env
$ echo 'export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH' >> ./venv/bin/activate

```

### 4. Install Python dependencies

```bash
# activate virtual env
$ source venv/bin/activate

# first upgrade pip
(venv) $ pip install --upgrade pip

(venv) $ pip install --upgrade -r requirements.txt

# deactivate virtual env
$ deactivate
```

### 5. Download the RITA airlines dataset

Please, look at the [download the RITA airlines dataset](dataset-download.md) guideline.


## Run

Activate virtualenv and run Jupiter Notebook

```bash
$ source venv/bin/activate

(venv) $ jupyter notebook .
```


### Sources

- <https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f>


[Java]: https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html
[Python]: https://www.python.org
[Spark downloads page]: http://spark.apache.org/downloads.html
