from pyspark import SapakContext
from pyspark.streaming import StreamingContext

sc = SapakContext("local[2]","Contagem")
ssc = StreamingContext(sc,10)

pesquisa = ssc.textFileStream("file:///home/cloudera/spark/")

contagem = pesquisa.flatMap(lambda palavra: palavra.split(" "))
contagem = contagem.map(lambda pal: (pal,1))
contagem = conta.reduceByKey(lambda a, b: a + b)

contagem.pprint()

ssc.start()
ssc.awaitTermination()