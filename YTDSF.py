'''
In This Section I am going to Define Functions for YouTube Channel Dashboard,
And We will use these functions in our main code.
Thanks.
Subhash Kumar..
'''

import pandas as pd
import matplotlib.pyplot as plt

file_path = "youtube_channel_data.csv"      #File Path
df = pd.read_csv(file_path)                 #Load data

# Data Cleaning & Preparation

df1 = df.copy()     # We make a duplicate for original data, and we perform action on copied data.

# Convert 'UploadDate' to datetime
df1['UploadDate'] = pd.to_datetime(df1['UploadDate'])

# Handle 'N/A' values in Dislikes and Comments columns
df1['Dislikes'] = pd.to_numeric(df1['Dislikes'], errors='coerce').fillna(0)
df1['Comments'] = pd.to_numeric(df1['Comments'], errors='coerce').fillna(0)

# Check and handle 'N/A' values in 'Views' and 'Likes' if any, though the inspection showed they are numeric
df1['Views'] = pd.to_numeric(df1['Views'], errors='coerce').fillna(0)
df1['Likes'] = pd.to_numeric(df1['Likes'], errors='coerce').fillna(0)

def Head():
    print(df.head())    #Display Top 10 Data in Dataset
    return

def Describe():
    print(df.describe())    # Describing Dataset
    return

def Info():
    print(df.info())        #Dataset Info
    return

def LinePLot():                   #Line Chart: Views over Time
    plt.figure(figsize=(12, 6))
    df_sorted_by_date = df1.sort_values('UploadDate')
    plt.plot(df_sorted_by_date['UploadDate'], df_sorted_by_date['Views'])
    plt.title('Views Over Time', fontsize=16)
    plt.xlabel('Upload Date', fontsize=12)
    plt.ylabel('Views', fontsize=12)
    plt.yticks(fontsize=10)
    plt.xticks(fontsize=10)
    plt.grid(True)
    plt.show()
    return


def BarPlot():      # Bar Chart : View per Video we Choose Top(10).
    plt.rcParams['font.family'] = 'Segoe UI Emoji'  # Sometimes i encounter font warning/error, that why i call this.
    df_sorted_by_views = df.sort_values('Views', ascending=False).head(10)
    plt.figure(figsize=(12, 8))
    plt.barh(df_sorted_by_views['Title'], df_sorted_by_views['Views'], color='green')
    plt.xlabel('Views', fontsize=12)
    plt.ylabel('Video Title', fontsize=12)
    plt.title('Top 10 Most Viewed Videos', fontsize=16)
    plt.gca().invert_yaxis()  # Invert Y-axit.
    plt.tight_layout()  # Use this for better Title visibility
    plt.show()
    return

def PiPlot():           #Pie Chart: Engagement (Likes/Dislikes/Comments)
    # Creating a small dictionary with total data:
    engagement_data = {
        ' 👍Likes': df1['Likes'].sum(),
        ' 👎Dislikes': df1['Dislikes'].sum(),
        ' 💬Comments': df1['Comments'].sum()
    }

    # Calculating Percentages for data and assigning labels.
    total = sum(engagement_data.values())
    labels = [
        f'{key} → {value / total * 100:.1f}%'
        for key, value in engagement_data.items()
    ]

    plt.figure(figsize=(6, 6))
    plt.pie(engagement_data.values(), labels=labels, colors=['m', '0', 'b'], explode=[0, 0, 0.2], startangle=40)
    plt.title("Engagement Distribution")
    plt.show()
    return

def ProjectInfo():
    msg1 = (
        "📊 YouTube Channel Analytics Dashboard\n"
        "This project is created and submitted by **Mr. Subhash Kumar Rana** "
        "(subhash_2312res664@iitp.ac.in) as part of the **90-Day Internship** program by **GUVI (HCL)**.\n\n"
        "🎯 Project Objective:\n"
        "Analyze and visualize YouTube channel data using Python.\n"
        "This is **Project-1** of the internship.\n"
    )
    print(msg1)


def AboutMe():
    aboutme = (
        "👋 Hey Developers,\n"
        "I’m **Subhash Kumar Rana**, an aspiring Data Scientist and a Computer Science & Data Analytics undergraduate "
        "(Graduating in 2026).\n\n"
        "🔍 I have a strong foundation in data analysis, Python programming, and general computer science concepts. "
        "I enjoy working on real-world datasets and building insightful visualizations.\n\n"
        "📬 Let’s connect or collaborate!\n"
        "Email: subhash_2312res664@iitp.ac.in\n"
        "Phone: +91 62997 42348\n"
    )
    print(aboutme)
