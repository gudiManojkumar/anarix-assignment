import sqlite3
import pandas as pd


df_total_sales = pd.read_csv("./datasets/total_sales.csv")
df_ad_sales = pd.read_csv("./datasets/ad_sales.csv")
df_eligibility = pd.read_csv("./datasets/eligibility.csv")


conn = sqlite3.connect('D://ecommerce//ecommerce.db')


df_total_sales.to_sql('total_sales_metrics', conn, if_exists='replace', index=False)
df_ad_sales.to_sql('ad_sales_metrics', conn, if_exists='replace', index=False)
df_eligibility.to_sql('eligibility_table', conn, if_exists='replace', index=False)


conn.close()