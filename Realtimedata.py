# Databricks notebook source
dbutils.fs.put('/scenario/sensor.csv',"""Location,Sensor,Metric,Timestamp,Temp,Air_Velocity,Sensitivity,Humidity
LocationA,Sensor1,Temperature,2023-08-10 00:00:00,25.6,2.3,0.87,60,2
LocationA,Sensor2,Temperature,2023-08-10 00:00:00,24.8,2.1,0.92,58.7
LocationB,Sensor1,Temperature,2023-08-10 00:00:00,26.3,2.5,0.81,55.8
LocationB,Sensor2,Temperature,2023-08-10 00:00:00,24.1,2.0,0.95,59.4""")

# COMMAND ----------

dbutils.fs.ls('/scenario/')

# COMMAND ----------

dbutils.fs.ls('/scenario/sensor.csv')

# COMMAND ----------

df=spark.read.csv('/scenario/sensor.csv',header=True)

# COMMAND ----------

df.show(10)


# COMMAND ----------


