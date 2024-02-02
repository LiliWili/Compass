from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType


spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()

df_nomes = df_nomes.withColumn("Escolaridade", (F.rand() * 3).cast("int")).withColumn(
    "Escolaridade",
    F.when(F.col("Escolaridade") == 0, "Fundamental")
    .when(F.col("Escolaridade") == 1, "Medio")
    .when(F.col("Escolaridade") == 2, "Superior")
)


paises = ["Guiana", "Paraguai", "Colômbia", "Suriname", "Bolívia", "Venezuela", "Argentina", "Equador", "Uruguai", "Brasil", "Guiana Francesa", "Chile", "Peru"]
df_nomes = df_nomes.withColumn("Pais", 
                               F.when(F.rand() <= (1/len(paises)), F.lit(paises[0]))
                              .when(F.rand() <= (2/len(paises)), F.lit(paises[1]))
                              .when(F.rand() <= (3/len(paises)), F.lit(paises[2]))
                              .when(F.rand() <= (4/len(paises)), F.lit(paises[3]))
                              .when(F.rand() <= (5/len(paises)), F.lit(paises[4]))
                              .when(F.rand() <= (6/len(paises)), F.lit(paises[5]))
                              .when(F.rand() <= (7/len(paises)), F.lit(paises[6]))
                              .when(F.rand() <= (8/len(paises)), F.lit(paises[7]))
                              .when(F.rand() <= (9/len(paises)), F.lit(paises[8]))
                              .when(F.rand() <= (10/len(paises)), F.lit(paises[9]))
                              .when(F.rand() <= (11/len(paises)), F.lit(paises[10]))
                              .when(F.rand() <= (12/len(paises)), F.lit(paises[11]))
                              .otherwise(F.lit(paises[12])))

df_nomes = df_nomes.withColumn("AnoNascimento", (1945 + (F.rand() * (2023 - 1945))).cast(IntegerType()))

df_select = df_nomes.select("*").filter(df_nomes.AnoNascimento >= 2000)

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")


millennials = df_nomes.filter("AnoNascimento BETWEEN 1980 AND 1994").select("*").count()
print("Número de pessoas da geração Millennials:", millennials)


millennials_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0][0]
print("Número de pessoas da geração Millennials:", millennials_sql)



paises_geracoes = spark.sql("""
    SELECT Pais,
       CASE
           WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
           WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geracao X'
           WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
           WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geracao Z'
       END AS Geracao,
       COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao;
""")
paises_geracoes.show()
