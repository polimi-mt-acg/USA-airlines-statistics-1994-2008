import sys
from datetime import datetime
from pathlib import Path
from pyspark.sql.types import IntegerType

def preprocess_data_sets(spark, data_sets, parquet_data_sets):    
    # This is going to take lot of time. Just wait.
    if not Path(parquet_data_sets).is_dir():
        start_time = datetime.now()
        print("*info*  Preprocessing started. Please wait..")
        sys.stdout.flush()
        
        # Read
        df = spark.read.csv(data_sets, inferSchema=True, header=True, sep=',').replace('NA', None)
        read_time = datetime.now()
        print("*info*  Data sets read.")
        sys.stdout.flush()

        # Casts
        df = df.withColumn('ArrDelay', df['ArrDelay'].cast(IntegerType()))
        df = df.withColumn('DepDelay', df['DepDelay'].cast(IntegerType()))
        df = df.withColumn('Distance', df['Distance'].cast(IntegerType()))
        cast_time = datetime.now()
        print("*info*  Casts completed.")
        sys.stdout.flush()
        
        # Write
        df.write.save(parquet_data_sets, format='parquet')
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
        print("Preprocessing NOT performed. Preprocessed data sets already exist.\n")