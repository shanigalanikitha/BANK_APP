import streamlit as st

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Smart Bank App",
    page_icon="🏦",
    layout="wide"
)

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#2E86C1;
}

.sub-title{
    font-size:25px;
    color:#117A65;
    font-weight:bold;
}

.stButton>button{
    background-color:#2E86C1;
    color:white;
    font-size:16px;
    border-radius:10px;
    padding:10px 20px;
}

.stButton>button:hover{
    background-color:#1B4F72;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------- BANK CLASS ----------------------
class BankAccount:

    def __init__(self,name,age,mobile_number,account_no,balance):
        self.name=name
        self.age=age
        self.mobile_number=mobile_number
        self.account_no=account_no
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return self.balance

    def mobile_update(self,new_mobile):
        self.mobile_number = new_mobile
        return new_mobile

    def check_balance(self):
        return self.balance


# ---------------------- TITLE ----------------------
st.markdown('<p class="main-title">🏦 Smart Bank Application</p>', unsafe_allow_html=True)


# ---------------------- SIDEBAR ----------------------
menu = st.sidebar.selectbox(
    "Navigation",
    ["Create Account","Deposit","Withdraw","Check Balance","Update Mobile"]
)

# ---------------------- CREATE ACCOUNT ----------------------
if menu == "Create Account":

    st.markdown('<p class="sub-title">Create New Account</p>', unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Name")
        age = st.number_input("🎂 Age",min_value=1)

    with col2:
        mobile = st.text_input("📱 Mobile Number")
        account_no = st.text_input("🏦 Account Number")

    balance = st.number_input("💰 Initial Balance",min_value=0)

    if st.button("Create Account"):

        st.session_state.account = BankAccount(name,age,mobile,account_no,balance)

        st.success("✅ Account Created Successfully!")



# ---------------------- DEPOSIT ----------------------
elif menu == "Deposit":

    st.markdown('<p class="sub-title">Deposit Money</p>', unsafe_allow_html=True)

    if "account" in st.session_state:

        amount = st.number_input("Enter Amount")

        if st.button("Deposit"):

            balance = st.session_state.account.deposit(amount)

            st.success(f"💰 Updated Balance: {balance}")

    else:
        st.warning("⚠ Please create account first")



# ---------------------- WITHDRAW ----------------------
elif menu == "Withdraw":

    st.markdown('<p class="sub-title">Withdraw Money</p>', unsafe_allow_html=True)

    if "account" in st.session_state:

        amount = st.number_input("Enter Amount")

        if st.button("Withdraw"):

            result = st.session_state.account.withdraw(amount)

            if result == "Insufficient Balance":
                st.error("❌ Insufficient Balance")
            else:
                st.success(f"💰 Remaining Balance: {result}")

    else:
        st.warning("⚠ Please create account first")



# ---------------------- CHECK BALANCE ----------------------
elif menu == "Check Balance":

    st.markdown('<p class="sub-title">Account Balance</p>', unsafe_allow_html=True)

    if "account" in st.session_state:

        balance = st.session_state.account.check_balance()

        st.info(f"💰 Your Balance is: {balance}")

    else:
        st.warning("⚠ Please create account first")



# ---------------------- UPDATE MOBILE ----------------------
elif menu == "Update Mobile":

    st.markdown('<p class="sub-title">Update Mobile Number</p>', unsafe_allow_html=True)

    if "account" in st.session_state:

        new_mobile = st.text_input("Enter New Mobile Number")

        if st.button("Update"):

            updated = st.session_state.account.mobile_update(new_mobile)

            st.success(f"📱 Mobile Updated: {updated}")

    else:
        st.warning("⚠ Please create account first")