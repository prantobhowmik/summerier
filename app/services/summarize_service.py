from app.core.config import client

def summarize_text(text: str) -> str:
    prompt = f"Summarize this text in one short paragraph:\n{text}"
    print(f"[DEBUG] Prompt sent to model: {prompt}")
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )
    print(f"[DEBUG] Raw response from model: {response}")
    content = response.choices[0].message.content
    print(f"[DEBUG] Extracted summary: '{content}'")
    return content
