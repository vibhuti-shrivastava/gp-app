import pandas as pd
import streamlit as st
import altair as alt
#import matplotlib.pyplot as plt
#from bokeh.plotting import figure
import plotly.express as px
import json

#INTRODUCTION
##st.title("Supply Chain Analytics")
##st.markdown("One stop solution to Supply Chain Decision Making")
from PIL import Image
image = Image.open(r'banner.png')
st.image(image, use_column_width=True)
#FILE UPLOAD
st.sidebar.subheader('What would you like work with today?')
todo = st.sidebar.selectbox('To do:', ('Inbound Logistics', 'Inhouse Preparation', 'Outbound Logistics', 'Fulfillment', 'Sales'))
if todo == 'Inbound Logistics':
    st.sidebar.subheader('Inbound Logistics')
    inbound = st.sidebar.selectbox('To do:', ('Lead Time', 'Purchase Order'))

#PURCHASE ORDER FREQUENCY
    if inbound == 'Purchase Order':
        st.header("Purchase Order Analysis")
        st.markdown("Analysis of purchase order data such as PO frequency, PO volume and PO prices")
        uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
        if uploaded_file:
            data = pd.read_excel(uploaded_file)
            df = pd.DataFrame(data, columns= ['PO Number', 'Doc Date', 'Vendor Name', 'Category', 'Base Qty', 'Net value per UoM', 'Grand Total FA PO'])
            #st.markdown("Say hello to your database")
            #st.dataframe(df)
            if st.button('Preview Dataset'):
                st.dataframe(df)
            st.cache(persist=True)
            
            st.sidebar.subheader('Select for Purchase Order')
            basis = st.sidebar.selectbox('Basis', ('Purchase Frequency','Purchase Volume',))
            if basis == 'Purchase Frequency':
                st.sidebar.subheader('Select for Purchase Frequency')
                criteria = st.sidebar.selectbox('Criteria', ('Category', 'Vendor', 'Volume'))
##                if criteria == 'Date':
##                    #PO Frequency by date
##                    df_date = df.groupby(['Doc Date'])
##                    df_datecount = df.groupby(['Doc Date']).count()
##                    df_date_count = pd.DataFrame(df_datecount, columns= ['PO Number'])
##                    st.markdown(" ")
##                    st.markdown(" ")
##                    st.markdown("Date wise analysis of the purchase frequency")
##                    st.line_chart(df_date_count)
##                    st.dataframe(df_date_count)
                if criteria == 'Category':
                    #PO Frequency by category
                    df_category = df.groupby(['Category'])
                    df_catcount = df.groupby(['Category']).count()
                    df_cat_count = pd.DataFrame(df_catcount, columns= ['PO Number'])
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Category wise analysis of the purchase frequency")
                    st.bar_chart(df_cat_count)
                    st.dataframe(df_cat_count)
                elif criteria == 'Vendor':
                    #PO Frequency by vendor name
                    st.sidebar.subheader('Select the category')
                    category = st.sidebar.selectbox('Categories', ('Stitched apparel', 'Jewelry', 'Unstitched apparel', 'Home and Art', 'Bags and Footwear'))
                    if category == 'Stitched apparel':
                        df_SA = df.loc[df['Category'] == 'Stitched apparel']
                        df_SAvname = df_SA.groupby(['Vendor Name'])
                        df_SA_vname = df_SA.groupby(['Vendor Name']).count()
                        df_SA_vname_count = pd.DataFrame(df_SA_vname, columns= ['PO Number'])
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown("Vendor wise analysis of the purchase frequency for the Stitched Apparel Category")
                        st.bar_chart(df_SA_vname_count)
##                        stitched_PO = df_SA_vname_count['PO Number'].values.tolist()
##                        vendorname = df_SA_vname_count['Vendor Name'].values.tolist()
##                        l = []
##                        for i in stitched_PO:
##                            if i >= 60:
##                                index = stitched_PO.index(i)
##                                a = vendorname(index)
##                                l.append(a)
##                                print [l]
                        st.dataframe(df_SA_vname_count)
                    elif category == 'Jewelry':
                        df_jew = df.loc[df['Category'] == 'Jewelry']
                        df_jewvname = df_jew.groupby(['Vendor Name'])
                        df_jew_vname = df_jew.groupby(['Vendor Name']).count()
                        df_jew_vname_count = pd.DataFrame(df_jew_vname, columns= ['PO Number'])
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown("Vendor wise analysis of the purchase frequency for the Category Jewelry")
                        st.bar_chart(df_jew_vname_count)
                        st.dataframe(df_jew_vname_count)
                    elif category == 'Unstitched apparel':
                        df_USA = df.loc[df['Category'] == 'Unstitched apparel']
                        df_USAvname = df_USA.groupby(['Vendor Name'])
                        df_USA_vname = df_USA.groupby(['Vendor Name']).count()
                        df_USA_vname_count = pd.DataFrame(df_USA_vname, columns= ['PO Number'])
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown("Vendor wise analysis of the purchase frequency for the Unstitched Apparel Category")
                        st.bar_chart(df_USA_vname_count)
                        st.dataframe(df_USA_vname_count)
                    elif category == 'Home and Art':
                        df_HA = df.loc[df['Category'] == 'Home and Art']
                        df_HAvname = df_HA.groupby(['Vendor Name'])
                        df_HA_vname = df_HA.groupby(['Vendor Name']).count()
                        df_HA_vname_count = pd.DataFrame(df_HA_vname, columns= ['PO Number'])
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown("Vendor wise analysis of the purchase frequency for the Home and Art Category")
                        st.bar_chart(df_HA_vname_count)
                        st.dataframe(df_HA_vname_count)
                    elif category == 'Bags and Footwear':
                        df_BF = df.loc[df['Category'] == 'Bags and Footwear']
                        df_BFvname = df_BF.groupby(['Vendor Name'])
                        df_BF_vname = df_BF.groupby(['Vendor Name']).count()
                        df_BF_vname_count = pd.DataFrame(df_BF_vname, columns= ['PO Number'])
                        st.markdown(" ")
                        st.markdown(" ")
                        st.markdown("Vendor wise analysis of the purchase frequency for the Bags and Footwear Category")
                        st.bar_chart(df_BF_vname_count)
                        st.dataframe(df_BF_vname_count)
                elif criteria == 'Volume':
                    #PO Frequency by vendor name
##                    st.sidebar.subheader('Select the category')
##                    category = st.sidebar.selectbox('Categories', ('Stitched apparel', 'Jewelry', 'Unstitched apparel', 'Home and Art', 'Bags and Footwear'))
##                    if category == 'Jewelry':
##                        df_jew = df.loc[df['Category'] == 'Jewelry']
                    #df_volume1 = df.groupby(['Base Qty'])
                    df_volume = df.groupby(['Base Qty']).count()
                    df_volume_count = pd.DataFrame(df_volume, columns= ['PO Number'])
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Analysis of the volume of POs that were raised")
                    st.line_chart(df_volume_count)
                    st.dataframe(df_volume_count)
##                    elif category == 'Stitched apparel':
##                        df_SA = df.loc[df['Category'] == 'Stitched apparel']
##                        df_SAvname = df_SA.groupby(['Base Qty'])
##                        df_SA_vname = df_SA.groupby(['Base Qty']).count()
##                        df_SA_vname_count = pd.DataFrame(df_SA_vname, columns= ['PO Number'])
##                        st.markdown(" ")
##                        st.markdown(" ")
##                        st.markdown("Analysis of the volume of POs that were raised for a particular category")
##                        st.line_chart(df_SA_vname_count)
##                        st.dataframe(df_SA_vname_count)
##                    elif category == 'Unstitched apparel':
##                        df_USA = df.loc[df['Category'] == 'Unstitched apparel']
##                        df_USAvname = df_USA.groupby(['Base Qty'])
##                        df_USA_vname = df_USA.groupby(['Base Qty']).count()
##                        df_USA_vname_count = pd.DataFrame(df_USA_vname, columns= ['PO Number'])
##                        st.markdown(" ")
##                        st.markdown(" ")
##                        st.markdown("Analysis of the volume of POs that were raised for a particular category")
##                        st.line_chart(df_USA_vname_count)
##                        st.dataframe(df_USA_vname_count)
##                    elif category == 'Home and Art':
##                        df_HA = df.loc[df['Category'] == 'Home and Art']
##                        df_HAvname = df_HA.groupby(['Base Qty'])
##                        df_HA_vname = df_HA.groupby(['Base Qty']).count()
##                        df_HA_vname_count = pd.DataFrame(df_HA_vname, columns= ['PO Number'])
##                        st.markdown(" ")
##                        st.markdown(" ")
##                        st.markdown("Analysis of the volume of POs that were raised for a particular category")
##                        st.line_chart(df_HA_vname_count)
##                        st.dataframe(df_HA_vname_count)
##                    elif category == 'Bags and Footwear':
##                        df_BF = df.loc[df['Category'] == 'Bags and Footwear']
##                        df_BFvname = df_BF.groupby(['Base Qty'])
##                        df_BF_vname = df_BF.groupby(['Base Qty']).count()
##                        df_BF_vname_count = pd.DataFrame(df_BF_vname, columns= ['PO Number'])
##                        st.markdown(" ")
##                        st.markdown(" ")
##                        st.markdown("Analysis of the volume of POs that were raised for a particular category")
##                        st.line_chart(df_BF_vname_count)
##                        st.dataframe(df_BF_vname_count)
            elif basis == 'Purchase Volume':
                #PO Frequency by volume
                st.sidebar.subheader('Select the category')
                category = st.sidebar.selectbox('Categories', ('Jewelry','Stitched apparel', 'Unstitched apparel', 'Home and Art', 'Bags and Footwear'))
                if category == 'Jewelry':
                    df_jew = df.loc[df['Category'] == 'Jewelry']
                    df_jewvname = df_jew.groupby(['Vendor Name'])
                    df_jew_vname = df_jew.groupby(['Vendor Name']).sum()
                    df_jew_vname_count = pd.DataFrame(df_jew_vname, columns= ['Base Qty'])
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Analysis of the volumes ordered in the PO for the category of Jewelry")
                    st.bar_chart(df_jew_vname_count)
                    st.dataframe(df_jew_vname_count)
                elif category == 'Stitched apparel':
                    df_SA = df.loc[df['Category'] == 'Stitched apparel']
                    df_SAvname = df_SA.groupby(['Vendor Name'])
                    df_SA_vname = df_SA.groupby(['Vendor Name']).sum()
                    df_SA_vname_count = pd.DataFrame(df_SA_vname, columns= ['Base Qty'])
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Analysis of the volumes ordered in the PO for the category of Stitched Apparel")
                    st.bar_chart(df_SA_vname_count)
                    st.dataframe(df_SA_vname_count)
                elif category == 'Unstitched apparel':
                    df_USA = df.loc[df['Category'] == 'Unstitched apparel']
                    df_USAvname = df_USA.groupby(['Vendor Name'])
                    df_USA_vname = df_USA.groupby(['Vendor Name']).sum()
                    df_USA_vname_count = pd.DataFrame(df_USA_vname, columns= ['Base Qty'])
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Analysis of the volumes ordered in the PO for the category of Unstitched Apparel")
                    st.bar_chart(df_USA_vname_count)
                    st.dataframe(df_USA_vname_count)
                elif category == 'Home and Art':
                    df_HA = df.loc[df['Category'] == 'Home and Art']
                    df_HAvname = df_HA.groupby(['Vendor Name'])
                    df_HA_vname = df_HA.groupby(['Vendor Name']).sum()
                    df_HA_vname_count = pd.DataFrame(df_HA_vname, columns= ['Base Qty'])
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Analysis of the volumes ordered in the PO for the category of Home and Art")
                    st.bar_chart(df_HA_vname_count)
                    st.dataframe(df_HA_vname_count)
                elif category == 'Bags and Footwear':
                    df_BF = df.loc[df['Category'] == 'Bags and Footwear']
                    df_BFvname = df_BF.groupby(['Vendor Name'])
                    df_BF_vname = df_BF.groupby(['Vendor Name']).sum()
                    df_BF_vname_count = pd.DataFrame(df_BF_vname, columns= ['Base Qty'])
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Analysis of the volumes ordered in the PO for the category of Bags and Footwear")
                    st.bar_chart(df_BF_vname_count)
                    st.dataframe(df_BF_vname_count)
##            elif basis == 'Purchase Price':
##                #PO Frequency by price
##                st.sidebar.subheader('Select the category')
##                category = st.sidebar.selectbox('Categories', ('Jewelry','Stitched apparel', 'Unstitched apparel', 'Home and Art', 'Bags and Footwear'))
##                if category == 'Jewelry':
##                    df_jew = df.loc[df['Category'] == 'Jewelry']
##                    df_jewvname = df_jew.groupby(['Vendor Name'])
##                    df_jew_vname = df_jew.groupby(['Base Qty']).sum()
##                    df_jew_vname_count = pd.DataFrame(df_jew_vname, columns= ['Base Qty'])
##                    
##                    st.line_chart(df_jew_vname_count)
##                    st.dataframe(df_jew_vname_count)
##                elif category == 'Stitched apparel':
##                    df_SA = df.loc[df['Category'] == 'Stitched apparel']
##                    df_SAvname = df_SA.groupby(['Base Qty'])
##                    df_SA_vname = df_SA.groupby(['Base Qty']).count()
##                    df_SA_vname_count = pd.DataFrame(df_SA_vname, columns= ['PO Number'])
##                    
##                    st.line_chart(df_SA_vname_count)
##                    st.dataframe(df_SA_vname_count)
##                elif category == 'Unstitched apparel':
##                    df_USA = df.loc[df['Category'] == 'Unstitched apparel']
##                    df_USAvname = df_USA.groupby(['Base Qty'])
##                    df_USA_vname = df_USA.groupby(['Base Qty']).count()
##                    df_USA_vname_count = pd.DataFrame(df_USA_vname, columns= ['PO Number'])
##                    
##                    st.line_chart(df_USA_vname_count)
##                    st.dataframe(df_USA_vname_count)
##                elif category == 'Home and Art':
##                    df_HA = df.loc[df['Category'] == 'Home and Art']
##                    df_HAvname = df_HA.groupby(['Base Qty'])
##                    df_HA_vname = df_HA.groupby(['Base Qty']).count()
##                    df_HA_vname_count = pd.DataFrame(df_HA_vname, columns= ['PO Number'])
##                    
##                    st.line_chart(df_HA_vname_count)
##                    st.dataframe(df_HA_vname_count)
##                elif category == 'Bags and Footwear':
##                    df_BF = df.loc[df['Category'] == 'Bags and Footwear']
##                    df_BFvname = df_BF.groupby(['Base Qty'])
##                    df_BF_vname = df_BF.groupby(['Base Qty']).count()
##                    df_BF_vname_count = pd.DataFrame(df_BF_vname, columns= ['PO Number'])
##                    
##                    st.line_chart(df_BF_vname_count)
##                    st.dataframe(df_BF_vname_count)
    if inbound == 'Lead Time':
        st.header("Lead Time Analysis")
        st.markdown("Analysis of how the lead times are varying")
        uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
        if uploaded_file:
            data = pd.read_excel(uploaded_file)
            st.cache(persist=True)
            df = pd.DataFrame(data, columns= ['PO Number', 'Doc Date', 'Receiving Date', 'Vendor Name', 'Category', 'Location', 'Lead Time', 'State'])
            #st.markdown("Say hello to your database")
            #st.dataframe(df)
            if st.button('Preview Dataset'):
                st.dataframe(df)
            st.sidebar.subheader('Select a criteria for Lead Time')
            basis = st.sidebar.selectbox('Basis', ('Category','Category wise Vendors', 'Location'))
            if basis == 'Category':
                df_category = (df.groupby(['Category', 'Lead Time'], as_index=False).mean().groupby('Category')['Lead Time'].mean())
                df_category1 = (df.groupby(['Category', 'Lead Time'], as_index=False).mean()).groupby('Category', as_index=False)['Lead Time'].mean()
                #st.dataframe(df_category1)
                st.markdown(" ")
                st.markdown(" ")
                st.markdown("Category wise analysis of the Lead Time")
                st.bar_chart(df_category)
                category = df_category1['Category'].values.tolist()
                leadtime = df_category1['Lead Time'].values.tolist()
                    # inbuilt function to find the position of minimum  
                minpos = leadtime.index(min(leadtime))
                mini=category[minpos]
                    # inbuilt function to find the position of maximum  
                maxpos = leadtime.index(max(leadtime))
                maxi=category[maxpos]
                    # printing the position  
                st.write("The highest vendor lead time is for", maxi)  
                st.write ("The least vendor lead time is for", mini)
                    
                if st.button('View Dataframe'):
                    st.dataframe(df_category)
            if basis == 'Category wise Vendors':
                #Lead time by vendor name
                st.sidebar.subheader('Select the category')
                category = st.sidebar.selectbox('Categories', ('Stitched apparel', 'Jewelry', 'Unstitched apparel', 'Home and Art', 'Bags and Footwear'))
                if category == 'Jewelry':
                    df_jew = df.loc[df['Category'] == 'Jewelry']
                    df_category = (df_jew.groupby(['Vendor Name', 'Lead Time'], as_index=False).mean().groupby('Vendor Name')['Lead Time'].mean())
                    st.bar_chart(df_category)
                    #df_jewlead = pd.DataFrame(df_jew, columns=['Vendor Name', 'Lead Time', 'PO Number'])
##                    c = alt.Chart(df_category).mark_circle().encode(
##                    x='Vendor Name', y='Lead Time', tooltip=['Vendor Name', 'Lead Time', 'PO Number'])
##                    st.markdown(" ")
##                    st.markdown(" ")
##                    st.markdown("Vendor wise analysis of the Lead Time for the category of Jewelry")
##                    st.altair_chart(c, use_container_width=True)
                    st.dataframe(df_category)
                elif category == 'Stitched apparel':
                    df_SA = df.loc[df['Category'] == 'Stitched apparel']
                    df_category = (df_SA.groupby(['Vendor Name', 'Lead Time'], as_index=False).mean().groupby('Vendor Name')['Lead Time'].mean())
                    st.bar_chart(df_category)
##                    df_SAlead = pd.DataFrame(df_SA, columns=['Vendor Name', 'Lead Time', 'PO Number'])
##                    c = alt.Chart(df_SAlead).mark_circle().encode(
##                    x='Vendor Name', y='Lead Time', tooltip=['Vendor Name', 'Lead Time', 'PO Number'])
##                    st.markdown(" ")
##                    st.markdown(" ")
##                    st.markdown("Vendor wise analysis of the Lead Time for the category of Stitched Apparel")
##                    st.altair_chart(c, use_container_width=True)
                    st.dataframe(df_category)
                elif category == 'Unstitched apparel':
                    df_USA = df.loc[df['Category'] == 'Unstitched apparel']
                    df_category = (df_USA.groupby(['Vendor Name', 'Lead Time'], as_index=False).mean().groupby('Vendor Name')['Lead Time'].mean())
                    st.bar_chart(df_category)
##                    df_USAlead = pd.DataFrame(df_USA, columns=['Vendor Name', 'Lead Time', 'PO Number'])
##                    c = alt.Chart(df_USAlead).mark_circle().encode(
##                    x='Vendor Name', y='Lead Time', tooltip=['Vendor Name', 'Lead Time', 'PO Number'])
##                    st.markdown(" ")
##                    st.markdown(" ")
##                    st.markdown("Vendor wise analysis of the Lead Time for the category of Unstitched Apparel")
##                    st.altair_chart(c, use_container_width=True)
                    st.dataframe(df_category)
                elif category == 'Home and Art':
                    df_HA = df.loc[df['Category'] == 'Home and Art']
                    df_category = (df_HA.groupby(['Vendor Name', 'Lead Time'], as_index=False).mean().groupby('Vendor Name')['Lead Time'].mean())
                    st.bar_chart(df_category)
##                    df_HAlead = pd.DataFrame(df_HA, columns=['Vendor Name', 'Lead Time', 'PO Number'])
##                    c = alt.Chart(df_HAlead).mark_circle().encode(
##                    x='Vendor Name', y='Lead Time', tooltip=['Vendor Name', 'Lead Time', 'PO Number'])
##                    st.markdown(" ")
##                    st.markdown(" ")
##                    st.markdown("Vendor wise analysis of the Lead Time for the category of Home and Art")
##                    st.altair_chart(c, use_container_width=True)
                    st.dataframe(df_category)
                elif category == 'Bags and Footwear':
                    df_BF = df.loc[df['Category'] == 'Bags and Footwear']
                    df_category = (df_BF.groupby(['Vendor Name', 'Lead Time'], as_index=False).mean().groupby('Vendor Name')['Lead Time'].mean())
                    st.bar_chart(df_category)
##                    df_BFlead = pd.DataFrame(df_BF, columns=['Vendor Name', 'Lead Time', 'PO Number'])
##                    c = alt.Chart(df_BFlead).mark_circle().encode(
##                    x='Vendor Name', y='Lead Time', tooltip=['Vendor Name', 'Lead Time', 'PO Number'])
##                    st.markdown(" ")
##                    st.markdown(" ")
##                    st.markdown("Vendor wise analysis of the Lead Time for the category of Bags and Footwear")
##                    st.altair_chart(c, use_container_width=True)
                    st.dataframe(df_category)
            if basis == 'Location':
                st.cache(persist=True)
                df_location_leadtime = (df.groupby(['State', 'Lead Time'], as_index=False).mean().groupby('State')['Lead Time'].mean())
                
                st.markdown(" ")
                st.markdown(" ")
                st.markdown("Location wise analysis of the Lead Time")
                st.bar_chart(df_location_leadtime)
                if st.button('View Dataset'):
                    st.dataframe(df_location_leadtime)
                st.cache(persist=True)

                df_state = df.groupby(['State'])
                df_statecount = df.groupby('State',as_index=False).count()
                df_state_count = pd.DataFrame(df_statecount, columns= ['PO Number', 'State'])
                st.markdown(" ")
                st.markdown(" ")
                india_states = json.load(open(r"C:\Users\sd\Desktop\states_india.geojson"))
                #st.dataframe(df_state_count)
                state_id_map = {}
                for feature in india_states["features"]:
                    feature["id"] = feature["properties"]["state_code"]
                    state_id_map[feature["properties"]["st_nm"]] = feature["id"]
                #df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
                df_state_count["id"] = df_state_count["State"].apply(lambda x: state_id_map[x])
                st.markdown("State wise analysis of the Vendors")
                fig = px.choropleth_mapbox(
                    df_state_count,
                    locations="id",
                    geojson=india_states,
                    color="PO Number",
                    hover_name="State",
                    hover_data=["PO Number"],
                    title="State wise orders",
                    mapbox_style="carto-positron",
                    center={"lat": 24, "lon": 78},
                    zoom=3,
                    opacity=0.5
                )
                fig.update_geos(fitbounds="locations", visible=False)
                #fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
                st.plotly_chart(fig)
                if st.button('View Data'):
                    st.dataframe(df_state_count)
                

if todo == 'Outbound Logistics':
    st.sidebar.subheader('Outbound Logistics')
    outbound = st.sidebar.selectbox('To do:', ('Order to ship', 'Ship to delivery', 'Miscellaneous'))

    if outbound == 'Order to ship':
        st.header("Outbound Logistics: Order to ship")
        st.markdown("Analysis of how long it takes for orders to be shipped")
        uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
        if uploaded_file:
            data = pd.read_excel(uploaded_file)
            df = pd.DataFrame(data, columns= ['Order No', 'Order Date', 'Ship Date', 'Delivery Date', 'Order to Ship Days', 'Ship to Delivery Days', 'O2S group'])
            
            if st.button('Preview Dataset'):
                st.dataframe(df)
            st.cache(persist=True)
            
            df_shipdatecount = df.groupby(['O2S group'],as_index=False).count()
            df_shipdate_count = pd.DataFrame(df_shipdatecount, columns= ['O2S group','Order No'])
            st.markdown(" ")
            st.markdown(" ")
            st.markdown("Order to ship analysis")
            fig = px.bar(df_shipdate_count, x='O2S group', y='Order No')
            fig.update_layout(xaxis_type = 'category')
            st.plotly_chart(fig)
            agree = st.checkbox('Show dataframe')
            if agree:
                st.dataframe(df_shipdate_count)
                
    elif outbound == 'Ship to delivery':
        st.cache(persist=True)
        st.header("Outbound Logistics: Ship to delivery")
        st.markdown("Analysis of how long it takes for orders to be delivered after they are shipped from the warehouse")
        uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
        if uploaded_file:
            data = pd.read_excel(uploaded_file)
            df = pd.DataFrame(data, columns= ['Order No', 'Order Date', 'Ship Date', 'Delivery Date', 'Order to Ship Days', 'Ship to Delivery Days'])
            #st.markdown("Say hello to your database")
            #st.dataframe(df)
            if st.button('Preview Dataset'):
                st.dataframe(df)
            st.cache(persist=True)
            #PO Frequency by date
            df_deliverydate = df.groupby(['Ship to Delivery Days'])
            df_deliverycount = df.groupby(['Ship to Delivery Days']).count()
            df_delivery_count = pd.DataFrame(df_deliverycount, columns= ['Order No'])
            st.markdown(" ")
            st.markdown(" ")
            st.markdown("Ship to order analysis of the shipments")
            st.bar_chart(df_delivery_count)
            st.dataframe(df_delivery_count)
    elif outbound == 'Miscellaneous':
        st.header("Outbound Logistics: Miscellaneous")
        st.markdown("Analysis of payment types, transporters, location wise orders")
        uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
        if uploaded_file:
            data = pd.read_excel(uploaded_file)
            df = pd.DataFrame(data, columns= ['Order No', 'Order to Ship Days', 'Ship to Delivery Days', 'City', 'State', 'Country', 'Payment Mode', 'Transporter'])
            #st.markdown("Say hello to your database")
            #st.dataframe(df)
            if st.button('Preview Dataset'):
                st.dataframe(df)
            st.cache(persist=True)
            st.sidebar.subheader('Select for Delivery')
            basis = st.sidebar.selectbox('Basis', ('Delivery Location','Payment Modes', 'Transport Service'))
            if basis == 'Delivery Location':
##                st.sidebar.subheader('Select for Delivery')
##                location = st.sidebar.selectbox('Domestic/International', ('Domestic Orders','International Orders'))
                #if location == 'Domestic Orders':
                    st.cache(persist=True)
            #PO Frequency by date
                    df_state = df.groupby(['State'])
                    df_statecount = df.groupby('State',as_index=False).count()
                    df_state_count = pd.DataFrame(df_statecount, columns= ['Order No', 'State'])
                    st.markdown(" ")
                    st.markdown(" ")
                    india_states = json.load(open(r"C:\Users\sd\Desktop\states_india.geojson"))
                    #st.dataframe(india_states)
                    state_id_map = {}
                    for feature in india_states["features"]:
                        feature["id"] = feature["properties"]["state_code"]
                        state_id_map[feature["properties"]["st_nm"]] = feature["id"]
                    #df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
                    df_state_count["id"] = df_state_count["State"].apply(lambda x: state_id_map[x])
                    st.markdown("State wise analysis of the Domestic orders")
                    fig = px.choropleth_mapbox(
                        df_state_count,
                        locations="id",
                        geojson=india_states,
                        color="Order No",
                        hover_name="State",
                        hover_data=["Order No"],
                        title="State wise orders",
                        mapbox_style="carto-positron",
                        center={"lat": 24, "lon": 78},
                        zoom=3,
                        opacity=0.5
                    )
                    fig.update_geos(fitbounds="locations", visible=False)
                    #fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
                    st.plotly_chart(fig)
                    
                    #st.bar_chart(df_state_count)
                    if st.button('View Dataset'):
                        st.dataframe(df_state_count)
                #if location == 'International Orders':
                    st.cache(persist=True)
            #PO Frequency by date
                    df_country = df[df['Country'] != 'India']
                    df_countrycount = df_country.groupby('Country',as_index=False).count()
                    df_country_count = pd.DataFrame(df_countrycount, columns= ['Order No', 'Country'])
                    st.markdown(" ")
                    st.markdown(" ")
                    country = json.load(open(r"C:\Users\sd\Desktop\world.geojson"))
                    #st.dataframe(india_states)
                    world_id_map = {}
                    for feature in country["features"]:
                        feature["id"] = feature["properties"]["ADM0_A3"]
                        world_id_map[feature["properties"]["NAME"]] = feature["id"]
                    #df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
                    df_country_count["id"] = df_country_count["Country"].apply(lambda x: world_id_map[x])
                    st.markdown("Country wise analysis of the International orders")
                    fig = px.choropleth_mapbox(
                        df_country_count,
                        locations="id",
                        geojson=country,
                        color="Order No",
                        hover_name="Country",
                        hover_data=["Order No"],
                        title="Country wise orders",
                        mapbox_style="carto-positron",
                        #center={"lat": 24, "lon": 78},
                        zoom=0.5,
                        opacity=0.5
                    )
                    fig.update_geos(fitbounds="locations", visible=False)
                    fig.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0})
                    st.plotly_chart(fig)
                    
                    #st.bar_chart(df_state_count)
                    if st.button('View Data'):
                        st.dataframe(df_country_count)
                    
                    
            elif basis == 'Payment Modes':
                st.cache(persist=True)
                #df_country = df[df['Country'] != 'India']
                df_pmcount = df.groupby(['Payment Mode']).count()
                df_pm_count = pd.DataFrame(df_pmcount, columns= ['Order No'])
                st.markdown(" ")
                st.markdown(" ")
                st.markdown("Preferred payment mode analysis for the orders")
                # This dataframe has 244 lines, but 4 distinct values for `day`
                #df = px.data.tips()
                #st.title("Payment Modes")
                fig = px.pie(df, values=df['Order No'], names=df['Payment Mode'], title='Payment Modes')
                st.plotly_chart(fig)
                #fig.show()
                #st.bar_chart(df_pm_count)
                #st.pyplot(fig)
                st.dataframe(df_pm_count)
            elif basis == 'Transport Service':
                
                    st.cache(persist=True)
                    df_country = df[df['Country'] != 'India']
                    df_transcount = df_country.groupby('Transporter',as_index=False).count()
                    df_transmean = df_country.groupby('Transporter').mean()
                    df_trans_mean = pd.DataFrame(df_transmean, columns= ['Ship to Delivery Days'])
                    df_trans_count = pd.DataFrame(df_transcount, columns= ['Order No', 'Transporter'])
                    #st.dataframe(df_transcount)
                    #df_trans_count = pd.DataFrame(df_transcount.columns('Transporter', 'Order No'))
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Transporter analysis for the orders")
                    #st.title("International Transporters")
                    fig = px.pie(df_transcount, values=df_transcount['Order No'], names=df_transcount['Transporter'], title='International Transporters')
                    st.plotly_chart(fig)
                    st.bar_chart(df_trans_mean)
                    if st.button('View Dataset'):
                        st.dataframe(df_trans_mean)
                    
                    st.cache(persist=True)
                    df_country = df[df['Country'] == 'India']
                    df_transcount = df_country.groupby('Transporter',as_index=False).count()
                    df_transmean = df_country.groupby('Transporter').mean()
                    df_trans_mean = pd.DataFrame(df_transmean, columns= ['Ship to Delivery Days'])
                    #df_trans_count = df_transcount('Order No', 'Transporter', 'Ship to Delivery Days')
                    df_trans_count = pd.DataFrame(df_transcount, columns= ['Order No', 'Transporter'])
                    st.markdown(" ")
                    st.markdown(" ")
                    st.markdown("Transporter analysis for the orders")
                    #st.title("Domestic Transporters")
                    fig = px.pie(df_transcount, values=df_transcount['Order No'], names=df_transcount['Transporter'], title='Domestic Transporters')
                    st.plotly_chart(fig)
                    st.bar_chart(df_trans_mean)
                    if st.button('View Data'):
                        st.dataframe(df_trans_count)
                        st.dataframe(df_trans_mean)

if todo == 'Fulfillment':
    #st.sidebar.subheader('Fulfillment')
    #fulfillment = st.sidebar.selectbox('To do:', ('Order to Delivery', 'Ship to delivery', 'Miscellaneous'))
    #if fulfillment == 'Order to Delivery':
    st.cache(persist=True)
    st.header("Order Fulfillment: Order to delivery")
    st.markdown("Analysis of how long it takes for orders to be delivered")
    uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
    if uploaded_file:
        data = pd.read_excel(uploaded_file)
        df = pd.DataFrame(data, columns= ['Order No', 'Order Date', 'Delivery Date', 'Order to Delivery Days','O2D group'])
        #st.markdown("Say hello to your database")
        #st.dataframe(df)
        if st.button('Preview Dataset'):
            st.dataframe(df)
        st.cache(persist=True)
        df_shipdatecount = df.groupby(['O2D group'],as_index=False).count()
        df_shipdate_count = pd.DataFrame(df_shipdatecount, columns= ['O2D group','Order No'])
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("Order to ship analysis")
        fig = px.bar(df_shipdate_count, x='O2D group', y='Order No')
        fig.update_layout(xaxis_type = 'category')
        st.plotly_chart(fig)
        agree = st.checkbox('Show dataframe')
        if agree:
            st.dataframe(df_shipdate_count)

if todo == 'Inhouse Preparation':
    #st.sidebar.subheader('Inhouse Preparation')
    #prep = st.sidebar.selectbox('To do:', ('Preparation Time'))
    st.header("Inhouse Preparation: Quality Check and Packaging")
    st.markdown("Analysis of how long it takes for the order to be prepared inhouse. This includes Quality Check and Packaging of the products")
    uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
    if uploaded_file:
        data = pd.read_excel(uploaded_file)
        df = pd.DataFrame(data, columns= ['Order No', 'Order Date', 'Prep Time', 'SKU source','Order to Delivery Days'])
        #st.markdown("Say hello to your database")
        #st.dataframe(df)
        if st.button('Preview Dataset'):
            st.dataframe(df)
        st.cache(persist=True)
        #if prep == 'Preparation Time':
        df_prepcount = df.groupby(['Prep Time']).count()
        df_prep_count = pd.DataFrame(df_prepcount, columns= ['Order No'])
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("Preparation Time for the orders")
        st.bar_chart(df_prep_count)
        
        df_ordercount = df.groupby('SKU source',as_index=False).count()
        df_ordermean = df.groupby('SKU source').mean()
        df_order_mean = pd.DataFrame(df_ordermean, columns= ['Order to Delivery Days', 'Prep Time'])
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("Order Type based on the source")
        fig = px.pie(df_ordercount, values=df_ordercount['Order No'], names=df_ordercount['SKU source'], title='Order Type')
        st.plotly_chart(fig)
        if st.button('View Dataset'):
            st.dataframe(df_ordercount)
        st.bar_chart(df_order_mean)

if todo == 'Sales':
    #st.sidebar.subheader('Fulfillment')
    #fulfillment = st.sidebar.selectbox('To do:', ('Order to Delivery', 'Ship to delivery', 'Miscellaneous'))
    #if fulfillment == 'Order to Delivery':
    st.cache(persist=True)
    st.header("Sales")
    st.markdown("Analysis of Sales")
    uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
    if uploaded_file:
        data = pd.read_excel(uploaded_file)
        df = pd.DataFrame(data, columns= ['Channel', 'BUSINESS', 'BRAND', 'Order Qty 1', ' GSV Value ','DIVISION'])
        #st.markdown("Say hello to your database")
        #st.dataframe(df)
        if st.button('Preview Dataset'):
            st.dataframe(df)
        st.cache(persist=True)
        df_channel = df.loc[df['DIVISION'] == 'Stitched']
        df_shipdatecount = df_channel.groupby(['BRAND'],as_index=False).count()
        df_shipdate_count = pd.DataFrame(df_shipdatecount, columns= ['BRAND','Order Qty 1'])
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("Sales analysis")
        fig = px.bar(df_shipdate_count, x='BRAND', y='Order Qty 1')
        fig.update_layout(xaxis_type = 'category')
        st.plotly_chart(fig)
        agree = st.checkbox('Show dataframe')
        if agree:
            st.dataframe(df_shipdate_count)
