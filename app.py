import streamlit as st

# اسکرین پر دل اور غبارے دکھانے کے لیے
st.set_page_config(page_title="A Special Message", page_icon="❤️")

st.title("Assalam-o-Alaikum Momina! ✨")
st.header("I have a very special question for you...")

# بٹن بنانا
if st.button("Will you marry me?"):
    st.balloons()  # اسکرین پر رنگ برنگے غبارے اڑیں گے
    st.snow()      # برف باری والا ایفیکٹ
    st.success("You've made me the happiest person in the world! ❤️")
    st.write("I promise to build a beautiful future with you, full of love (and code! 😉)")
