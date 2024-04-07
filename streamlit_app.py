import streamlit as st
from autoscraper import AutoScraper
import json


amazon_scraper = AutoScraper()
amazon_scraper.load('amazon-search')

def get_amazon_result(search_query):
    api = 'https://www.amazon.in/s?k=%s' % search_query
    result = amazon_scraper.get_result_similar(api, group_by_alias=True)
    return result


def sort_results(results, sort_by):
   
    result_list = [{key: value[i] for key, value in results.items()} for i in range(len(list(results.values())[0]))]

    for sort_key in reversed(sort_by):
        if sort_key.lower() == "price":
            result_list.sort(key=lambda x: float(x.get("Price", "").replace("₹", "").replace(",", "")))
        elif sort_key.lower() == "title":
            result_list.sort(key=lambda x: x.get("Title", "").lower())
        elif sort_key.lower() == "ratings":
            result_list.sort(key=lambda x: int(x.get("Ratings", "").replace(",", "").split()[0]), reverse=True)

    return result_list

def main():
    st.title("Scrappy.ai")
    st.image("https://media.licdn.com/dms/image/D4E12AQHb2kkxJftUPw/article-cover_image-shrink_720_1280/0/1659445780016?e=2147483647&v=beta&t=ePb-EzQTDchZJ_O_9LTtS7wr-y_m4l-ovMRxt8hqqLI", use_column_width=False, width=500)


    search_query = st.text_input("Enter product name:")

    if st.button("Search"):
        if search_query:
            
            results = get_amazon_result(search_query)
          
            st.subheader("Scraping Output:")
            st.json(results)
        else:
            st.warning("Please enter a product name.")


    st.sidebar.subheader("Sorting Options")
    sort_by = st.sidebar.multiselect("Sort by", options=["Price", "Title", "Ratings"])

   
    if sort_by and 'results' in locals():  
        sorted_results = sort_results(results, sort_by)
        st.subheader("Sorted Results")
        st.json(sorted_results)


    if 'results' in locals():
        json_data = json.dumps(results, indent=4)
        st.download_button(label="Download JSON", data=json_data, file_name="amazon_search_results.json", mime="application/json")

if __name__ == '__main__':
    main()
