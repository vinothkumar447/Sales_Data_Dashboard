import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Streamlit settings
st.set_page_config(page_title="📊 Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard - June & July 2022")

# 🔹 Load CSV/Excel from local path
# Change the file path as per your system
file_path = r"C:\Users\vinuv\Downloads\Data\Sample Data 2 (2) (1) (1).xls - Sales data.csv"   

if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

# Convert date column
if "Sales Date" in df.columns:
    df['Sales Date'] = pd.to_datetime(df['Sales Date'], errors='coerce')

# Data Preview
with st.expander("👀 Preview Data"):
    st.dataframe(df.head(20))

# Sidebar Filters
st.sidebar.header("🔎 Filters")
if "Sales Date" in df.columns:
    date_range = st.sidebar.date_input(
        "Select Date Range",
        [df['Sales Date'].min(), df['Sales Date'].max()]
    )
else:
    date_range = None

selected_status = st.sidebar.multiselect("Payment Status", df['Payment Status'].unique(), default=df['Payment Status'].unique())
selected_source = st.sidebar.multiselect("Source", df['Source'].unique(), default=df['Source'].unique())
selected_currency = st.sidebar.multiselect("Currency", df['Currency  Code'].unique(), default=df['Currency  Code'].unique())

# Apply Filters
df_filtered = df.copy()
if date_range:
    df_filtered = df_filtered[
        (df['Sales Date'] >= pd.to_datetime(date_range[0])) &
        (df['Sales Date'] <= pd.to_datetime(date_range[1]))
    ]

df_filtered = df_filtered[
    (df_filtered['Payment Status'].isin(selected_status)) &
    (df_filtered['Source'].isin(selected_source)) &
    (df_filtered['Currency  Code'].isin(selected_currency))
]

# Tabs for navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📌 Key Metrics", "📈 Charts", "🏆 Products", "🧑‍🤝‍🧑 Customers", "📝 Insights"])

# KPIs
with tab1:
    total_sales = df_filtered['Product Amount with GST'].sum()
    paid_orders = df_filtered[df_filtered['Payment Status'] == 'paid'].shape[0]
    initiated_orders = df_filtered[df_filtered['Payment Status'] == 'Initiated'].shape[0]
    refund_orders = df_filtered[df_filtered['Payment Status'] == 'refund'].shape[0]
    conversion_rate = (paid_orders / (paid_orders + initiated_orders) * 100) if (paid_orders + initiated_orders) > 0 else 0
    avg_order_value = df_filtered['Product Amount with GST'].mean()
    total_orders = df_filtered.shape[0]

    st.markdown("### 📌 Key Metrics")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
    col2.metric("✅ Paid Orders", paid_orders)
    col3.metric("❌ Refund Orders", refund_orders)
    col4.metric("⚡ Conversion Rate", f"{conversion_rate:.2f}%")
    col5.metric("📦 Avg. Order Value", f"₹{avg_order_value:,.0f}")

# Charts
with tab2:
    st.subheader("📈 Sales Trend Over Time")
    sales_trend = df_filtered.groupby("Sales Date")["Product Amount with GST"].sum().reset_index()
    fig = px.line(sales_trend, x="Sales Date", y="Product Amount with GST", markers=True, title="Sales Over Time")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📊 Sales by Source")
    fig = px.bar(df_filtered.groupby("Source")["Product Amount with GST"].sum().reset_index(),
                 x="Source", y="Product Amount with GST", color="Source", title="Sales by Source")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📌 Payment Status Distribution")
    fig = px.pie(df_filtered, names="Payment Status", title="Payment Status Split")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔥 Sales Heatmap (Day vs Amount)")
    df_filtered['Day'] = df_filtered['Sales Date'].dt.day
    pivot = df_filtered.pivot_table(index=df_filtered['Sales Date'].dt.weekday,
                                    columns='Day',
                                    values='Product Amount with GST',
                                    aggfunc='sum')
    fig, ax = plt.subplots(figsize=(10,4))
    sns.heatmap(pivot, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

# Top Products
with tab3:
    st.subheader("🏆 Top 10 Best-Selling Products")
    top_products = df_filtered.groupby("Product Code")["Product Amount with GST"].sum().sort_values(ascending=False).head(10)
    fig = px.bar(top_products, x=top_products.index, y=top_products.values, title="Top Products", labels={'x':'Product Code','y':'Sales'})
    st.plotly_chart(fig, use_container_width=True)

# Top Customers
with tab4:
    st.subheader("🧑‍🤝‍🧑 Top 5 Customers by Sales")
    if "Customer ID" in df_filtered.columns:
        top_customers = df_filtered.groupby("Customer ID")["Product Amount with GST"].sum().sort_values(ascending=False).head(5).reset_index()
        st.table(top_customers)
    else:
        st.info("Customer ID column not found in dataset.")

# Insights
with tab5:
    st.subheader("📝 Insights & Recommendations")
    avg_sales = df_filtered['Product Amount with GST'].mean()
    top_source = df_filtered.groupby("Source")["Product Amount with GST"].sum().idxmax()
    top_product = top_products.index[0] if not top_products.empty else "N/A"

    st.markdown(f"""
    - ✅ Paid orders: **{paid_orders}** out of {len(df_filtered)} total transactions.  
    - ⚡ Conversion rate: **{conversion_rate:.2f}%** — improving checkout flow could raise this.  
    - ❌ Refund orders: **{refund_orders}**, reduce by enhancing product quality or payment experience.  
    - 📢 Highest sales source: **{top_source}** — invest more in this channel.  
    - 🏆 Top product: **{top_product}** — promote this with bundles/discounts.  
    - 💰 Average order value: ₹{avg_sales:,.0f}.  
    """)
