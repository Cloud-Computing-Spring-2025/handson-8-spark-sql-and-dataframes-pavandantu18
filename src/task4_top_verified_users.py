from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

spark = SparkSession.builder.appName("TopVerifiedUsers").getOrCreate()

# Load datasets
posts_df = spark.read.option("header", True).csv("input/posts.csv", inferSchema=True)
users_df = spark.read.option("header", True).csv("input/users.csv", inferSchema=True)

# Filter verified users
verified_users_df = users_df.filter(col("Verified") == True)

# Join posts with verified users
verified_posts_df = posts_df.join(verified_users_df, "UserID")

# Calculate reach (Likes + Retweets)
verified_posts_df = verified_posts_df.withColumn("Reach", col("Likes") + col("Retweets"))

# Aggregate total reach per verified user (grouped by Username)
user_reach = verified_posts_df.groupBy("Username") \
    .agg(_sum("Reach").alias("TotalReach"))

# Select top 5 verified users by total reach
top_verified = user_reach.orderBy(col("TotalReach").desc()).limit(5)

# Save result
top_verified.coalesce(1).write.mode("overwrite").csv("outputs/top_verified_users.csv", header=True)
