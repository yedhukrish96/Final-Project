![Kivafinal](https://user-images.githubusercontent.com/123810799/233998913-a6c5b985-81b1-4f41-a5e8-ee031023ad2c.png)
# KIVA Crowdfunding Data Exploration
## Data-Driven Analysis and Loan Amount Prediction of Kiva Crowdfunding and EDA on various aspects.
* Yedhu Krishnan
* Iron Hack, April - 2023

The KIVA loan prediction app is a machine learning web application that predicts the maximum loan amount that a user can borrow from KIVA, a nonprofit organization that offers microloans to people in need around the world. The app allows users to input their personal and loan-related details, and then uses a machine learning model to predict the loan amount. The app also includes an exploratory data analysis (EDA) section where users can explore the KIVA loan dataset, and a conclusion section that summarizes the findings of the project.

### Overview
* This project is a web application built using Streamlit that predicts the loan amount that a borrower can apply for on the Kiva platform
* In addition to loan prediction, the application also provides exploratory data analysis (EDA) of the Kiva loan dataset, allowing users to visualize and explore various loan characteristics such as loan amount, sector, and repayment intervals. 
* Overall, this project aims to provide a useful tool for potential Kiva borrowers and anyone interested in learning more about microfinance and poverty alleviation efforts.

### Part 1: Web Scraping
This section involves web-scraping from the official website of KIVA using GraphQL API method.

### Part 2: Data Cleaning and Wrangling
In Part 1 of the project, we focus on data cleaning and wrangling. This involves handling missing values, removing duplicates, and converting data types as needed. 

### Part 3: Exploratory Data Analysis
In this section, we analyze the cleaned and wrangled data to gain insights about the Kiva loans. We explore different variables like loan amount, loan term, borrower gender, sector-wise loan distribution, geographical distribution of loans, and more. We use various visualization techniques like histograms, bar charts, pie charts, and maps to present our findings. Our aim is to identify trends and patterns in the data that can help us understand the borrowers' needs and the effectiveness of Kiva's lending model.

### Part 4: Predictive Modeling
* In this section, we applied K-Nearest Neighbors (KNN) algorithm to predict the loan amount that borrowers can borrow. We used the cleaned and preprocessed dataset obtained from the previous section to train and test our model. We used the scikit-learn library to implement the KNN algorithm.

* After tuning the hyperparameters, our model achieved an R2 score of 0.86, indicating that our model explains 86% of the variance in the loan amount data. In addition, we also calculated the mean squared error (MSE) and root mean squared error (RMSE) scores, and the rmse score i obtained was 453. These scores indicate that our model's predictions have an average error of [insert error value here].

* Overall, our predictive model provides a useful tool for borrowers to estimate the loan amount they can borrow based on their personal and loan-related information.

### Part 5 : Using the Web-Scraped data as a Validation Set to make Predictions
In this section, I opened a new Jupyter notebook and used the web-scraped data as a validation set to predict the loan amount. As a result of difference in datasets, as the first one I obtained was from Kaggle and the second using web-scraping from the official website of KIVA, there were differences in data and the whole structure. As a result, the model on my validation set performed not as great as my original dataset. However, using better methods to webscrape can prove my model to perform better, something which I undoubtedly wish to venture soon!

### Part 6: StreamLit App- My Loan Prediction Platform
In this part, I built a Streamlit app to allow users to interact with the data and make predictions using the KNN model I developed in Part 3. The app includes three main pages: Home, EDA, and Prediction.

* On the Home page, users are welcomed to the Kiva loan prediction app and can navigate to the other pages using the sidebar menu. The EDA page displays various visualizations of the loan data, including the distribution of loan amounts and the top 20 countries by loan count. 

* The Prediction page allows users to input various loan parameters and receive a predicted loan amount based on the KNN model.

I also added two additional sections to the app: Conclusion and What to Improve. 

* In the Conclusion section, I summarized the findings of the project and provided recommendations for future improvements. 

* The What to Improve section lists potential areas for further development, such as incorporating additional machine learning models and expanding the dataset to include more loan parameters.

Overall, the Streamlit app provides a user-friendly interface for exploring and predicting Kiva loans, and serves as a valuable tool for both loan applicants and Kiva administrators.


### Technologies Used

Python

Jupyter Notebook

Scikit-learn

Pandas

Matplotlib

Seaborn

GraphQL

Requests

StreamLit

### Repository Structure
This folder contains Jupyter Notebooks with the code for the project, including data cleaning, exploratory data analysis, modeling, and evaluation, as well as the dataset I obtained from both Kaggle and Webscraped data.
The second Jupyter notebook consists of the part where I use the webscraped data as a validation set to predict the loan amount.

### Conclusion
* In this project, we used data from Kiva to build a predictive model for loan disbursement. We started by cleaning and preprocessing the data to prepare it for analysis. We then performed exploratory data analysis to gain insights into the loan data and identify patterns and trends.

* Overall, this project demonstrates the potential of machine learning in the lending industry and highlights the importance of data-driven decision making. As with any predictive model, there is always room for improvement, and we have identified several areas for future work.

I hope that this project serves as a useful resource for anyone interested in machine learning and its applications in the financial industry.

### Additional Information
* Kaggle dataset obtained from - https://www.kaggle.com/datasets/kiva/data-science-for-good-kiva-crowdfunding?datasetId=12414&searchQuery=Model+
* Kiva webscraped data obatined from - https://api.kivaws.org/graphql
* Streamlit presentation- https://www.linkedin.com/feed/update/urn:li:activity:7069289318636236800/
