from pyspark.sql import SparkSession

# Inisialisasi SparkSession dengan Hive support dan lokasi warehouse yang aman
spark = SparkSession.builder \
    .appName("Load Review Data to Hive") \
    .config("spark.sql.warehouse.dir", "/opt/bitnami/spark/warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

print("=== Membaca CSV pertama ===")
df1 = spark.read.option("header", "true").csv("/app/cleansed_review_rating.csv")
df1.show(5)
df1.write.mode("overwrite").saveAsTable("cleansed_review_rating")
print("=== Tabel 'cleansed_review_rating' berhasil ditulis ===")

print("=== Membaca CSV kedua ===")
df2 = spark.read.option("header", "true").csv("/app/review_summary_by_sentiment.csv")
df2.show(5)
df2.write.mode("overwrite").saveAsTable("review_summary_by_sentiment")
print("=== Tabel 'review_summary_by_sentiment' berhasil ditulis ===")

spark.stop()
