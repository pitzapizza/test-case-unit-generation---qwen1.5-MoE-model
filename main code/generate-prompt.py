prompt_text = """You are generating structured unit test cases for a secure banking login system.

Your output must be **valid JSON** in the following format:
{
  "response": {
    "tests": {
      "TC001": {
        "description": "...",
        "input": {
          "username": "...",
          "password": "..."
        },
        "expected_status_code": ...,
        "expected_response": "..."
      },
      ...
    }
  }
}

✅ DO:
- Use a JSON **object** under `"tests"` with test case IDs like `"TC001"`, `"TC002"`, etc.
- Include all required fields with proper JSON syntax.
- Return **only JSON**—no bullet points, no lists, no markdown, no natural language summary.

❌ DO NOT:
- Use an array `[]` for `"tests"`—this is invalid in our schema.
- Repeat keys (e.g., two `"expected_response"` fields).
- Return any commentary or explanation before or after the JSON.
- Omit test case IDs as dictionary keys.

🔄 If your output would violate these constraints, consider it illegal and regenerate a corrected version. This is a strict schema-generation task.

Think very broadly about the functionality of the prompt. Logically include every test cases that can be assumed and figure about it's content required from the above prompt.
"""


with open("prompt.txt", "w+", encoding="utf-8") as f:
    f.write(prompt_text)

print("Prompt file created: prompt.txt")