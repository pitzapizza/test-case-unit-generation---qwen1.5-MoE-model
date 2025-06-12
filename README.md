# **Qwen-Based Test Case Unit Generation**

## **Overview**
This project automates unit test case generation using **Qwen models**, ensuring structured validation for improved test coverage and reliability. The system generates test cases from prompts, validating logic consistency and adaptability. While the model enhances structured validation, its accuracy depends on well-formed prompts.

## **How to Download the Qwen Model**
The project requires the **Qwen1.5-MoE-A2.7B-Chat-Q3_K_S** model. You can download it from the official Qwen repository:

👉 [Qwen Model Download](https://huggingface.co/Gapsar/Qwen1.5-MoE-A2.7B-Chat-Q3_K_S-GGUF/blob/main/qwen1.5-moe-a2.7b-chat-q3_k_s.gguf)

Once downloaded, update the `MODEL_PATH` in the code to reflect your local directory.

## **Project Workflow**
1. **Run `generate-prompt.py` First**  
   Before executing the main script, you must run `generate-prompt.py`. This script allows you to define structured prompts inside `prompt.txt`. These prompts are crucial because AI-generated test cases depend on well-crafted inputs.

2. **Executing `main.py`**  
   After defining the prompt, `main.py` processes it using the **Qwen model**. The script:
   - Loads the Qwen model.
   - Reads the prompt from `prompt.txt`.
   - Generates AI-driven test cases.
   - Validates the response format and converts it into structured JSON.
   - Saves the output in a JSON file for further analysis.

3. **File Path Customization**  
   Paths within the script (such as the model and JSON output locations) should be **modified according to the user's implementation**. Ensure all paths are correctly set to avoid errors.

## **Limitations & Next Steps**
🔸 The project is **not fully completed** and is still evolving.  
🔸 AI-generated test cases depend on **well-structured prompts**—poorly defined prompts may lead to inconsistent results.  
🔸 Future improvements will refine prompt engineering and validation accuracy.

---

This README clearly outlines the workflow, dependencies, and limitations without unnecessary details. Good luck! 🚀
