import streamlit as st

# Set the title of the app
st.title("Simple Calculator")

# User inputs
st.write("Enter the numbers and select the operation:")
num1 = st.number_input("First Number", value=0.0, step=0.1)
num2 = st.number_input("Second Number", value=0.0, step=0.1)

operation = st.selectbox("Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform calculation based on user selection
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

# Display the result
st.write(f"The result of {operation} is: {result}")
