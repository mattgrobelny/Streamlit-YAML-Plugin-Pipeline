import os
import importlib.util

def discover_steps(plugin_dir="plugins"):
    registry = {}
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py"):
            path = os.path.join(plugin_dir, filename)
            module_name = filename[:-3]

            spec = importlib.util.spec_from_file_location(module_name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "step_name") and hasattr(module, "run"):
                registry[module.step_name] = module.run
            else:
                print(f"⚠️ Plugin {filename} missing 'step_name' or 'run'")
    return registry
