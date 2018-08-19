# Environment setup

To completely setup environment for the first time:

### 1. Install PySpark

Before installing PySpark, you must have Python and Spark installed.

To install Spark, make sure you have [Java 8 or higher installed] on your computer. Then, visit the [Spark downloads page]. Select the latest Spark release, a prebuilt package for Hadoop, and download it directly.

To download the (current) latest version:

```bash
$ cd ~/Downloads

$ wget http://www-eu.apache.org/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
```

Unzip it and move it to your /opt folder:

```bash
$ tar -xzf spark-2.3.1-bin-hadoop2.7.tgz

$ mv spark-2.3.1-bin-hadoop2.7 /opt/spark-2.3.1-bin-hadoop2.7
```

Create a symbolic link:

```bash
$ ln -s /opt/spark-2.3.1-bin-hadoop2.7 /opt/spark
```

This way, you will be able to download and use multiple Spark versions.

Finally, tell your bash (or zsh, etc.) where to find Spark. To do so, configure your $PATH variables by adding the following lines in your ~/.bashrc (or ~/.zshrc) file:

```
export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH
```

Restart your shell to make the exports effective.

### 2. Create virtual env

Be sure to have [Python] 3 installed.

Create a new virtual env. At the root of this repository:

```bash
$ python3 -m venv ./venv

# Export spark home variables within virtual env
$ echo 'export SPARK_HOME=/opt/spark
export PATH=$SPARK_HOME/bin:$PATH' >> ./venv/bin/activate
```

### 3. Install dependencies

Activate virtual env

```bash
$ source venv/bin/activate
```

Install dependencies into activated virtualenv

```bash
(venv) $ pip install --upgrade -r requirements.txt
```

# Usual operations

- **Activate virtual env and launch Jupyter notebook**

```bash
$ source venv/bin/activate

(venv) $ jupyter notebook
```

- **Deactivate virtual env**

```bash
(venv) $ deactivate
```


### Sources

- <https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f>

[Python]: https://www.python.org
[Java 8 or higher installed]: https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html
[Spark downloads page]: http://spark.apache.org/downloads.html