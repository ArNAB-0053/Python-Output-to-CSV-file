import csv
import requests 
import api_key

country = input("Enter country: ")
catagory = input("Enter Catagory: ")
ch = input("You want a new csv file? \n")


url = f"https://newsapi.org/v2/top-headlines?country={country}&category={catagory}&apiKey={api_key.api_key}"
news = requests.get(url).json()
articels = news["articles"]

op = ""
if ch == "YES":
    op = 'w'  # To create new csv file

else:
    op = 'a'  # To add new data in that csv file
# print(f'{op}')


## There has to a csv file named CSV_file.csv
# Open the CSV file
with open('CSV_file.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    # Convert the reader object to a list and get the length
    data_list = list(reader)
    length = len(data_list)

# Print the length of the CSV file
print(f"The length of the CSV file is: {length}")


def news():
    news_articles = []

    index = length

    # For adding data in csv file
    if op == 'a':
        for i, article in enumerate(articels, index):
            news_articles.append((i, article["title"]))
    
    # Createing new csv file
    else:
        for i, article in enumerate(articels, 1):
            news_articles.append((i, article["title"]))

    # Open the CSV file in write mode
    with open('CSV_file.csv', f'{op}', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        if op == 'w':
            writer.writerow(['index', 'title'])   

        # Write each news headline and index to a separate row in the CSV file
        for article in news_articles:
            writer.writerow([article[0], article[1]])

    # Print a message to confirm that the file has been written
    print("News headlines written to CSV_file.csv")

news()