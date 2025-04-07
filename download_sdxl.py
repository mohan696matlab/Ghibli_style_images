from huggingface_hub import snapshot_download
import os

# Define the model repository ID on Hugging Face
model_id = "diffusers/controlnet-depth-sdxl-1.0-small"

# Define the specific folder where you want to download the model
# IMPORTANT: Replace "path/to/your/specific/folder" with the actual path
target_folder = "/home/nas/buffer/mohan.dash/controlnet-depth-sdxl"

# Create the target folder if it doesn't exist
os.makedirs(target_folder, exist_ok=True)

print(f"Downloading model {model_id} to {target_folder}...")

# Download the model snapshot to the specified folder
# local_dir_use_symlinks=False ensures files are copied, not symlinked (safer for portability)
snapshot_download(
    repo_id=model_id,
    local_dir=target_folder,
    local_dir_use_symlinks=False,
    # You can optionally specify specific file types or ignore patterns
    allow_patterns=["*model.safetensors", "*.json", "*.txt"], # Example: only download safetensors and config files
    # ignore_patterns=["*.ckpt", "*.pt"], # Example: ignore older checkpoint formats
)

print(f"Model downloaded successfully to {target_folder}")