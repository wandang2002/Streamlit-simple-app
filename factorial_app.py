import streamlit as st

USERS = ["admin", "Wan Dang"]


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


def login():
    st.title("Login page")
    username = st.text_input("Username:")
    if st.button("Login"):
        if username:
            if username in USERS:
                st.session_state.logged_in = True
                st.session_state.user_name = username
            else:
                st.session_state.logged_in = False
                st.session_state.user_name = username
                st.warning(
                    f"{st.session_state.user_name} does not have access to this app."
                )
        else:
            st.warning("Input username")


def factorial_calculator():
    st.write(f"Hello, {st.session_state.username}")

    # Log out
    if st.button("Logged out"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.rerun()
    number = st.number_input(
        "Please input a positive integer you want to factorial",
        min_value=0,
        max_value=900,
    )
    if st.button("Factorial"):
        result = fact(number)
        st.write(f"Factorial of {number} is {result}")


def main():
    st.title("Calculation factorial app")

    # Create session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.user_name = False
    if st.session_state.logged_in:
        factorial_calculator()
    else:
        login()


if __name__ == "__main__":
    main()
