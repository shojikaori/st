import plotly.express as px
import streamlit as st
import requests
import numpy as np
import pandas as pd

st.title('沖縄那覇市のホテル') # タイトル

st.write('DataFrame') # テキストの表示

#楽天APIからデータをとってくる
REQUEST_URL="https://app.rakuten.co.jp/services/api/Travel/SimpleHotelSearch/20170426?"
APP_ID="1058887096118834280" 

params = {
    "format":"JSON",
    "largeClassCode": "japan",
    "middleClassCode": "okinawa",
    "smallClassCode": "nahashi",
    "applicationId": APP_ID
}

res = requests.get(REQUEST_URL, params)

result = res.json()
# これでAPIで取得したデータはresultに代入されます。

df = pd.DataFrame()

i=0
hotel_info = hotel_info = result["hotels"][i]["hotel"][0]["hotelBasicInfo"]

for i in range(0, len(result["hotels"])):
    hotel_info = result["hotels"][i]["hotel"][0]["hotelBasicInfo"]
    temp_df = pd.DataFrame(hotel_info, index=[i])
    df = pd.concat([df, temp_df])

df[['hotelMinCharge', 'reviewAverage']]

#Streamlitでplotyでグラフ化

st.subheader("那覇市のホテルのレビューと価格の関係")
fig = px.scatter(
    df,
    x="hotelMinCharge",
    y="reviewAverage",
    color="reviewAverage",
    color_continuous_scale="reds",
)

st.plotly_chart(fig)

