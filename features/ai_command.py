from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_name = "Salesforce/codet5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

def generate_excel_formula(user_input):
    prompt = f"Write an Excel formula to: {user_input}"
    result = generator(prompt, max_new_tokens=50)
    return result[0]['generated_text']

if __name__ == "__main__":
    user_command = input("Excel için yapmak istediğin işlemi yaz: ")
    formula = generate_excel_formula(user_command)
    print("Önerilen Excel Formülü:", formula)
