"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.8
"""
import random


def generate_random_float():
    random_float = random.random()
    return {"random_number": random_float}
