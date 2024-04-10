import requests
from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import urlparse
import pandas as pd



class Scraper:
    def __init__(self):
        self.data = pd.read_excel(r"scraper\data\xpath_data.xlsx")
    
    def __get_host(self, link):
        parsed_url = urlparse(link)
        return parsed_url.netloc
    
    def __clean_text(self, text):
        # Define the special characters to remove
        special_chars = ['\n', '\r', '\t']  # Add more special characters if needed
        
        # Remove the specified special characters
        cleaned_text = text
        for char in special_chars:
            cleaned_text = cleaned_text.replace(char, ' ')
        
        # Remove extra spaces
        cleaned_text = ' '.join(cleaned_text.split())
        
        return cleaned_text  

    

    def scrape(self, link):
        response = requests.get(link)
        response.raise_for_status()
        
        df = self.data
        
        filtered_df = df[df["Host"] == self.__get_host(link)]
        
        if not filtered_df.empty:
            fields = dict(filtered_df.iloc[0])
            
            soup = BeautifulSoup(response.content, 'html.parser')
            root = etree.HTML(str(soup))
            
            scraped_data = {}  # Initialize an empty dictionary to store scraped data
        
            for label, xpath in fields.items():
                if label in ["Title", "Content"] and not pd.isnull(xpath):  # Check if xpath is not NaN
                    result = root.xpath(xpath)
                    if result:
                        if isinstance(result, list):  # Handle multiple results
                            result = ', '.join(result)
                        scraped_data[label] = result.strip()  # Add scraped data to the dictionary
                    else:
                        scraped_data[label] = None  # If content not found, set value to None
                    
            scraped_data["Content"] = self.__clean_text(scraped_data["Content"])
            return scraped_data
        else:
            return None  # Return None if no matching rows found in DataFrame

