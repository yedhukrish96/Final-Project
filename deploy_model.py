# Python libraries
import streamlit as st
from PIL import Image

# User module files
from ml import ml
from eda import eda
import os



def main():
    

    # Display sidebar menu options
    options = ['Home','EDA','Prediction','Conclusion','What To Improve?']
    choice = st.sidebar.selectbox("Menu", options)

    # Display different pages based on user choice
    if choice == 'Home':
        image_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'dokumenty', 'Kivafinal.png')
        st.image(image_path)
        st.header("Welcome to KIVA!!")

        st.write("Kiva is a non-profit organization that allows people to lend money via the Internet to low-income entrepreneurs and students in over 80 countries. Since its founding in 2005, Kiva has facilitated more than $1 billion in loans.", 
         unsafe_allow_html=True, 
         height=200,
         font_size=20)
        
        
        image_path1 = os.path.join(os.path.expanduser('~'), 'Desktop', 'dokumenty', 'kiva_lending.png')
        st.image(image_path1)
        
        
        image_path2= os.path.join(os.path.expanduser('~'), 'Desktop', 'dokumenty', 'kiva_impact_tiny.png')
        st.image(image_path2)
        #st.image('/Desktop/dokumenty/KIVA.jpg')
        # Add other content for home page here
    elif choice == 'EDA':
        eda()
        
    
    
    
    elif choice == 'Prediction':
        ml()
#         loan_amount = ml()
#         st.write("Based on your inputs, you can borrow up to ", loan_amount)
    
    elif choice == 'Conclusion':
        conclusion = """
        - I came up with one important conclusion. It seems that KIVA is a crowdfunding organization which focus on improving the good aspects of life. As you can see, they mostly lend loans to sectors like Agriculture, Food, Retail etc. This is a proof that the organization aims at improving the welfare and life of people in that country
        - Agriculture sector remains the top sector to which most loans are borrowed.Over the years, this sector remains unchanged although there are a few sectors which moved up.
        - As the years pass by, Clothing sector and Retail has increased considerably. this indicates that people tend to be more conscious about Fashion.
        - Phillipines is the country with the most loan-borrowings during the years of 2013 to 2017. However, Kenya surpassed Phillipines during the recent years.
        - In terms of repayment methods, Irregular and Monthly were the two main methods from 2013 to 2017. However, Monthly installments are the most preferred payments at the moment.
        - During the years of 2013-2017, Female gender occupies the highest proportion for loan borrowings. Agriculture, Food, and retail are the sectors to which Female genders invested loan borrowings.In case of Male gender, Agriculture , Education and Food are the most invested however in small proportions.
        - Regarding the loan amount, from 2013 to 2014, there was a huge increase in loan borrowings. Afterwards, till 2016, the graph went steadily up and then finally, there was a huge drop in the loan borrowings.
        """
        st.header("Conclusions about my Project")
        
        st.markdown(conclusion)
    
    elif choice == 'What To Improve?':
        st.header("I realized that the second dataset I had, presented only a few data where I can explore. In terms of years, I just had one year- 2023. I would improve my project by using API more efficiently and gathering more data")
        
        

if __name__ == "__main__":
    main()
