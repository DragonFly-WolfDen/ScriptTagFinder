# Install and import 'requests' and 'beautifulsoup4' libraries
import requests
from bs4 import BeautifulSoup


# Define the function for checking a URL for <script> tags
def check_url_for_script_tags(url):
    # Add try handle with if, else, and except pathways to account for possible results scenarios
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            script_tags = soup.find_all('script')
            if script_tags:
                print(f"Found {len(script_tags)} <script> tags in website: {url}")
            else:
                print(f"No <script> tags found in website: {url}")
        else:
            print(f"Failed to find and open {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Define main functions for user input of a URL and checking for script tags
def main():
    website_url = input("Enter the website URL: ")
    check_url_for_script_tags(website_url)


# Add if __name__ == "__main__" code and main() function for functionality assurance and standard convention
if __name__ == "__main__":
    main()
