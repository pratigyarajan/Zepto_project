import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df=pd.read_csv("zepto_v2.csv", encoding="ISO-8859-1")

st.set_page_config(page_title=" Zepto Inventory Dashboard...",layout="wide")

st.title("welcome to Zepto Inventory..,!📦")

with st.sidebar:
    st.header("🔍Find our Products")
    Category=st.selectbox("choose ur category",["All"]+list(df["Category"].unique()))
    
    if Category=="All":
        name_options=["All"]+list(df["name"].unique())
        print(name_options)
    else:
        fil=df[df["Category"]==Category]
        name_options=["All"]+list(fil["name"].unique())
    
    name=st.selectbox("SubCategory",name_options,index=0)

filtered=df.copy()
if Category!="All":
    filtered=filtered[filtered["Category"]==Category]
if name!="All":
    filtered=filtered[filtered["name"]==name]

# mrp by category
st.subheader("MRP Rate of the product")
fig1, ax1=plt.subplots()
sns.barplot(x="mrp",y="Category",
            data=filtered.sort_values("mrp",ascending=False),
            ax=ax1,palette="Spectral")
st.pyplot(fig1)

#subproduct rate
st.subheader("Subproduct Rate")
fig2, ax2=plt.subplots()
sns.barplot(x="mrp",y="name",
            data=filtered.sort_values("mrp",ascending=False),
            ax=ax2,palette="coolwarm")
st.pyplot(fig2)



# Plot 2: Discount vs Profit
st.subheader("🎯 MRP vs Discount")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=filtered,
                 x='mrp',
                   y='discountPercent', 
                   hue='Category', ax=ax3)
st.pyplot(fig3)

# st.subheader("Category & subCategory")
# fig2, ax2=plt.subplots()
# sns.catplot(x="name",y="discountedSellingPrice",data=filtered,ax=ax2,palette="coolwarm")
# st.pyplot(fig2)