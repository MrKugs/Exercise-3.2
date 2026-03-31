import streamlit as st

st.title("Question 5 & 6: Robust Division App")

n1 = st.text_input("First Number:")
n2 = st.text_input("Second Number:")

if st.button("Calculate"):
    try:
        res = float(n1) / float(n2)
        st.success(f"Result: {res}")
    except ValueError:
        st.error("ERROR!: Please enter numeric digits only.")
    except ZeroDivisionError:
        st.error("Meaningful Message: You cannot divide by zero.")


