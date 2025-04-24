# 🚪 Streamlit YAML Plugin Pipeline

A modular and extensible pipeline framework built with **Streamlit**, **YAML**, and **plugin-discoverable Python scripts**. Define pipeline steps declaratively in YAML and implement logic in drop-in plugin files — no manual registration needed.

---

## ✨ Features

- 🛡️ **Modular pipeline steps** defined in `plugins/`
- ✍️ **Declarative pipeline configs** in `pipeline.yaml`
- 🔌 **Auto-discovery of plugins** via `importlib`
- 🎛️ **Streamlit UI** to run and inspect pipelines
- 🧠 **Shared context** between steps for passing data
- ✅ Easily extendable — just drop a new `.py` into `plugins/`

---

## 📁 Project Structure

```
my_pipeline_app/
├── app.py                  # Main Streamlit app
├── pipeline.yaml           # YAML config that defines the pipeline steps
├── step_loader.py          # Plugin auto-discovery
└── plugins/                # Drop-in step logic
    ├── load_data.py
    ├── filter_rows.py
    └── summarize.py
```

---

## 🔧 How It Works

### 1. Define Steps in YAML

```yaml
pipeline:
  - step: load_data
    config: {}

  - step: filter_rows
    config:
      min_age: 30

  - step: summarize
    config: {}
```

### 2. Implement Steps as Plugins

Each plugin must define:

- `step_name`: a unique string
- `run(config, context)`: a function that accepts step config and context dictionary

#### Example: `plugins/load_data.py`

```python
step_name = "load_data"

def run(config, context):
    import pandas as pd
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 32, 37]
    })
    context["data"] = df
    return "Data loaded"
```

### 3. Launch the App

```bash
streamlit run app.py
```

You'll see a dynamic interface executing each step and sharing data via `context`.

---

## 🧠 Design Principles

- **Configurable:** Pipeline behavior is defined in a human-readable YAML file.
- **Composable:** Each step is a modular plugin that’s easy to test and reuse.
- **Safe:** Only registered or discovered functions are called — avoids `eval()` risk.
- **Extendable:** Add steps by simply dropping new Python files into `plugins/`.

---

## 🚀 Future Ideas

- Add optional `description` and `parameter_schema` fields to each plugin
- Build a live YAML editor into the Streamlit UI
- Add support for conditional steps and branching
- Generate a Mermaid.js or Graphviz visual of the pipeline

---

## 📜 License

MIT License. Use it freely and build cool things!

---

## 🧑‍💻 Built With

- [Streamlit](https://streamlit.io)
- [PyYAML](https://pyyaml.org)
- [importlib](https://docs.python.org/3/library/importlib.html)

