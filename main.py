import pandas as pd
import os

all_data = pd.read_csv("./trial/all_data.csv")

def generate_split_data(category):
    os.makedirs (f"./trial/split data/{category}", exist_ok=True)
    grouped_data = all_data.groupby(f"{category}")
    for group in grouped_data:
        group[1].to_csv(f"./trial/split data/{category}/{group[0]}_data.csv")

def generate_collective_data(category):
    os.makedirs (f"./trial/collective data/{category}", exist_ok=True)
    grouped_data = all_data.groupby (f"{category}").agg (
        counts = ("sales", "size"),
        average_sales = ("sales", "mean"),
        total_sales = ("sales", "sum")
    )

    grouped_data.to_csv(f"./trial/collective data/{category}/{category}_data.csv")

generate_split_data("date")
generate_split_data("location")
generate_split_data("payment_method")

generate_collective_data("location")
generate_collective_data("date")
generate_collective_data("payment_method")
