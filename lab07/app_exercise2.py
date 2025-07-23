import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Phân tích dữ liệu thuốc", layout="wide")

st.title("💊 Ứng dụng phân tích dữ liệu thuốc")

# Kiểm tra xem file có tồn tại không
csv_path = "drug200.csv"
if not os.path.exists(csv_path):
    st.error(f"❌ Không tìm thấy file '{csv_path}'. Hãy chắc chắn rằng bạn đã để file này trong cùng thư mục với app.")
    st.stop()

# Đọc dữ liệu
df = pd.read_csv(csv_path)

# Hiển thị bảng dữ liệu gốc
st.subheader("📋 Bảng dữ liệu gốc")
st.dataframe(df)

# Bộ lọc
st.sidebar.header("🔍 Bộ lọc dữ liệu")

age_min = int(df["Age"].min())
age_max = int(df["Age"].max())
age_filter = st.sidebar.slider("Chọn độ tuổi", age_min, age_max, (age_min, age_max))

sex_options = ["All"] + sorted(df["Sex"].unique())
sex_filter = st.sidebar.selectbox("Giới tính", sex_options)

bp_options = ["All"] + sorted(df["BP"].unique())
bp_filter = st.sidebar.selectbox("Huyết áp (BP)", bp_options)

chol_options = ["All"] + sorted(df["Cholesterol"].unique())
chol_filter = st.sidebar.selectbox("Cholesterol", chol_options)

# Lọc dữ liệu
filtered_df = df[
    (df["Age"] >= age_filter[0]) &
    (df["Age"] <= age_filter[1])
]

if sex_filter != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == sex_filter]

if bp_filter != "All":
    filtered_df = filtered_df[filtered_df["BP"] == bp_filter]

if chol_filter != "All":
    filtered_df = filtered_df[filtered_df["Cholesterol"] == chol_filter]

# Hiển thị dữ liệu sau khi lọc
st.subheader("📊 Dữ liệu sau khi lọc")
st.dataframe(filtered_df)

# Biểu đồ số lượng thuốc theo loại
st.subheader("📈 Biểu đồ số lượng thuốc theo loại")
if not filtered_df.empty:
    st.bar_chart(filtered_df["Drug"].value_counts())
else:
    st.warning("⚠️ Không có dữ liệu để hiển thị biểu đồ. Hãy điều chỉnh bộ lọc.")
