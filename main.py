import pandas as pd
import numpy as py
from transformers import pipeline
import torch

true_data = pd.read_csv("News_dataset/True.csv")
false_data = pd.read_csv("News_dataset/Fake.csv")

print(true_data.head())
