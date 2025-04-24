import streamlit as st
import yaml
from step_loader import discover_steps

st.title("🧪 YAML-Configured Plugin Pipeline")

# Load plugins
STEP_REGISTRY = discover_steps()

# Load YAML config
with open("pipeline.yaml", "r") as f:
    pipeline_def = yaml.safe_load(f)["pipeline"]

context = {}

# Execute pipeline
for step in pipeline_def:
    name = step["step"]
    config = step.get("config", {})
    st.subheader(f"🔹 Step: {name}")

    func = STEP_REGISTRY.get(name)
    if not func:
        st.error(f"❌ Step '{name}' not found in plugins.")
        continue

    try:
        with st.spinner(f"Running {name}..."):
            result = func(config, context)
        st.code(result)
    except Exception as e:
        st.error(f"❗ Error in step '{name}': {e}")

# Optional debug info
if st.checkbox("🔍 Show Context"):
    st.json({k: str(v) for k, v in context.items()})
