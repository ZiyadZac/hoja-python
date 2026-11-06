import streamlit as st
st.title("Zac's convenience store")
st.subheader('Everything U need!!!')
store_inventory = {
    "milk": 3.99,
    "eggs": 3.49,
    "bread": 2.99,
    "bananas": 1.89,
    "chicken breast": 5.49,
    "rice": 6.29,
    "apples": 2.19,
    "cheddar cheese": 3.79,
    "butter": 4.89,
    "pasta": 1.49
}
if 'cart' not in st.session_state:
    st.session_state.cart = {}
def add_item(item_name, quantity):
    """Adds an item to the cart or updates quantity if it already exists."""
    item_name = item_name.lower().strip()
    
    if item_name in store_inventory:
        
        if item_name in st.session_state.cart:
            st.session_state.cart[item_name] += quantity
        else:
            
            st.session_state.cart[item_name] = quantity
        st.success(f"Added {quantity} of {item_name} to your cart!")
    else:
        st.error("Sorry! That item is not available in our store inventory.")
def calculate_total(cart_dict):
    """Calculates the subtotal by multiplying quantity with price for each item."""
    subtotal = 0.0
    for item, qty in cart_dict.items():
        price = store_inventory[item]
        subtotal += qty * price
    return subtotal
def calculate_gst(subtotal):
    """Calculates 5% GST and returns both GST amount and final total."""
    gst_amount = subtotal * 0.05
    final_total = subtotal + gst_amount
    return gst_amount, final_total

st.write("### Add Items to Cart")

# Text input for item name and number input for quantity
item_input = st.text_input("Enter Item Name (milk, rice, water, snacks)")
qty_input = st.number_input("Enter Quantity", min_value=1, step=1)


if st.button("Add Item"):
    if item_input != "":
        add_item(item_input, qty_input)
    else:
        st.warning("Please type an item name first.")
if len(st.session_state.cart) > 0:
    st.divider()
    st.write("### 🛒 Current Shopping Cart")
    
    # Prepare list for table display
    display_data = []
    for item, qty in st.session_state.cart.items():
        unit_price = store_inventory[item]
        total_price = qty * unit_price
        display_data.append({
            "Item Name": item.capitalize(),
            "Quantity": qty,
            "Unit Price (₹)": unit_price,
            "Total (₹)": total_price
        })
        
    # Show table
    st.table(display_data)
    
    # Calculate Subtotal and GST using our functions
    subtotal_amount = calculate_total(st.session_state.cart)
    gst_fee, final_bill_amount = calculate_gst(subtotal_amount)
    
    # Display Totals
    st.write(f"**Subtotal:** ₹{subtotal_amount:.2f}")
    st.write(f"**GST (5%):** ₹{gst_fee:.2f}")
    st.write(f"### **Final Total:** ₹{final_bill_amount:.2f}")

    # Generate Bill Button
    if st.button("Generate Official Bill"):
        st.divider()
        st.markdown("### 🧾 Zac's convenience store")
        st.text("GSTIN: 32AAAAA0000A1Z5")
        st.markdown("---")
        for row in display_data:
            st.text(f"{row['Item Name']}: {row['Quantity']} x ₹{row['Unit Price (₹)']} = ₹{row['Total (₹)']}")
        st.markdown("---")
        st.text(f"Subtotal: ₹{subtotal_amount:.2f}")
        st.text(f"GST (5%): ₹{gst_fee:.2f}")
        st.text(f"Grand Total: ₹{final_bill_amount:.2f}")
        st.markdown("Thank You! Visit Again 😊")