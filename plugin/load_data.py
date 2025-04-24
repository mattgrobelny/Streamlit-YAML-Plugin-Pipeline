step_name = "load_data"

def run(config, context):
    import pandas as pd
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 32, 37]
    })
    context["data"] = df
    return "Data loaded"
