from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load once globally for efficiency
translator_tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-3.3B")
translator_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-3.3B")

def translate(text: str, lang: str) -> str:
    if lang.lower() == "hi":
        inputs = translator_tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        forced_bos_token_id = translator_tokenizer._tokenizer.lang_code_to_id["hin_Deva"]
        generated_tokens = translator_model.generate(
            **inputs,
            forced_bos_token_id=forced_bos_token_id,
            max_length=512,
        )
        return translator_tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    else:
        # For English or unsupported languages, return text as-is
        return text
