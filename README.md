# handson-08-sparkSQL-dataframes-social-media-sentiment-analysis

## **Prerequisites**

Before starting the assignment, ensure you have the following software installed and properly configured on your machine:

1. **Python 3.x**:
   - [Download and Install Python](https://www.python.org/downloads/)
   - Verify installation:
     ```bash
     python3 --version
     ```

2. **PySpark**:
   - Install using `pip`:
     ```bash
     pip install pyspark
     ```

3. **Apache Spark**:
   - Ensure Spark is installed. You can download it from the [Apache Spark Downloads](https://spark.apache.org/downloads.html) page.
   - Verify installation by running:
     ```bash
     spark-submit --version
     ```

4. **Docker & Docker Compose** (Optional):
   - If you prefer using Docker for setting up Spark, ensure Docker and Docker Compose are installed.
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## **Setup Instructions**

### **1. Project Structure**

Ensure your project directory follows the structure below:

```
SocialMediaSentimentAnalysis/
├── input/
│   ├── posts.csv
│   └── users.csv
├── outputs/
│   ├── hashtag_trends.csv
│   ├── engagement_by_age.csv
│   ├── sentiment_engagement.csv
│   └── top_verified_users.csv
├── src/
│   ├── task1_hashtag_trends.py
│   ├── task2_engagement_by_age.py
│   ├── task3_sentiment_vs_engagement.py
│   └── task4_top_verified_users.py
├── docker-compose.yml
└── README.md
```



- **input/**: Contains the input datasets (`posts.csv` and `users.csv`)  
- **outputs/**: Directory where the results of each task will be saved.
- **src/**: Contains the individual Python scripts for each task.
- **docker-compose.yml**: Docker Compose configuration file to set up Spark.
- **README.md**: Assignment instructions and guidelines.

### **2. Running the Analysis Tasks**

You can run the analysis tasks either locally or using Docker.

#### **a. Running Locally**

1. **Navigate to the Project Directory**:
   ```bash
   cd SocialMediaSentimentAnalysis/
   ```

2. **Execute Each Task Using `spark-submit`**:
   ```bash
 
     spark-submit src/task1_hashtag_trends.py
     spark-submit src/task2_engagement_by_age.py
     spark-submit src/task3_sentiment_vs_engagement.py
     spark-submit src/task4_top_verified_users.py
     
   ```

3. **Verify the Outputs**:
   Check the `outputs/` directory for the resulting files:
   ```bash
   ls outputs/
   ```

#### **b. Running with Docker (Optional)**

1. **Start the Spark Cluster**:
   ```bash
   docker-compose up -d
   ```

2. **Access the Spark Master Container**:
   ```bash
   docker cp input my-spark-master:/opt/bitnami/spark
   docker cp src my-spark-master:/opt/bitnami/spark
   docker exec -it my-spark-master bash  
   ```

3. **Navigate to the Spark Directory**:
   ```bash
   cd /opt/bitnami/spark/
   ```

4. **Run Your PySpark Scripts Using `spark-submit`**:
   ```bash
   
   spark-submit src/task1_hashtag_trends.py
   spark-submit src/task2_engagement_by_age.py
   spark-submit src/task3_sentiment_vs_engagement.py
   spark-submit src/task4_top_verified_users.py
   ```

5. **Exit the Container**:
   ```bash
   exit
   docker cp my-spark-master:/opt/bitnami/spark/outputs/hashtag_trends.csv /outputs
   docker cp my-spark-master:/opt/bitnami/spark/outputs/engagement_by_age.csv /outputs   
   docker cp my-spark-master:/opt/bitnami/spark/outputs/sentiment_engagement.csv /outputs 
   docker cp my-spark-master:/opt/bitnami/spark/outputs/top_verified_users.csv /outputs 
   ```

6. **Verify the Outputs**:
   On your host machine, check the `outputs/` directory for the resulting files.

7. **Stop the Spark Cluster**:
   ```bash
   docker-compose down
   ```

## **Overview**

In this assignment, you will leverage Spark Structured APIs to analyze a dataset containing employee information from various departments within an organization. Your goal is to extract meaningful insights related to employee satisfaction, engagement, concerns, and job titles. This exercise is designed to enhance your data manipulation and analytical skills using Spark's powerful APIs.

## **Objectives**

By the end of this assignment, you should be able to:

1. **Data Loading and Preparation**: Import and preprocess data using Spark Structured APIs.
2. **Data Analysis**: Perform complex queries and transformations to address specific business questions.
3. **Insight Generation**: Derive actionable insights from the analyzed data.

## **Dataset**

## **Dataset: posts.csv **

You will work with a dataset containing information about **100+ users** who rated movies across various streaming platforms. The dataset includes the following columns:

| Column Name     | Type    | Description                                           |
|-----------------|---------|-------------------------------------------------------|
| PostID          | Integer | Unique ID for the post                                |
| UserID          | Integer | ID of the user who posted                             |
| Content         | String  | Text content of the post                              |
| Timestamp       | String  | Date and time the post was made                       |
| Likes           | Integer | Number of likes on the post                           |
| Retweets        | Integer | Number of shares/retweets                             |
| Hashtags        | String  | Comma-separated hashtags used in the post             |
| SentimentScore  | Float   | Sentiment score (-1 to 1, where -1 is most negative)  |


---

## **Dataset: users.csv **
| Column Name | Type    | Description                          |
|-------------|---------|--------------------------------------|
| UserID      | Integer | Unique user ID                       |
| Username    | String  | User's handle                        |
| AgeGroup    | String  | Age category (Teen, Adult, Senior)   |
| Country     | String  | Country of residence                 |
| Verified    | Boolean | Whether the account is verified      |

---

### **Sample Data**

Below is a snippet of the `posts.csv`,`users.csv` to illustrate the data structure. Ensure your dataset contains at least 100 records for meaningful analysis.

```
PostID,UserID,Content,Timestamp,Likes,Retweets,Hashtags,SentimentScore
101,1,"Loving the new update! #tech #innovation","2023-10-05 14:20:00",120,45,"#tech,#innovation",0.8
102,2,"This app keeps crashing. Frustrating! #fail","2023-10-05 15:00:00",5,1,"#fail",-0.7
103,3,"Just another day... #mood","2023-10-05 16:30:00",15,3,"#mood",0.0
104,4,"Absolutely love the UX! #design #cleanUI","2023-10-06 09:10:00",75,20,"#design,#cleanUI",0.6
105,5,"Worst experience ever. Fix it. #bug","2023-10-06 10:45:00",2,0,"#bug",-0.9
```

---

```
UserID,Username,AgeGroup,Country,Verified
1,@techie42,Adult,US,True
2,@critic99,Senior,UK,False
3,@daily_vibes,Teen,India,False
4,@designer_dan,Adult,Canada,True
5,@rage_user,Adult,US,False
```

---



## **Assignment Tasks**

You are required to complete the following three analysis tasks using Spark Structured APIs. Ensure that your analysis is well-documented, with clear explanations and any relevant visualizations or summaries.

### **1. Hashtag Trends **

**Objective:**

Identify trending hashtags by analyzing their frequency of use across all posts.

**Tasks:**

- **Extract Hashtags**: Split the `Hashtags` column and flatten it into individual hashtag entries.
- **Count Frequency**: Count how often each hashtag appears.
- **Find Top Hashtags**: Identify the top 10 most frequently used hashtags.


**Expected Outcome:**  
A ranked list of the most-used hashtags and their frequencies.

**Example Output:**

| Hashtag     | Count |
|-------------|-------|
| #tech       | 120   |
| #mood       | 98    |
| #design     | 85    |

---

### **2. Engagement by Age Group**

**Objective:**  
Understand how users from different age groups engage with content based on likes and retweets.

**Tasks:**

- **Join Datasets**: Combine `posts.csv` and `users.csv` using `UserID`.
- **Group by AgeGroup**: Calculate average likes and retweets for each age group.
- **Rank Groups**: Sort the results to highlight the most engaged age group.

**Expected Outcome:**  
A summary of user engagement behavior categorized by age group.

**Example Output:**

| Age Group | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Adult     | 67.3      | 25.2         |
| Teen      | 22.0      | 5.6          |
| Senior    | 9.2       | 1.3          |

---

### **3. Sentiment vs Engagement**

**Objective:**  
Evaluate how sentiment (positive, neutral, or negative) influences post engagement.

**Tasks:**

- **Categorize Posts**: Group posts into Positive (`>0.3`), Neutral (`-0.3 to 0.3`), and Negative (`< -0.3`) sentiment groups.
- **Analyze Engagement**: Calculate average likes and retweets per sentiment category.

**Expected Outcome:**  
Insights into whether happier or angrier posts get more attention.

**Example Output:**

| Sentiment | Avg Likes | Avg Retweets |
|-----------|-----------|--------------|
| Positive  | 85.6      | 32.3         |
| Neutral   | 27.1      | 10.4         |
| Negative  | 13.6      | 4.7          |

---

### **4. Top Verified Users by Reach**

**Objective:**  
Find the most influential verified users based on their post reach (likes + retweets).

**Tasks:**

- **Filter Verified Users**: Use `Verified = True` from `users.csv`.
- **Calculate Reach**: Sum likes and retweets for each user.
- **Rank Users**: Return top 5 verified users with highest total reach.

**Expected Outcome:**  
A leaderboard of verified users based on audience engagement.

**Example Output:**

| Username       | Total Reach |
|----------------|-------------|
| @techie42      | 1650        |
| @designer_dan  | 1320        |

---

## 🔍 Code Explanation for Each Task

All the analysis code is located in the `src/` directory. Each script is responsible for solving one of the assignment tasks using PySpark's powerful DataFrame and SQL APIs. Below is a breakdown of how each task is implemented.

---

### ✅ Task 1: Hashtag Trends (`task1_hashtag_trends.py`)

**Goal:** Identify the top 10 most frequently used hashtags from all posts.

**Steps:**
1. Load `posts.csv` into a DataFrame using `spark.read.csv()` with headers.
2. Split the `Hashtags` column into arrays using `split()`.
3. Use `explode()` to flatten arrays into individual hashtag rows.
4. Group by `hashtag` and count how often each one appears.
5. Sort the hashtags in descending order based on count.
6. Save the result to `outputs/hashtag_trends.csv`.

**Key PySpark Functions:**
- `split(col("Hashtags"), ",")`
- `explode()`
- `groupBy().count()`
- `orderBy()`

**Code Snippet:**
```python
hashtag_counts = posts_df.select(
    explode(split(col("Hashtags"), ",")).alias("hashtag")
).groupBy("hashtag").count().orderBy(col("count").desc())


---

### ✅ Task 2: Engagement by Age Group (`task2_engagement_by_age.py`)

**🎯 Goal:**  
Analyze how users from different age groups (Teen, Adult, Senior) engage with posts based on average likes and retweets.

**🧠 Approach:**
1. Load `posts.csv` and `users.csv` using `spark.read.csv()` with `inferSchema=True`.
2. Perform an inner join on `UserID` to combine post and user info.
3. Group the joined DataFrame by `AgeGroup`.
4. Use `avg()` to calculate average likes and retweets.
5. Sort the results by average likes in descending order.
6. Save the final output to `outputs/engagement_by_age.csv`.

**🛠️ PySpark Functions Used:**
- `join()` – combine both DataFrames on `UserID`
- `groupBy().agg(avg())` – compute average metrics
- `orderBy()` – sort age groups by engagement

**💡 Sample Code Snippet:**
```python
joined_df = posts_df.join(users_df, "UserID")

engagement_df = joined_df.groupBy("AgeGroup").agg(
    avg(col("Likes")).alias("AvgLikes"),
    avg(col("Retweets")).alias("AvgRetweets")
).orderBy(col("AvgLikes").desc())

---

### ✅ Task 3: Sentiment vs Engagement (`task3_sentiment_vs_engagement.py`)

**Objective:**  
Explore the relationship between sentiment and post engagement (likes and retweets). Posts are categorized as Positive, Neutral, or Negative based on their sentiment scores.

**Steps:**
1. Load the `posts.csv` file with `inferSchema=True` to interpret numeric columns like `SentimentScore`.
2. Use `when()` and `otherwise()` to create a new column `Sentiment`:
   - **Positive**: SentimentScore > 0.3
   - **Neutral**: -0.3 ≤ SentimentScore ≤ 0.3
   - **Negative**: SentimentScore < -0.3
3. Group the posts by `Sentiment`.
4. Calculate average `Likes` and average `Retweets` for each sentiment group.
5. Save the result to `outputs/sentiment_engagement.csv`.

**Key Functions Used:**
- `withColumn()` — to create the `Sentiment` label.
- `when()` and `otherwise()` — for conditional column logic.
- `groupBy().agg(avg(...))` — for aggregation.

**Code Snippet:**
```python
sentiment_df = posts_df.withColumn(
    "Sentiment",
    when(col("SentimentScore") > 0.3, "Positive")
    .when(col("SentimentScore") < -0.3, "Negative")
    .otherwise("Neutral")
)

sentiment_stats = sentiment_df.groupBy("Sentiment").agg(
    avg(col("Likes")).alias("AvgLikes"),
    avg(col("Retweets")).alias("AvgRetweets")
)

---

### ✅ Task 4: Top Verified Users by Reach (`task4_top_verified_users.py`)

**Objective:**  
Identify the top 5 most influential verified users based on total reach, where **reach = likes + retweets**.

**Steps:**
1. Load `users.csv` and `posts.csv` using `spark.read.option("header", True).csv(..., inferSchema=True)` to ensure correct data types.
2. Filter the `users_df` to include only rows where `Verified == True`.
3. Join the filtered users with `posts_df` on the common `UserID` column.
4. Create a new column called `Reach`, defined as `Likes + Retweets`, using `withColumn()`.
5. Group by `Username` and calculate the total reach using `sum()` (aliased as `TotalReach`).
6. Sort the result in descending order of total reach.
7. Limit the output to the **Top 5** users.
8. Save the final result to `outputs/top_verified_users.csv`.

**Key Functions Used:**
- `filter()` — to select only verified users.
- `join()` — to associate posts with user data.
- `withColumn()` — to compute `Reach`.
- `groupBy().agg(sum(...))` — to calculate total reach.
- `orderBy().limit()` — to rank and restrict the result.

**Code Snippet:**
```python
verified_users_df = users_df.filter(col("Verified") == True)

verified_posts_df = posts_df.join(verified_users_df, "UserID").withColumn(
    "Reach", col("Likes") + col("Retweets")
)

top_verified = verified_posts_df.groupBy("Username").agg(
    _sum("Reach").alias("TotalReach")
).orderBy(col("TotalReach").desc()).limit(5)


## **Grading Criteria**

| Task                        | Marks |
|-----------------------------|-------|
| Hashtag Trend Analysis      | 1     |
| Engagement by Age Group     | 1     |
| Sentiment vs Engagement     | 1     |
| Top Verified Users by Reach | 1     |
| **Total**                   | **1** |

---

## 📬 Submission Checklist

- [ ] PySpark scripts in the `src/` directory  
- [ ] Output files in the `outputs/` directory  
- [ ] Datasets in the `input/` directory  
- [ ] Completed `README.md`  
- [ ] Commit everything to GitHub Classroom  
- [ ] Submit your GitHub repo link on canvas

---

Now go uncover the trends behind the tweets 📊🐤✨
