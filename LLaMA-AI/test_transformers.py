from transformers import AutoModelForCausalLM, AutoTokenizer

try:
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
    print("Transformers 模組成功載入！")
except Exception as e:
    print("發生錯誤：", e)
