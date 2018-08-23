import sys
from datetime import datetime
from pathlib import Path
from pyspark.sql.types import IntegerType

# default datasets paths
DATASET_SOURCE='../dataset/*.csv.bz2'
DATASET_TARGET='../dataset/preprocessed_dataset.parquet'

# default DEV datasets paths
year = 1994
DATASET_SOURCE_DEV='../dataset/{}.csv.bz2'.format(year)
DATASET_TARGET_DEV='../dataset/preprocessed_dataset_{}.parquet'.format(year)


def perform_dataset_preprocessing(spark, dataset_source=DATASET_SOURCE, dataset_target=DATASET_TARGET):
    """
    By invoking: perform_dataset_preprocessing(spark_instance) the preprocessing with the default paths
    will be performed.
    """
    print("Starting preprocessing of {}".format(dataset_source))

    # This is going to take lot of time. Just wait.
    if not Path(dataset_target).is_dir():
        start_time = datetime.now()
        print("*info*  Preprocessing started. Please wait..")
        sys.stdout.flush()
        
        # Read
        df = spark.read.csv(dataset_source, inferSchema=True, header=True, sep=',').replace('NA', None)
        read_time = datetime.now()
        print("*info*  Dataset read.")
        sys.stdout.flush()

        # Casts
        df = df.withColumn('ArrDelay', df['ArrDelay'].cast(IntegerType()))
        df = df.withColumn('DepDelay', df['DepDelay'].cast(IntegerType()))
        df = df.withColumn('Distance', df['Distance'].cast(IntegerType()))
        cast_time = datetime.now()
        print("*info*  Casts completed.")
        sys.stdout.flush()
        
        # Write
        df.write.save(dataset_target, format='parquet')
        write_time = datetime.now()
        print("*info*  Write completed.")
        sys.stdout.flush()

        end_time = datetime.now()
        out = """
Preprocessing completed.

Elapsed time:
    READ:   {}
    CASTS:  {}
    WRITE:  {}

    TOTAL:  {}

        """.format(read_time-start_time,
                  cast_time-read_time,
                  write_time-cast_time,
                  end_time-start_time)
        print(out)
    else:
        print("Preprocessing NOT performed.\nPreprocessed dataset already exists: {}\n".format(dataset_target))


def load_preprocessed_dataset(spark, dataset=DATASET_TARGET):
    """
    Load the preprocessed dataset with spark.
    :return: :class`DataFrame`
    """
    print("Peprocessed dataset loaded.")
    print(dataset)
    return spark.read.load(dataset)


def perform_DEV_dataset_preprocessing(spark, dataset_source=DATASET_SOURCE_DEV, dataset_target=DATASET_TARGET_DEV):
    """
    Perform preprocessing of the development dataset
    """
    print("--------- DEV mode ON ---------")
    return perform_dataset_preprocessing(spark, dataset_source, dataset_target)


def load_DEV_preprocessed_dataset(spark, dataset=DATASET_TARGET_DEV):
    """
    Load the development preprocessed dataset with spark.
    :return: :class`DataFrame`
    """
    print("--------- DEV mode ON ---------")
    return load_preprocessed_dataset(spark, dataset)