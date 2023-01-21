import requests
from bs4 import BeautifulSoup
import csv

# Send GET request to the website
response = requests.get('https://www.businesslist.co.ke/')

# Parse HTML of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the name, email, phone number, and position of the businesses
businesses = soup.find_all('div', {'class': 'business-card'})

# Write the extracted data to a CSV file
with open('businesses.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Name', 'Email', 'Phone Number', 'Position'])
    for business in businesses:
        name = business.find('h2').text
        email = business.find('span', {'class': 'email'}).text
        phone_number = business.find('span', {'class': 'phone-number'}).text
        position = business.find('span', {'class': 'position'}).text
        writer.writerow([name, email, phone_number, position])
