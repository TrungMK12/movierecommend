# 🎬 Movie Recommendation System

Ứng dụng web gợi ý phim được xây dựng bằng **Python, Streamlit và Machine Learning**.  
Dữ liệu phim được xử lý bằng **pandas** và mô hình gợi ý dựa trên **similarity (cosine similarity)**.

---

## 🚀 Tính năng
    - Gợi ý 5 bộ phim tương tự khi bạn chọn 1 bộ phim yêu thích.
    - Hiển thị **poster phim + tên phim** trực quan.
    - Giao diện web đơn giản, dễ sử dụng (Streamlit).

---

## 🛠️ Công nghệ sử dụng
    - **Python 3.9+**
    - [Streamlit](https://streamlit.io/) (frontend web)
    - [pandas](https://pandas.pydata.org/)
    - [scikit-learn](https://scikit-learn.org/)
    - pickle (lưu mô hình & dữ liệu)

---

## 📂 Cấu trúc project
    MovieRecommendSystem
    ├── data/                     
    │   ├── tmdb_5000_movies.csv
    │   ├── tmdb_5000_credits.csv
    │
    ├── utils/                    
    │   ├── movies.pkl            
    │   ├── similarity.zip        
    │
    ├── app.py                   
    ├── MovieRecommend.ipynb      
    ├── requirements.txt         
    ├── README.md                

---

## ⚙️ Cài đặt & chạy
    1. Clone repo
       git clone https://github.com/TrungMK12/MovieRecommendSystem
       cd MovieRecommendSystem
    2. Tạo virtual environment
       python -m venv .venv
       Kích hoạt:
           Windows (PowerShell):
               .venv\Scripts\Activate
           Mac/Linux:
               source .venv/bin/activate
    3. Cài dependencies
       pip install -r requirements.txt
    4. Chạy ứng dụng
       streamlit run app/app.py




