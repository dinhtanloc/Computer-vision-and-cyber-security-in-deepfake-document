import streamlit as st
from PIL import Image

def chatbot_response(user_input):
    # Đây là một ví dụ đơn giản, bạn có thể thay đổi hoặc mở rộng chức năng này
    if "dog" in user_input.lower():
        response = "Here's a dog image!"
        # image_path = "path_to_dog_image.jpg"  # Đường dẫn đến hình ảnh chó
    elif "cat" in user_input.lower():
        response = "Here's a cat image!"
        # image_path = "path_to_cat_image.jpg"  # Đường dẫn đến hình ảnh mèo
    else:
        response = "I don't have an image for that."
        image_path = None

    return response, image_path

def main():
    st.title("Chatbox with Image Display")

    # Khởi tạo danh sách để lưu trữ lịch sử chat
    chat_history = []

    # Widget để nhập văn bản
    user_input = st.text_input("You:", "")

    # Xử lý và hiển thị phản hồi từ chatbot
    if st.button("Send"):
        if user_input:
            response, image_path = chatbot_response(user_input)
            chat_history.append({"user": user_input, "bot": response, "image": image_path})

    # Hiển thị lịch sử chat
    for chat in chat_history:
        st.text_area("You:", value=chat["user"], height=50)
        st.text_area("Chatbot:", value=chat["bot"], height=50)
        
        # Hiển thị hình ảnh nếu có
        if chat["image"]:
            image = Image.open(chat["image"])
            st.image(image, caption="Uploaded Image.", use_column_width=True)

if __name__ == "__main__":
    main()
