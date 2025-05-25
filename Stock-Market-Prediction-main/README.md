# Stock-Market-Prediction

** for data analysis and visualization.**


![📈 Stock Market Illustration](https://github.com/user-attachments/assets/f5751f74-43c5-4045-aa9f-bb7abd19c1aa)

<p align=center>
<a href="https://stock-market-numerical-text-hybrid-prediction.streamlit.app/">
  <img src="\Codes\Historical_Data_Analysis\App_Snapshots\Streamlit_App\App_Working_Real_Time_Prediction.gif" alt="💡 Real Time Prediction" title="💡 Real Time Prediction" height="300px">
</a></p>

## Project Description

The **Advanced Stock Price Forecasting Using a Hybrid Model of Numerical and Textual Analysis** project involves a comprehensive approach to predicting stock prices using both numerical data and textual analysis. The project components include:

1. **Data Collection and Storage**: We gathered historical stock data of major companies and stored it in an InfluxDB database to efficiently handle large-scale time-series data.

2. **Data Visualization**: A Grafana dashboard has been set up for real-time visualization of stock prices and analysis results, enhancing data interpretation and decision-making processes.

3. **Textual Analysis for Enhanced Forecasting**: We utilized Natural Language Processing (NLP) libraries, such as NLTK and spaCy, to analyze financial news and reports. This component complements numerical analysis to improve the accuracy of our hybrid forecasting model.

4. **Machine Learning Models**: The project used models including Naive Bayes, MLP (Multi-Layer Perceptron), Logistic Regression, and Random Forest to process both numerical and textual data, creating a robust and comprehensive stock prediction system.

5. **Reddit Chatbot Data Visualization Integration**: The project involved adding static and interactive plots to represent chatbot data from Reddit, using Matplotlib and Seaborn to visualize user interactions, message frequency, and topic distribution effectively.

6. **Collaboration and Project Management**: The repository includes contributions from all team members with well-organized tasks, ensuring seamless collaboration and effective version control.

## Directory Structure

```markdown
📁 Stock-Market-Prediction/
├── 📁 Codes/                            # 🧠 Core code modules for analysis and app development
│   ├── 📁 Historical_Data_Analysis/     # 📊 Scripts for long-term market trend analysis
│   ├── 📁 Partial_Data_Analysis/        # 📉 Focused short-term or segmented data analysis
│   ├── 📁 Ticker_Symbols_Stocks/        # 💹 Scripts for retrieving and managing ticker symbols
│   ├── 📁 Flask_App/                    # 🌐 Web interface built using Flask framework
│
├── 📁 Conferences/                      # 🎤 Presentation and academic conference materials
│
├── 📁 Documents/                        # 📚 Miscellaneous reports and supporting documents
│   ├── 📁 Major_Project/                # 🏆 Final-year major project resources
│   │   ├── 📁 PPT/                      # 📽️ Presentation slides for the major project
│   │   ├── 📁 Proforma_&_Progress_Report/ # 📝 Official progress reports and planning forms
│   │   └── 📁 Thesis/                   # 📖 Final thesis document with research and results
│   │
│   └── 📁 Minor_Project/                # 🎯 Minor-project materials
│       ├── 📁 PPT/                      # 🧾 Slides prepared for minor project presentation
│       ├── 📁 Proforma_&_Progress_Report/ # 📋 Progress reports and planning forms for minor project
│       └── 📁 Thesis/                   # 📘 Final minor project report or thesis
│
├── 📁 Reference_Documents/             # 🔍 Research papers and helpful external references
│
├── 📁 Resources/                       # 🛠️ Datasets, libraries, and supporting tools
│
├── 📄 LICENSE                          # 📄 Terms and conditions for usage and distribution
└── 📄 README.md                        # 📘 Overview, setup guide, and project introduction
```

### 📄 Thesis Reports

> 📖 Major & Minor Project Reports
> Detailed thesis reports for both major and minor projects are available under their respective [`Thesis`](Documents/Thesis/) folders in [`Documents/`](Documents/).

### 🗃️ InfluxDB Setup Guide

> 📖 Time-Series Data Storage & Integration
> Step-by-step InfluxDB setup and data integration guide is available at [`Codes/Historical_Data_Analysis/InfluxDB/`](Codes/Historical_Data_Analysis/InfluxDB/).

### 📊 Grafana Dashboard Guide

> 📖 Visualization Dashboard Setup
> Grafana dashboard setup and InfluxDB connection guide is available at [`Codes/Historical_Data_Analysis/Grafana_Dashboard/`](Codes/Historical_Data_Analysis/Grafana_Dashboard/).

---

## Dataset Used

| Company                           | Description                                                                                     | Data Range           | Dataset Shape | Starting Stock Date | Current Stock Date | Starting Stock Price | Current Stock Price |
|-----------------------------------|-------------------------------------------------------------------------------------------------|----------------------|---------------|---------------------|--------------------|----------------------|----------------------|
| <img src="https://www.freepnglogos.com/uploads/google-logo-png/google-logo-png-suite-everything-you-need-know-about-google-newest-0.png" height="40"> <br> Alphabet Inc. (Google) [GOOG] | Specializes in Internet-related services and products, including search engines, online advertising, and cloud computing. | 2014-03-27 : 2024-10-17 | (2659, 5) | 2014-03-27          | 2024-10-17         | $27.8542             | $164.51              |
| <img src="https://pngimg.com/uploads/amazon/amazon_PNG5.png" height="40"> <br> Amazon.com Inc. [AMZN]    | Started as an online bookstore, now a leader in e-commerce and cloud computing through AWS. | 1997-05-16 : 2024-10-17 | (6901, 5) | 1997-05-16          | 2024-10-17         | $0.0863              | $187.53              |
| <img src="https://th.bing.com/th/id/R.0ac491574e7ddb71dc2cab65a8bb501f?rik=5NzURUJ1L37UYg&riu=http%3a%2f%2fpurepng.com%2fpublic%2fuploads%2flarge%2fpurepng.com-apple-logologobrand-logoiconslogos-251519938788qhgdl.png&ehk=kQ%2bTI4imrP%2fg9UWIfehFMJOqAn1A3RQTROHV%2f1ORknk%3d&risl=&pid=ImgRaw&r=0" height="40"> <br> Apple Inc. [AAPL]   | Renowned for innovative consumer electronics, software, and services, including the iPhone and Mac computers. | 1980-12-12 : 2024-10-17 | (11053, 5) | 1980-12-12          | 2024-10-17         | $0.0992              | $232.15              |
| <img src="https://static.vecteezy.com/system/resources/previews/024/273/862/original/meta-logo-transparent-free-png.png" height="40"> <br> Meta Platforms [META] | Owner of Facebook, a global leader in social media and digital advertising. | 2012-05-18 : 2024-10-17 | (3124, 5) | 2012-05-18          | 2024-10-17         | $38.1174             | $576.93              |
| <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg" height="40"> <br> Microsoft Corp. [MSFT] | A leading developer of software, consumer electronics, and personal computers. | 1986-03-13 : 2024-10-17 | (9728, 5) | 1986-03-13          | 2024-10-17         | $0.0603              | $416.72              |
| <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg" height="40"> <br> Netflix Inc. [NFLX] | Global streaming entertainment service with a vast library of TV series and films. | 2002-05-23 : 2024-10-17 | (5640, 5) | 2002-05-23          | 2024-10-17         | $1.1964              | $687.65              |
| <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/235_Nvidia_logo-512.png" height="40"> <br> Nvidia Corp. [NVDA] | Specializes in graphics processing units and AI technology. | 1999-01-22 : 2024-10-17 | (6477, 5) | 1999-01-22          | 2024-10-17         | $0.0377              | $136.93              |
| <img src="https://companieslogo.com/img/orig/TCS.NS-7401f1bd.png?t=1631949260" height="40"> <br> Tata Consultancy Services [TCS] | Leading global IT services, consulting, and business solutions provider. | 2013-11-01 : 2024-10-17 | (2758, 5) | 2013-11-01          | 2024-10-17         | $543.0               | $11.8                |

---

## Tools and Technologies

1. **Python**: Core programming language used for data analysis, model building, and backend development.
2. **GitHub**: Platform for version control and collaborative development.
3. **InfluxDB**: Database for efficient time-series data storage and retrieval.
4. **Grafana**: Tool for real-time data visualization and dashboard creation.
5. **Streamlit**: Framework for creating interactive web applications.
6. **Flask**: Lightweight framework for developing the project’s backend.
7. **Pandas**: Library for data manipulation and analysis.
8. **Matplotlib & Plotly**: Libraries for data visualization and graphical representation.
9. **NLP Libraries (NLTK, spaCy)**: Tools for processing and analyzing text data.
10. **Machine Learning Libraries**: Used for implementing models like Naive Bayes, MLP, Logistic Regression, and Random Forest.

---

## Project Database & Dashboard

For easy visualization and data management, we are using the following tools:

### InfluxDB Database 

### 1. Numerical Analysis
![Numerical Analysis Snapshot](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Numerical_Analysis_1.png)

### 2. Model Prediction
![Model Prediction Snapshot](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Model_Prediction_1.png)

### 3. Textual Analysis
![Textual Analysis Snapshot](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Textual_Analysis_1.png)

### 4. Hybrid Model
![Hybrid Model Snapshot](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/InfluxDB_Database/Hybrid_Model_1.png)
`

### Grafana Dashboard

### 1. Stock Market and Project Dashboard Overview
This section provides an overview of the stock market, project details, and descriptions of the companies used in the project, 
including MAANG, Nvidia, Microsoft, and TCS.

![Stock Market Overview Snapshot 1](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_1.png)
![Stock Market Overview Snapshot 2](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Dashboard_Description_and_Datasets_Information_View_1.png)
![Stock Market Overview Snapshot 3](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Dashboard_Description_and_Datasets_Information_View_2.png)
![Stock Market Overview Snapshot 4](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Stock_Market_and_Project_Dashboard_Overview/Dashboard_Panel_Stock_Market_View_1.png)

### 2. Numerical Analysis
This section displays numerical data of the stock market, featuring graphs of open, high, low, and close prices 
along with volume bar plots, RSI, and moving averages.

![Numerical Analysis Snapshot 1](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_1.png)
![Numerical Analysis Snapshot 2](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_2.png)
![Numerical Analysis Snapshot 3](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Numerical_Analysis/Dashboard_3.png)

### 3. Model Prediction
This section highlights model predictions, including individual and comparative graphs of predicted and actual values 
for stock prices, as well as predicted RSI and moving averages.

![Model Prediction Snapshot 1](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_1.png)
![Model Prediction Snapshot 2](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_2.png)
![Model Prediction Snapshot 3](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Model_Prediction/Dashboard_Panel_Model_Evaluation_View.png)

### 4. Textual Analysis
This section visualizes sentiment analysis from news headlines, showcasing positive, negative, and neutral sentiment scores.

![Textual Analysis Snapshot 1](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Textual_Analysis/Dashboard_1.png)
![Textual Analysis Snapshot 2](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Textual_Analysis/Dashboard_2.png)

### 5. Hybrid Model
The hybrid model combines numerical and textual data for a comprehensive analysis.

![Hybrid Model Snapshot 1](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_1.png)
![Hybrid Model Snapshot 2](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_2.png)
![Hybrid Model Snapshot 3](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_3.png)
![Hybrid Model Snapshot 4](https://github.com/madhurimarawat/Stock-Market-Prediction/raw/main/Codes/Historical_Data_Analysis/Database_Dashboard_Snapshots/Grafana_Dashboard/Hybrid_Model/Dashboard_4.png)
        
---

### Project Deployment

1. **Streamlit:**
The app is deployed at: &nbsp; [Stock Market Numerical and Text Hybrid Prediction](https://stock-market-numerical-text-hybrid-prediction.streamlit.app/)

Here's an overview of the Streamlit App:

<a href="https://stock-market-numerical-text-hybrid-prediction.streamlit.app/" target="_blank">
  <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/blob/main/Codes/Historical_Data_Analysis/App_Snapshots/Streamlit_App/App_View_1.png" 
       alt="Streamlit App View 1" 
       title="Streamlit App View 1">
</a>

<a href="https://stock-market-numerical-text-hybrid-prediction.streamlit.app/" target="_blank">
  <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/blob/main/Codes/Historical_Data_Analysis/App_Snapshots/Streamlit_App/App_View_2.png" 
       alt="Streamlit App View 2" 
       title="Streamlit App View 2">
</a>

<a href="https://stock-market-numerical-text-hybrid-prediction.streamlit.app/" target="_blank">
  <img src="https://github.com/madhurimarawat/Stock-Market-Prediction/blob/main/Codes/Historical_Data_Analysis/App_Snapshots/Streamlit_App/App_View_3.png" 
       alt="Streamlit App View 3" 
       title="Streamlit App View 3">
</a>


3. **Flask:**
The app codes can be seen here: [Flask App Codes](https://github.com/madhurimarawat/Stock-Market-Prediction/tree/main/Codes/Flask_App).

Here's an overview of the Flask App:

![Flask App GIF](https://github.com/user-attachments/assets/86f149d3-d746-4008-8a0c-6dfd6f539f54)


---

## Meet the Team

<table align="center"> <tr> <th> </th> <th><b>Sudishta kumar yadav</b></th> </tr> <tr> <td> <picture> <source srcset="https://static.vecteezy.com/system/resources/previews/024/405/365/original/briefcase-icon-isolated-white-background-png.png" media="(prefers-color-scheme: dark)"> <img width="30" src="https://img.icons8.com/ios-glyphs/30/000000/briefcase.png" alt="Role"> </picture><br><b>Role</b> </td> <td>Project Planner & Developer</td> <td>Data l.com">Email</a></td> </tr> </table>

---

## Resources

1. **Partial Data Analysis**:
   - Historical Stock Prices: [Yahoo Finance](https://finance.yahoo.com/)
   - **Textual and Hybrid Data:**
        - [Kaggle Dataset - News & Stock Prices](https://www.kaggle.com/datasets/kianso/news-stock-price)

2. **Complete Historical Data**:
  - **Alphabet (Google) (GOOG)**: [Google Stock Price](https://www.macrotrends.net/stocks/charts/GOOG/google/stock-price-history)
   - **Apple (AAPL)**: [Apple Stock Price](https://www.macrotrends.net/stocks/charts/AAPL/apple/stock-price-history)
   - **Amazon (AMZN)**: [Amazon Stock Price](https://www.macrotrends.net/stocks/charts/TCS/container-store/stock-price-history)
   - **Meta (META)**: [Meta Stock Price](https://www.macrotrends.net/stocks/charts/META/meta-platforms/stock-price-history)
   - **Netflix (NFLX)**: [Netflix Stock Price](https://www.macrotrends.net/stocks/charts/NFLX/netflix/stock-price-history)
   - **Nvidia (NVDA)**: [Nvidia Stock Price](https://www.macrotrends.net/stocks/charts/NVDA/nvidia/stock-price-history)
   - **Microsoft (MSFT)**: [Microsoft Stock Price](https://www.macrotrends.net/stocks/charts/MSFT/microsoft/stock-price-history)
   - **TCS**: [TCS Stock Price](https://www.macrotrends.net/stocks/charts/TCS/container-store/stock-price-history)

3. **Illustration Links:**
   - [Project Resources (Illustration 1)](https://img.freepik.com/premium-vector/flat-design-stock-market-analysis_23-2148590818.jpg)
   - [Streamlit App Background Image (Illustration 2)](https://vectormine.b-cdn.net/wp-content/uploads/Stock_Market.jpg)

---

## Thanks for Visiting 😄

- Drop a 🌟 if you find this repository useful.<br><br>
- If you have any doubts or suggestions, feel free to reach us.<br><br>
- **Contribute and Discuss:** Feel free to open <a href= "https://github.com/madhurimarawat/Stock-Market-Prediction/issues">issues 🐛</a>, submit <a href = "https://github.com/madhurimarawat/Stock-Market-Prediction/pulls">pull requests 🛠️</a>, or start <a href = "https://github.com/madhurimarawat/Stock-Market-Prediction/discussions">discussions 💬</a> to help improve this repository!
