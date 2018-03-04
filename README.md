# Clips-tourist_recomendation
# USER MANUAL

## 1. Introduction

The objective of our system is to ensure that tourists coming to Singapore will be able to plan out a unique itinerary specially catered to them. The only thing the users have to do is to fill out a short questionnaire about their travel details as well as their interests and some personal information (sex, religion, age). With that, we will profile them with the existing data obtained through our research and inputs from domain experts then recommend to them a unique itinerary to maximize their holiday experience in Singapore.

## 2. Download

1. Get source code from [github](https://github.com/ISS-Kerui/Clips-tourist_recom-endation/tree/master).

 Requirements:

- Python 2.7
- Wxpython==3.0.3
- Pyclips==1.0.7.343 
- Pandas ==0.20.2

1. Get App for mac from  [Google Drive](https://drive.google.com/drive/folders/1QxFcs0HY27FiUgDe-DeCRpIP_0VYWnIu).

## 3. How to use

There are 10 questions in our system. User only needs to  choose answers or pictures that match their qualifications.

***Questions:***

**1.** Is this your first time travelling to Singapore? (Yes/No)

 Yes -> jump to Q2

No  ->  jump to Q3

**2. **Please select the places you have been to 

6 pictures totally, you can select 0-6 pictures

**3.** How many days will you be \n travelling in Singapore? 

a.one day b. two days c. three days

**4. **Who are you planning to travel with? 

a. Solo, I am Solo, Han Solo.                        

b. I am travelling with my Significant other.      

c. I am travelling with my parents/ elderly.         

d. I am travelling with my other half and my children.

e. I am travelling with my friends.               

**5.** What is your daily budget? (per person)

 a. $10-$50  b.$50-$100   c.above $100

**6.** Please choose one place you prefer to go

There are two pictures. The first picture represents metropolis. The second represents nature.

**7.** Please choose one place you prefer to go

There are two pictures. The first picture represents entertainment. The second represents historical.

**8.** Please choose one place you prefer to go

There are two pictures. The first picture represents culture. The second represents shopping.

**9.** Do you want a relax trip?

Yes or No

**10.** Do you like indoor activities more?

Yes or No



## 5. Output

The system recommends different sites depending on user's answers. For daily recommendation, the system recommends three large sites, each containing a number of small attractions.

## 6. System message

For question 6-8, users must choose **one** picture. If click **Next** button directly, the system will show the system message.

![3772F43B-900F-4F6D-AE76-F9602220858A](/Users/zhangkerui/Library/Containers/com.tencent.qq/Data/Library/Application Support/QQ/Users/520291037/QQ/Temp.db/3772F43B-900F-4F6D-AE76-F9602220858A.png)
