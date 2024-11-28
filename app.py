import streamlit as st 
from ipwhois import IPWhois
import json

def get_ip_reputation(ip):
    try:
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        return json.dumps(results, indent=4)
    except Exception as e:
        return str(e)
    
st.title("IP Reputation Checker by sivolko")
ip = st.text_input("Enter IP Address:")
if st.button("Check Reputation"):
    if ip:
        result = get_ip_reputation(ip)
        st.code(result, language='json')
    else:
        st.error("Please enter a valid IP Address.")        