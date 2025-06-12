#we are now testing qwen communication and finding test cases for the minus operators of all primitve datatype of python.
import json
from llama_cpp import Llama

# Path to Qwen GGUF model
MODEL_PATH = r"D:\qwen1.5-moe-a2.7b-chat-q3_k_s\qwen1.5-moe-a2.7b-chat-q3_k_s.gguf"

# Load Qwen GGUF model with optimized settings
llm = Llama(model_path=MODEL_PATH, n_ctx=8192, n_batch=512)

# Define structured prompt for minus operator test cases


PROMPT = """"""
try:
    with open("prompt.txt", "r", encoding = "utf-8") as f:
        
        PROMPT = f.read()

except FileNotFoundError:
    with open("prompt.txt", "w", encoding = "utf-8") as f:
        print(f"prompt file {f} create")
    PROMPT = """What are test cases?"""
# Generate AI response
response = llm(prompt=PROMPT, max_tokens=4096, temperature=0.9)
print(response["choices"][0]["text"])
# Extract and clean raw JSON output
raw_output = response["choices"][0]["text"].replace("\n", "").strip()

# Validate JSON structure
try:
    structured_json = json.loads(raw_output)
    print("✅ JSON Output is Valid!")
except json.JSONDecodeError:
    print("⚠️ AI response needs formatting fixes.")
    structured_json = {"response": {"tests": {}}}  # Fallback empty JSON structure

# Save JSON to a file
JSON_FILE_PATH = r"D:\test-case-generator\src\test-case-generation-qwen\main code\json-output (1).json"
with open(JSON_FILE_PATH, "w", encoding="utf-8") as json_file:
    json.dump(structured_json, json_file, indent=4)

print(f"✅ Test cases saved to {JSON_FILE_PATH}")