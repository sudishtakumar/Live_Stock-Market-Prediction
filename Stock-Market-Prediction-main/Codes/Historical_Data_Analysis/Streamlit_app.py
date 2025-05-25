"""

This Streamlit application is designed for a comprehensive stock market prediction project. It includes functionality for navigating different project sections, visualizing data, evaluating models, and predicting stock prices using preprocessed datasets. The app incorporates background customization, dropdown and radio button inputs, and interactive visualizations.

This script is used for the deployed app on Streamlit.

Libraries used:
- Streamlit: For building the web-based interactive application framework.
- Pandas: Used for data manipulation and analysis, especially with data frames.
- OS: For handling file and directory paths within the system.
- Matplotlib: Used for generating static plots and charts.
- NumPy: For numerical computations and array operations.
- Plotly: For creating interactive and dynamic visual plots.
- Pickle: Used for loading pre-trained machine learning models.
- Scikit-learn (implied): For model handling and text feature extraction.
- TextBlob: For basic natural language processing tasks.

Functions are explained below:

This Streamlit app provides an interactive platform for analyzing stock market data and models, including numerical, text-based, and hybrid approaches. The app allows users to explore data, view visualizations, evaluate models, and make predictions.

Functions Used:
- display_stock_market_description: Shows a detailed description of the stock market.
- display_project_description: Provides an overview of the project goals and scope.
- display_company_data_table: Displays a table of company-related data.
- display_numerical_dataset_info: Shows information about numerical datasets.
- display_numerical_data_visualizations: Displays visualizations for numerical datasets.
- display_numerical_model_performance: Shows evaluation metrics for numerical models.
- display_numerical_model_visualization: Visualizes numerical model outputs.
- display_numerical_model_predicted: Predicts stock closing prices.
- display_text_model_performance: Evaluates text-based model performance.
- display_text_model_visualization: Visualizes outputs from text-based models.
- display_text_model_prediction: Makes predictions using text-based models.
- display_hybrid_model_performance: Evaluates hybrid model performance.
- display_hybrid_model_visualization: Visualizes outputs from hybrid models.
- display_hybrid_model_prediction: Predicts using hybrid models.
- display_project_database: Provides information on InfluxDB database setup.
- display_project_dashboard: Links or embeds the Grafana dashboard.
- display_project_flask_app: Links or embeds the Flask app for predictions.
- display_power_bi_dashboard: Displays PowerBI Dashboard Plots
- display_real_time_stock_prediction: Provides real-time stock price predictions using trained models, including live data visualization and trend analysis.
- display_contact_information: Shows contact info for the project team.
- display_resources_information: Lists various project-related resources and illustrations.
"""

# --- STREAMLIT APP & VISUALIZATION FRAMEWORK ---

# Importing Streamlit for building the web-based interactive application framework
import streamlit as st

# Importing all functions
from Import_Functions_Deployed import *

# Setting the page title
# This title will only be visible when running the app locally.
# In the deployed app, the title will be displayed as "Title - Streamlit," where "Title" is the one we provide.
# If we don't set the title, it will default to "Streamlit"
st.set_page_config(page_title="Stock Prediction")

# To show Font Awesome icons
css_example = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"> """


# Directory containing the preprocessed datasets
DATASET_DIR = "Codes/Historical_Data_Analysis/Preprocessed_Dataset"


# Directory containing the preprocessed datasets
DATASET_DIR_1 = "Codes/Historical_Data_Analysis"


# Main function to handle the selection and display of sections
def main():
    """
    Main function that sets up the app's navigation, displays content based on user selection,
    and includes links to the GitHub repository.
    It also presents an interactive and visually appealing sidebar with emoji-enhanced radio options
    to enhance user engagement.
    """
    st.title("Stock Market Prediction")

    # Sidebar navigation for different sections
    st.sidebar.title("Explore")
    selected_section = st.sidebar.radio(
        "Go to",
        [
            "Stock Market Description 📈",
            "Project Description 🧾",
            "Companies 🏢",
            "Numerical Dataset Information 🔢",
            "Numerical Dataset Visualization 📊",
            "Numerical Model Evaluation ✅",
            "Numerical Model Visualization 📉",
            "Numerical Model Prediction 🎯",
            "Text Model Evaluation 🔍",
            "Text Model Visualization 📝",
            "Text Model Prediction 💡",
            "Hybrid Model Evaluation ⚙️",
            "Hybrid Model Visualization 🧮",
            "Hybrid Model Prediction 🧠",
            "InfluxDB Database 🗄️",
            "Grafana Dashboard 📟",
            "Flask App ⚗️",
            "PowerBI Dashboard ⚡",
            "Real Time Prediction ⏱️",
            "Reddit Chatbot 🤖",
            "Meet the Team 👥",
            "Resources 📚",
        ],
    )

    # Include Font Awesome CSS for icons
    st.sidebar.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <div class="sidebar-content">
            <h1><a href="https://github.com/madhurimarawat/Stock-Market-Prediction" target="_blank">
                    <i class="fab fa-github"></i> &nbsp; Visit Repository
                </a></h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Call respective functions based on the selected section
    if selected_section == "Stock Market Description 📈":
        """
        Provides an introduction and overview of the stock market,
        covering key concepts and market behaviors.
        """
        display_stock_market_description()

    elif selected_section == "Project Description 🧾":
        """
        Gives a concise description of the project objectives,
        methodology, and expected outcomes.
        """
        display_project_description()

    elif selected_section == "Companies 🏢":
        """
        Displays a table containing company data, such as stock prices and financial metrics,
        allowing users to compare different companies.
        """
        display_company_data_table()

    elif selected_section == "Numerical Dataset Information 🔢":
        """
        Displays detailed dataset information for the selected ticker symbol.
        Users can explore the dataset using a sidebar dropdown.
        """
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        display_numerical_dataset_info(ticker_symbol)

    elif selected_section == "Numerical Dataset Visualization 📊":
        """
        Shows visual representations of stock data, such as price trends
        and volume analysis for the selected ticker symbol.
        """
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        display_numerical_data_visualizations(ticker_symbol)

    elif selected_section == "Numerical Model Evaluation ✅":
        """
        Displays performance statistics for numerical models,
        including accuracy, RMSE, and other metrics.
        """
        display_numerical_model_performance()

    elif selected_section == "Numerical Model Visualization 📉":
        """
        Provides visualizations of numerical model predictions and actual results
        to help users understand model performance.
        """
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )
        display_numerical_model_visualization(ticker_symbol)

    elif selected_section == "Numerical Model Prediction 🎯":
        """
        Offers a prediction feature where users can input values manually
        or select data from a dataset to predict stock closing prices.
        """
        ticker_symbol = st.sidebar.selectbox(
            "Select Dataset (Ticker Symbol)",
            ["AAPL", "GOOG", "AMZN", "META", "MSFT", "NFLX", "NVDA", "TCS"],
        )

        input_method = st.radio(
            "Select Input Method", ("Manual Input", "Select from Dataset")
        )

        if input_method == "Manual Input":
            open_price = st.number_input(
                "Enter Open Price ($)", min_value=0.0, format="%.2f"
            )
            high = st.number_input("Enter High Price ($)", min_value=0.0, format="%.2f")
            low = st.number_input("Enter Low Price ($)", min_value=0.0, format="%.2f")
            volume = st.number_input("Enter Volume", min_value=0, format="%d")

            if st.button("Predict Closing Price"):
                display_numerical_model_predicted(
                    ticker_symbol, open_price, high, low, volume
                )

        else:
            df = pd.read_csv(
                os.path.join(DATASET_DIR, f"Preprocessed_{ticker_symbol}_Dataset.csv"),
                index_col="date",
                parse_dates=True,
            )
            date_options = df.index.strftime("%Y-%m-%d").tolist()
            selected_date = st.selectbox("Select Date", date_options)
            selected_row = df.loc[selected_date]

            open_price = selected_row["open"]
            high = selected_row["high"]
            low = selected_row["low"]
            volume = selected_row["volume"]
            close = selected_row["close"]

            st.write(f"### Using values for {selected_date}:")
            st.write(
                f"<p>Open Price: <strong>${open_price:.2f}</strong> &nbsp;&nbsp; "
                f"High: <strong>${high:.2f}</strong> &nbsp;&nbsp; "
                f"Low: <strong>${low:.2f}</strong> &nbsp;&nbsp; "
                f"Volume: <strong>{volume}</strong></p> "
                f"Close: <strong>${close:.2f}</strong></p>",
                unsafe_allow_html=True,
            )

            if st.button("Predict Closing Price"):
                display_numerical_model_predicted(
                    ticker_symbol, open_price, high, low, volume
                )

    elif selected_section == "Text Model Evaluation 🔍":
        """
        Displays performance metrics of the text-based model,
        including precision, recall, and F1-score.
        """
        display_text_model_performance()

    elif selected_section == "Text Model Visualization 📝":
        """
        Shows visualizations related to the output of the text-based model,
        such as word clouds and sentiment analysis charts.
        """
        display_text_model_visualization()

    elif selected_section == "Text Model Prediction 💡":
        """
        Provides a text-based prediction tool that analyzes sentiment
        and correlates it with stock price trends.
        """
        display_text_model_prediction()

    elif selected_section == "Hybrid Model Evaluation ⚙️":
        """
        Evaluates the combined performance of numerical and text-based models,
        showing how well the hybrid approach works.
        """
        display_hybrid_model_performance()

    elif selected_section == "Hybrid Model Visualization 🧮":
        """
        Displays visual outputs of the hybrid model, highlighting predictions
        and actual stock price trends.
        """
        display_hybrid_model_visualization()

    elif selected_section == "Hybrid Model Prediction 🧠":
        """
        Predicts stock prices using a hybrid model that integrates numerical
        and text-based data for better accuracy.
        """
        display_hybrid_model_prediction()

    elif selected_section == "InfluxDB Database 🗄️":
        """
        Provides an overview of the InfluxDB database setup used for storing
        and querying time-series data.
        """
        display_project_database()

    elif selected_section == "Grafana Dashboard 📟":
        """
        Displays a link or an embedded Grafana dashboard that visualizes real-time
        data monitoring for stock analysis.
        """
        display_project_dashboard()

    elif selected_section == "Flask App ⚗️":
        """
        Links or embeds the Flask app, enabling users to access prediction features
        through a separate web service.
        """
        display_project_flask_app()

    elif selected_section == "PowerBI Dashboard ⚡":
        """
        Displays a collection of plots created using Power BI for historical stock data analysis.
        The plots are hosted in the GitHub repository and dynamically rendered using Streamlit.
        Helps users visualize trends and insights from historical stock performance.
        """
        display_power_bi_dashboard()

    elif selected_section == "Real Time Prediction ⏱️":
        """
        Displays the real-time stock prediction interface using the latest data.
        Allows users to input stock ticker symbols and view forecasted results.
        """
        display_real_time_stock_prediction()

    elif selected_section == "Reddit Chatbot 🤖":
        """
        Displays the Reddit Chatbot interface that fetches real-time data using the Reddit API.
        Allows users to interact with the chatbot, retrieve relevant discussions, and visualize
        data trends through plots and insights gathered from Reddit posts and comments.
        """
        display_reddit_chatbot_visualization()

    elif selected_section == "Meet the Team 👥":
        """
        Introduces the team members working on the project and provides
        their contact information.
        """
        display_contact_information()

    elif selected_section == "Resources 📚":
        """
        Lists resources and links relevant to the project, including stock data
        sources and illustrations.
        """
        display_resources_information()


# Running the main function
if __name__ == "__main__":
    # Call function to display the background image with opacity
    display_background_image(
        "https://vectormine.b-cdn.net/wp-content/uploads/Stock_Market.jpg", 0.8
    )

    # Call main function to run the app
    main()
