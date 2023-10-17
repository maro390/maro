
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st

new_liss=["Founded_year","UK_rank","World_rank","CWUR_score","Minimum_IELTS_score","UG_average_fees_(in_pounds)","PG_average_fees_(in_pounds)","Estimated_cost_of_living_per_year_(in_pounds)","Latitude","Longitude"]


st.title('universities in uk')



df = pd.read_csv(r"C:\Users\maraw\OneDrive\Desktop\test\uk_universities.csv")
df1 = df.sort_values(ascending=True, by="UK_rank").head(10)
def plt_1():
    plt.figure(figsize=(15, 8))
    plt.bar(df1["University_name"], df1["UK_rank"], color='skyblue')
    plt.xlabel("University_name")
    plt.ylabel("UK_rank")
    plt.title("UK University Rankings")
    plt.xticks(rotation=70)
    st.pyplot(plt)


    
my_lambda = print("Hello World!")
my_lambda1 = print("Hello World!")
my_lambda3 = print("Hello World!")
my_lambda4 = print("Hello World!")

task1='''click this button to see
         the top 10 universities in the rankings (UK_rank)'''
st.write(task1)
# Create the button and attach the lambda function to it
btn1=st.button("click me",on_click=my_lambda)
if btn1:
    plt_1()







x = df['Region'].value_counts()
def plt_2():
    plt.figure(figsize=(25, 10))
    plt.bar(x.index, x.values, color='skyblue') 

    plt.title('Region Counts')  
    plt.xlabel('Region')  
    plt.ylabel('Count')  

    plt.xticks(rotation=45) 
    st.pyplot(plt)

task2='''click this button to see
         the number of universities by region'''


st.write(task2)
    

btn2=st.button("click        me",on_click=my_lambda1)
if btn2:
    plt_2()











def plt_3():
    plt.figure(figsize=(15, 10))
    plt.hist(df['Minimum_IELTS_score'], bins=[4, 5, 6, 6.5], edgecolor='black', color='skyblue')

    plt.title('Minimum of IELTS Scores')
    plt.xlabel('IELTS Score')
    plt.ylabel('Number of Universities')

    plt.xticks([4,5, 6, 6.5])
    st.pyplot(plt)

task3='''click this button to see
         Number of universities that require minimum scores Between 4 to 5, 5 to 6, and 6 to 6.5 for IELTS'''


st.write(task3)
    

btn22=st.button("click  me",on_click=my_lambda3)
if btn22:
    plt_3()





def plt_4():
    last=df['Academic_Calender'].value_counts()

    plt.pie(last.values ,labels=last.index,autopct="%0.0f%%")
    plt.legend(labels=last.index)
    st.pyplot(plt)

task4='''click this button to see
         The percentage of the university’s academic calendar'''


st.write(task4)
    

btn4=st.button("click   me",on_click=my_lambda4)
if btn4:
    plt_4()





y=df["University_name"].value_counts()
xx=y.index
xxx=y.index
xxxx=y.index
def main1():
    global selected_rows
    st.title("University Name Selection")
    selected_options = st.multiselect("Select universities", xx)
    selected_rows = df[df["University_name"].isin(selected_options)]
    


main1()
urt2=st.button("click            me")
if urt2:
    
    st.write(selected_rows)
def main2():
    global new_df
    lisrr=["Region","Founded_year","Motto","UK_rank","World_rank","CWUR_score","Minimum_IELTS_score","UG_average_fees_(in_pounds)","PG_average_fees_(in_pounds)","International_students","Student_satisfaction","Student_enrollment","Academic_staff","Control_type","Academic_Calender","Campus_setting","Estimated_cost_of_living_per_year_(in_pounds)","Latitude","Longitude","Website"]
    st.title("University compare Selection")
    selected_options = st.multiselect("compare universities", xxx)
    selected_rows = df[df["University_name"].isin(selected_options)]
    selected_compare_in=st.multiselect("Select the compared columns",lisrr)
    
    new_df=selected_rows[selected_compare_in]
    new_df['name']=selected_options
    
    
main2()
urt=st.button("click           me")
if urt:
    
    st.write(new_df)

def bar(selected_optionss,selected_compare_inn):
    
    plt.figure(figsize=(15, 8))  
    
    plt.xlabel("University_name") 
    selected_rows = df[df["University_name"].isin(selected_optionss)]
    plt.title("UK University Rankings") 
    plt.xticks(rotation=70)
    
    

    
    plt.ylabel(f"{selected_compare_inn}")
    plt.bar(selected_optionss, selected_rows[selected_compare_inn], color='skyblue') 
    st.pyplot(plt)


#selected_optuion = st.radio("Select one choice", options)



def main22(event):
    print(event)
    global new_df
    
    st.title("University compare Selection")
    selected_optionsss = st.multiselect("compare universities   ", xxxx)
    
    selected_compare_ins = st.radio("Select one choice", new_liss)
    bar(selected_optionsss,selected_compare_ins)
    
    
    
    
    

main22("event")





    
