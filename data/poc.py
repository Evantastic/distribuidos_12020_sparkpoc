from pyspark import SparkContext, SparkConf

conf = SparkConf().setAppName("Spark Count")
sc = SparkContext(conf=conf)

# the first step involves reading the source text file from HDFS 
text_file = sc.textFile("/tmp/data/quijote.txt")

# this step involves the actual computation for reading the number of words in the file
# flatmap, map and reduceByKey are all spark RDD functions
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

# the final step is just saving the result.
counts.saveAsTextFile("/tmp/data/resultado")
