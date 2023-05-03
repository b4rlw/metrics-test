"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import generate_random_float


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=generate_random_float,
                inputs=None,
                outputs="random_number",
                name="generate_random_float",
            )
        ]
    )
