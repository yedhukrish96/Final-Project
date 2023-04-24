def eda():
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    
    data1= pd.read_csv('kaggle_cleaned.csv')
    data2= pd.read_csv('kiva_eda.csv')
    
    
    def plot_sector_count(df):
        d = df.groupby('sector').agg(nr=('activity', 'count')).reset_index()
        d = d.sort_values('nr', ascending=False)

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(d['sector'], d['nr'], color='sandybrown', edgecolor='black')
        ax.invert_yaxis()
        ax.set_xlabel('Number of loans')
        ax.set_title('Sector (all)')
        return fig
        
        
    fig1 = plot_sector_count(data1)
    st.write("These are the top 20 Sectors in terms of loans from the year 2013-2017.\n\nAgriculture is the sector with the most number of loans, followed by Food, Retail, Services etc.")
    st.pyplot(fig1)
    
    
    
    fig2 = plot_sector_count(data2)
    st.write("These are the top 20 Sectors in terms of loans just for the year 2023.\n\nIt shows that Clothing showed an increase in loan borrowings.\n\nArts showed a big increase in this year while Wholesale sector showed a slight increase.\n\nHealth and Personal Use sectors went down in terms of loan borrowings.")
    st.pyplot(fig2)

    def activity_count(df):
        d = (
        df.groupby('activity')
            .agg(nr=('sector', 'count'))
            .nlargest(20, columns='nr')
            .reset_index()
            .assign(activity=lambda df: pd.Categorical(df['activity'], 
                                                        df['activity'][::-1],
                                                        ordered=True))
    )

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(d['activity'], d['nr'], color='yellowgreen', edgecolor='black')
        ax.invert_yaxis()
        ax.set_xlabel('Number of loans')
        ax.set_title('Activities (top 20 by number of loans)')
        return fig

    fig3= activity_count(data1)
    st.write("These are the top 20 activities in terms of loans.\n\nAs you see, Farming is the number 1 activity which has obtained the most loans.\n\nFollowed by General store, Personal Housing Expenses etc.")
    st.pyplot(fig3)
             
             
             
    fig4 = activity_count(data2)
    st.write("During the year 2023, Farming is still at the number 1 position as it is a part of the Agriculture sector.\n\nRetail and Clothing Sales shows a huge increase during this year in terms of loan-borrowings.")
    st.pyplot(fig4)
    
    
    

    def country_count(df):
        d3 = (
        df.groupby('country')
        .agg(nr=('sector', 'count'))
        .nlargest(20, columns='nr')
        .reset_index()
        .assign(country=lambda df: pd.Categorical(df['country'], 
                                                   df['country'][::-1],
                                                   ordered=True))
        )

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.barh(d3['country'], d3['nr'], color='tomato', edgecolor='black')
        ax.invert_yaxis()
        ax.set_xlabel('Number of loans')
        ax.set_title('Countries (top 20 by number of loans)')
        return fig

    
    fig5= country_count(data1)
    st.write("The top 20 countries which have borrowed the most number of loans.\n\nPhillipines secure the first place in terms of loan borrowing.\n\nFollowed by Kenya, El Salvador, Cambodia etc.")
    st.pyplot(fig5)
    
    
    fig6 = country_count(data2)
    st.write("During the year 2023, Kenya secured the first place in terms of loan-borrowing.\n\nTajikistan came up over the years and there are countries like Senegal, Indonesia, Fiji which showed a big leap in the list.\n\nIndia which was among the top20 list is no longer visible along with Pakistan and other countries too.")
    st.pyplot(fig6)
    
    
    
    
    def sector_repayment_count(df):
        df = df.groupby(['sector', 'repayment_interval']).size().reset_index(name='nr')

        import seaborn as sns
        import matplotlib.pyplot as plt

        sns.set_style("whitegrid")

        g = sns.catplot(x="sector", y="nr", hue="repayment_interval", data=df,
                    kind="bar", height=6, aspect=2, palette="Set2")

        return g.fig

    fig7 = sector_repayment_count(data1)
    st.write("The graph shows a very clear presentation.\n\nMonthly and Irregular are the most common repayment intervals for almost all the sectors.\n\nIn case of Agriculture, Bullet repayment is almost on par with Irregular.\n\nWholesale sector shows very little graphical data for us to decide. This sector has a very low loan borrowing status.")
    st.pyplot(fig7,width=800, height=600)
    
    
    
    fig8= sector_repayment_count(data2)
    st.write("During the year 2023, Monthly repayment seems to be the most favourite repayment method for almost all sectors.\n\nBullet repayment seems to be ruled out for the year 2023 for unknown reasons.\n\nFor the Agriculture sector, at-the-end and irregular payments dropped considerably but for the other sectors these two payment methods are the least chosen.")
    st.pyplot(fig8,width=800, height=600)
    
    
    
    def gender_borrower_count(df):
        df = df.groupby(['sector', 'mode_gender_of_borrower']).size().reset_index(name='nr')
        sns.set_style("whitegrid")
        fig = sns.catplot(x="sector", y="nr", hue="mode_gender_of_borrower", data=df,
                      kind="bar", height=8, aspect=2, palette="Set2")
        st.write("Now this graph shows the Gender wise loan borrowings.\n\nI had already dropped the original column gender in my dataset because there were over 40 borrowers just for one loan.\n\nSo, I took the mode gender out of that and filled in the value so that the column has just one gender.\n\nBut even so, around 60-70% of the data belonged to one gender per loan. So it does not make a big difference.\n\nAnyways-Most of the loans are owned by Female borrowers in almost all sectors.A small percentage is owned by unknown gender")
        st.pyplot(fig.fig)
    
    gender_borrower_count(data1)
    

    
    
    def gender_borrower_count_2(df):
        df = df.groupby(['sector', 'gender']).size().reset_index(name='nr')
        sns.set_style("whitegrid")
        fig = sns.catplot(x="sector", y="nr", hue="gender", data=df,
                      kind="bar", height=8, aspect=2, palette="Set2")
        st.write("During the year 2023, the graph showed little or no change in the case of Gender-wise loan borrowing.\n\nAgriculture sector experienced a drop whereas, the Food sector showed an increase.\n\nAlthough Gender-wise, Female constitutes the highest share in terms of loan borrowing.")
        st.pyplot(fig.fig)
    
    gender_borrower_count_2(data2)
    
    
    
    
    
    

    
    def loan_vs_lender_scatter(df):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(df['loan_amount'], df['lender_count'], alpha=0.5)
        ax.set_xlabel('Loan Amount')
        ax.set_ylabel('Lender Count')
        ax.set_title('Loan Amount vs. Lender Count')
        st.write("I wanted to explore the relationship between loan amount and lender count by using a scatter plot.\n\nAs you can see as the Loan amount increases, the Lender count also increases.\n\nHowever, this is not always true as there are some loans which have a high value,but with a small number of lenders.")
        st.pyplot(fig)

    loan_vs_lender_scatter(data1)
        
        
     
    def loan_vs_lender_scatter2(df):
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(df['loan_amount'], df['lender_count'], alpha=0.5)
        ax.set_xlabel('Loan Amount')
        ax.set_ylabel('Lender Count')
        ax.set_title('Loan Amount vs. Lender Count')
        st.write("During the year 2023,the relationship between loan amount and lender count is rather less informative.\n\nAs you can see, there are loans with the same amount but with more lenders and some have less lenders.\n\nThere are also a few outliers.")
        st.pyplot(fig)
    
    
    
    loan_vs_lender_scatter2(data2)  
    
    
    
    

    def loan_amount_over_time_line(df):
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.lineplot(x='disbursed_year', y='loan_amount', data=df, estimator=sum, ci=None, ax=ax)
        ax.set_xlabel('Disbursed Year')
        ax.set_ylabel('Total Loan Amount (USD)')
        ax.set_title('Loan Amount over Time')
        return fig
    
    
    fig1 = loan_amount_over_time_line(data1)
    st.write("Let us take a look at the distribution of loan amounts over the years.")
    st.pyplot(fig1)

    

    
 
    
    
    
    
    
    
    
#     def loan_vs_term_scatter(df):
#         fig, ax = plt.subplots(figsize=(8, 6))
#         ax.scatter(df['loan_amount'], df['term_in_months'], alpha=0.5)
#         ax.set_xlabel('Loan Amount')
#         ax.set_ylabel('Term in Months')
#         ax.set_title('Loan Amount vs. Term in Months')
#         st.pyplot(fig)


    
    
#     loan_vs_term_scatter(data1)



# loan_vs_lender_scatter(data2)
# loan_vs_term_scatter(data2)
    
    
    

    
    
    
    
    
#     # Import python modules
#     import pandas as pd
#     import streamlit as st
#     import matplotlib.pyplot as plt
#     import seaborn as sns
#     import plotly.express as px
    
#     data1= pd.read_csv('kaggle_cleaned.csv')
#     data2= pd.read_csv('kiva_eda.csv')
    
    
#     def plot_sector_count(df):
#         d = df.groupby('sector').agg(nr=('activity', 'count')).reset_index()
#         d = d.sort_values('nr', ascending=False)

#         plt.figure(figsize=(8, 6))
#         plt.barh(d['sector'], d['nr'], color='sandybrown', edgecolor='black')
#         plt.gca().invert_yaxis()
#         plt.xlabel('Number of loans')
#         plt.title('Sector (all)')
#         st.pyplot()
        
        
        
#     plot_sector_count(data1)
#     plot_sector_count(data2)
