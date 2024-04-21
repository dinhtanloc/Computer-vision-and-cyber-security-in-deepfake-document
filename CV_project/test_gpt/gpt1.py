import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load tokenizer và model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def chatbot(user_input):
    # Tiền xử lý đầu vào
    input_text = f"User: {user_input} \nBot:"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')

    # Tạo đầu ra từ mô hình
    bot_output = model.generate(input_ids, max_length=150, pad_token_id=tokenizer.eos_token_id)

    # Giải mã và trả về kết quả
    bot_response = tokenizer.decode(bot_output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return bot_response

def main():
    st.title("Simple Chatbot with Streamlit and GPT-2")

    user_input = st.text_input("You:", "")
    
    if st.button("Send"):
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=200, max_chars=None, key=None)

if __name__ == "__main__":
    main()
