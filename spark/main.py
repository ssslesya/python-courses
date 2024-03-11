from pyspark.sql import SparkSession

from get_product_category_pairs import get_product_category_pairs

# Запуск SparkSession
spark = SparkSession.builder.appName("Product Category").getOrCreate()

# Загрузка данных
products_df = spark.read.csv("products.csv", header=True)
categories_df = spark.read.csv("categories.csv", header=True)
product_category_df = spark.read.csv("product_category.csv", header=True)
# Импорт метода


# Вызов метода
result_df = get_product_category_pairs(products_df, categories_df, product_category_df)

# Сохранение результата
result_df.write.csv("output.csv", header=True)

# Остановка SparkSession
spark.stop()
