import streamlit as st

# Store price database
STORE = {'milk': 25.0, 'rice': 100.0, 'water': 20.0, 'snacks': 10.0}

# 1. Initialize session state cart (persists items across clicks)
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# --- Modular Functions ---

def add_item(item_name, qty):
    """Appends or updates items in the cart dictionary."""
    if item_name in STORE:
        st.session_state.cart[item_name] = st.session_state.cart.get(item_name, 0) + qty
        st.success(f"Added {qty} x {item_name} to cart!")
    else:
        st.error("Item not found in supermarket inventory!")

def calculate_total(cart):
    """Calculates subtotal based on store prices."""
    subtotal = 0
    for item, qty in cart.items():
        if item in STORE:
            subtotal += qty * STORE[item]
    return subtotal

def calculate_gst(subtotal):
    """Calculates 5% GST and final total."""
    gst_amount = subtotal * 0.05
    final_total = subtotal + gst_amount
    return gst_amount, final_total

# --- Streamlit GUI Interface ---

st.title("🛒 HOJA Super Market")
st.subheader("Grocery Billing System")

# User Input Widgets
col1, col2 = st.columns(2)
with col1:
    item_input = st.text_input("Enter Item Name").lower().strip()
with col2:
    qty_input = st.number_input("Enter Quantity", min_value=1, step=1)

# Add Item Button
if st.button("Add Item"):
    if item_input:
        add_item(item_input, qty_input)
    else:
        st.warning("Please enter an item name.")

# Live Cart Display
if st.session_state.cart:
    st.write("### 🛒 Active Shopping Cart")
    
    # Format cart into tabular view
    cart_display = []
    for item, qty in st.session_state.cart.items():
        price = STORE.get(item, 0)
        cart_display.append({
            "Item": item.capitalize(),
            "Quantity": qty,
            "Price per Unit": f"₹{price}",
            "Total": f"₹{qty * price}"
        })
    st.table(cart_display)

    # Real-Time Calculations
    subtotal = calculate_total(st.session_state.cart)
    gst, final_total = calculate_gst(subtotal)

    st.write(f"**Subtotal:** ₹{subtotal:.2f}")
    st.write(f"**GST (5%):** ₹{gst:.2f}")
    st.write(f"### **Final Total:** ₹{final_total:.2f}")

    # Generate Bill Trigger
    if st.button("Generate Bill"):
        st.divider()
        st.write("### 🧾 Official Receipt")
        st.write("**HOJA Super Market**")
        st.write("GSTIN: 32AAAAA0000A1Z5")
        st.divider()
        for row in cart_display:
            st.write(f"{row['Item']} ({row['Quantity']} x {row['Price per Unit']}) = {row['Total']}")
        st.divider()
        st.write(f"**Grand Total:** ₹{final_total:.2f}")
        st.write("Thank You! Visit Again 😊")