import streamlit as st
st.title("📒 Contact Book ")
menu=st.sidebar.selectbox("Select an Option",["Add Contact", "Search Contact", "Delete Contact", "View Contacts"])

if 'contacts' not in st.session_state:
    st.session_state.contacts = {}

if menu == "Add Contact":
    st.subheader("➕ Add a New Contact")
 
    name = st.text_input("Enter Name").lower().strip().capitalize()
    phone = st.text_input("Enter Phone Number").strip()
    
    if st.button("Add Contact"):
        if name != "" and phone != "":
            # Check if phone number already exists in our saved contacts
            if phone in st.session_state.contacts.values():
                st.error("Error: This phone number is already registered!")
            else:
                # Save into session state using your simple name -> phone dictionary style
                st.session_state.contacts[name] = phone
                st.success(f"Contact '{name}' added successfully!")
        else:
            st.warning("Please fill in both name and phone number.")

if menu == "Search Contact":
    st.subheader("🔍 Search for a Contact")
    
    # Text input to search by name
    search_name = st.text_input("Enter Name to Search").lower().strip().capitalize()
    
    if st.button("Search"):
        if search_name != "":
            # Check if name exists in our session state dictionary
            if search_name in st.session_state.contacts:
                phone_num = st.session_state.contacts[search_name]
                st.success(f"Found Contact!")
                st.write(f"**Name:** {search_name}")
                st.write(f"**Phone:** {phone_num}")
            else:
                st.error("Contact not found in your book.")
        else:
            st.warning("Please enter a name to search.")

if menu == "View Contacts":
    st.subheader("📖 All Saved Contacts")
    
    # Check if there are any contacts saved
    if len(st.session_state.contacts) > 0:
        # Loop through the dictionary and display each contact
        for name, phone in st.session_state.contacts.items():
            st.write(f"**Name:** {name} | **Phone:** {phone}")
    else:
        st.info("Your contact book is currently empty. Add some contacts first!")

if menu == "Delete Contact":
    st.subheader("❌ Delete a Contact")
    
    # Text input for name to delete
    delete_name = st.text_input("Enter Name to Delete").lower().strip().capitalize()
    
    if st.button("Delete Contact"):
        if delete_name != "":
            if delete_name in st.session_state.contacts:
                # Remove the contact from our session state dictionary
                del st.session_state.contacts[delete_name]
                st.success(f"Contact '{delete_name}' deleted successfully!")
            else:
                st.error("Contact not found in your book.")
        else:
            st.warning("Please enter a name to delete.")