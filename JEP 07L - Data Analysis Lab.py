# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC # Data Analysis with Pandas
# MAGIC 
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/301/sf.jpg" style="height: 200px; margin: 10px; border: 1px solid #ddd; padding: 10px"/>
# MAGIC 
# MAGIC You'll be analyzing data from [Inside Airbnb]((http://insideairbnb.com/get-the-data.html) to better understand the San Francisco rental market.
# MAGIC 
# MAGIC 0. Read in SF Airbnb data into a pandas DataFrame
# MAGIC 0. Select a subset of columns
# MAGIC 0. Sort based on largest # of bedrooms
# MAGIC 0. Fill in missing values
# MAGIC 0. Compute the average number of bathrooms
# MAGIC 0. Plot the most common property listings in the Financial District

# COMMAND ----------

# MAGIC %md
# MAGIC Read in the file located `/dbfs/databricks-datasets/learning-spark-v2/sf-airbnb/sf-airbnb.csv` into a pandas DataFrame, and display the first 5 records.

# COMMAND ----------

# MAGIC %sh ls /dbfs/databricks-datasets/learning-spark-v2/sf-airbnb/

# COMMAND ----------

import pandas as pd
pd.read_csv("/dbfs/databricks-datasets/learning-spark-v2/sf-airbnb/sf-airbnb.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC We are not interested in all of the columns in this DataFrame so let's select just these columns: 
# MAGIC 
# MAGIC `"beds", "bedrooms", "bathrooms", "property_type", "neighbourhood_cleansed"` and assign the result to the variable `df`.
# MAGIC 
# MAGIC NOTE: We are not looking at the `price` column for now because we need to convert it from a string to a double (and remove the `$` and `,` from the values)

# COMMAND ----------

df = pd.read_csv("/dbfs/databricks-datasets/learning-spark-v2/sf-airbnb/sf-airbnb.csv")
df = df[["beds", "bedrooms", "bathrooms", "property_type", "neighbourhood_cleansed"]]

# COMMAND ----------

# MAGIC %md
# MAGIC Now that we have the columns that we want, we would like to view the listings with the highest number of bedrooms first. We can do this using the [.sort_values()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) function!

# COMMAND ----------

df.sort_values("bedrooms", ascending=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Fill Missing Values
# MAGIC If you scroll through the rows carefully you'll notice that some of the entries say `NaN` instead of a number. Run the following cell to pick out and display those listings using [isna()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isna.html).

# COMMAND ----------

df[df.isna().any(axis=1)]

# COMMAND ----------

# MAGIC %md
# MAGIC We're going to assume if a listing didn't input a number for `beds`, `bedrooms`, or `bathrooms` then the number should have been a 0.
# MAGIC 
# MAGIC Let's go ahead and fill the missing values for `beds`, `bedrooms`, or `bathrooms` with `0`.

# COMMAND ----------

#my attempt, which did not work
df = df[df.fillna("0").any(axis=1)]

# COMMAND ----------

#answer
df = df.fillna(0)

# COMMAND ----------

df[df.isna().any(axis=1)]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Average # Bathrooms
# MAGIC What is the average number of bathrooms in this list of Airbnb listings?

# COMMAND ----------

df["bathrooms"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Filter
# MAGIC 
# MAGIC Suppose we are only going to be near `Financial District` so we only want to view listings in that neighbourhood.

# COMMAND ----------

# TODO
financial_district_df = df.loc[df["neighbourhood_cleansed"]=="Financial District"]
financial_district_df

# COMMAND ----------

#DB answer
financial_district_df = df[df["neighbourhood_cleansed"]=="Financial District"]
financial_district_df

# COMMAND ----------

# MAGIC %md
# MAGIC ### Plot
# MAGIC 
# MAGIC We want to see what the most common types of property listings around `Financial District` are! 
# MAGIC 
# MAGIC [Plot](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html) the count of the various `property_type`.

# COMMAND ----------

#suggested solution
financial_district_df.groupby(by="property_type").count().plot(kind="bar", y="beds")

# COMMAND ----------

#my tweaked favorite
#property_type er kolonnen som det grupperes på, men det telles over neighborhood_cleansed kolonnen
financial_district_df.groupby(by="property_type")["neighbourhood_cleansed"].count().plot(kind="bar")

# COMMAND ----------

financial_di

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2020 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="http://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="http://help.databricks.com/">Support</a>
