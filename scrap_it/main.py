from bs4 import BeautifulSoup
import requests
import csv

# Request for the remote html
remote_html = requests.get("https://profound-caramel-e3f140.netlify.app/").text

# instantiate BeautifulSoup
soup = BeautifulSoup(remote_html, "lxml")

# Scrap all 'article' tags
articles = soup.find_all("article")

# Open CSV for saving the scraped data
csv_file = open("python_scraped.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Article Title", "Image Description", "Image Source"])

# Loop through the data and 
for article in articles:

    # sieve the target columns [article h2, img src, img figcaption]
    article_title = article.h2.text
    img_source = article.figure.img["src"]
    img_description = article.figure.figcaption.text

    # Save the data columns in CSV
    csv_writer.writerow([article_title, img_description, img_source])
    # Print the sieved data
    print(f"{article_title}: {img_description}: {img_source}")

# Close the file after writing to it
csv_file.close()
