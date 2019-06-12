# Python-I-Final-Project
Final Project

* Commit and upload your final project using Github like previous homeworks.
* Add instructions in this README.md file to demonstrate your project.
* We will demonstrate our projects on June 12, 2019. If you can't attend, I will try to run your program for the class.
* If the program does not run, I will have to deduct major points, so please make sure it runs!
* If I can't get it to run, I may reach out and ask you to fix your program.



Project Douban Book: Top 250

This project will pull out top-250-book related information, including book name, author, rating, number of people rated, and quote, from the web page (https://book.douban.com/top250?start=0), and save the data as both text and csv files.

Notes:
There are 10 web pages of these 250 books, 25 books per page. To better demonstrate the outputs, only 25 books are written into the text and csv files.

The program includes three parts:
I: Download the web page through get_html function:
    def get_html():
      #using requests
II: Parse and extract information:
    --Loop through all top-rated-book web pages by using function all_page(). It starts at 0, ends at 250, and increments by 25.
    --Get 5 lists of book names, authors, ratings, No. of people rated, and Quote.
    --Handle these lists to remove redundant information and/or spaces.
III: Write data into text file by using writelines, and export into csv with dataframe to_csv methods.
IV: Output file includes 'top25.txt' and 'top25.csv'.
