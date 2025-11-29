import streamlit as st

from llm import get_ai_response

st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")

st.title("🤖 소득세 챗봇")
st.caption("소득세에 관련된 모든것을 답해드립니다!")

# app.py의 세션 초기화 부분 수정
if 'message_list' not in st.session_state:
    st.session_state.message_list = []
    
    # 챗봇이 처음 시작할 때 AI의 환영 메시지를 띄워줌
    st.session_state.message_list.append({
        "role": "ai",
        "content": "안녕하세요! 저는 소득세법 전문 AI 챗봇입니다. 소득세 관련 궁금한 점을 질문해 주세요. (예: 소득 구분은 어떻게 되나요?)"
    })

for message in st.session_state.message_list:
    # 아이콘 설정 추가
    avatar_icon = "🧑‍💻" if message["role"] == "user" else "🤖" 

    with st.chat_message(message["role"], avatar=avatar_icon):
        st.write(message["content"])



if user_question := st.chat_input(...):
    with st.chat_message("user", avatar="🧑‍💻"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("답변을 생성하는 중입니다"):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({"role": "ai", "content": ai_message})