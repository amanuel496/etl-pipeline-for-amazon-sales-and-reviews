# **ETL Pipeline for Amazon Sales and Reviews**

🚀 A fully automated **ETL (Extract, Transform, Load) pipeline** designed to process Amazon sales and review data. The project extracts raw data from CSV files, cleans and transforms it, and loads it into a **PostgreSQL** database using `psycopg2`.

📊 **Dataset Source**: [Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset/data) by **Karkavel Raja**.

## **Key Features**
✅ **Extract**: Load raw sales and review data from CSV files.  
✅ **Transform**: Clean missing values, handle duplicates, remove outliers, and standardize text.  
✅ **Load**: Store structured data in **PostgreSQL** using `psycopg2`.  
✅ **Analyze**: Perform SQL queries for **sales insights** and **customer sentiment analysis**.  
✅ **Scalable**: Can be integrated with **AWS RDS** or **Google Cloud SQL** for cloud deployment.  

## **Tech Stack**
- 🐍 **Python** (pandas, logging)  
- 🗄 **PostgreSQL** (Data storage & query execution)  
- 🔌 **psycopg2** (PostgreSQL adapter for Python)  
- 📊 **Jupyter Notebook / SQL Queries** (Data analysis & visualization)  

## **Setup Instructions**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/amanuel496/etl-pipeline-for-amazon-sales-and-reviews.git
cd etl-pipeline-for-amazon-sales-and-reviews
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Configure Database**
- Ensure **PostgreSQL** is installed and running.  
- Create a **database** named `amazon_sales`.  
- Update **database credentials** in `config.py`.  

### **4️⃣ Run the ETL Pipeline**
```bash
python etl.py
```

## **Credits**
- **Dataset:** [Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset/data) by **Karkavel Raja**.  
- **Database Adapter:** [psycopg2](https://www.psycopg.org/docs/) - PostgreSQL adapter for Python.  

🚀 **Transform raw data into meaningful insights with this powerful ETL pipeline!**
