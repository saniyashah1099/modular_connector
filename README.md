Hello, a few instructions and comments on how to run this repository smoothly -

1) I have created a dummy infrastructure that generates crypto currency prices using a random function and performs functionalities as mentioned in the "Work Trail Crypto" pdf. <br><br>
2) For tasks 1,2 and 3, run main.py file and the output would look like <br>

![main_py_image!](main_py_image.png)

3) For task 4, run file run_symbol_mapper.py (modular_connector/symbol_mapper/run_symbol_mapper.py) folder to see an output like <br>

![symbol_mapper_image!](symbol_mapper_image.png)

4) For task 5, firstly, we need to create a timescaledb database. Assuming the user has timescaledb installed, open terminal and run the following command -><br>
 "docker exec -it timescaledb psql -U postgres -d postgres"<br><br>

5) This would take us inside postgres database and we create a dummy database with this command -><br>
 "CREATE DATABASE dummy;"<br><br>

6) We are creating a username and password as follows -> <br>
"CREATE ROLE saniyashah WITH LOGIN PASSWORD 'your_secure_password';<br>
GRANT ALL PRIVILEGES ON DATABASE dummy TO saniyashah;"<br>
[ Kindly replace 'saniyashah' with your username and 'your_secure_password' with your password ]<br><br>

7) Then we navigate inside this database -> <br>
"docker exec -it timescaledb psql -U postgres -d dummy" and grant permissions for the username, in my case it was 'saniyashah' using -><br>
"GRANT USAGE, CREATE ON SCHEMA public TO saniyashah;<br>
ALTER SCHEMA public OWNER TO saniyashah;"<br><br>

8) After this, we run store_order_book.py (modular_connector/utils/store_order_book.py) that will call the combined_order_book function and append the newly made order book. 'collect_and_store' function will create a table called 'order_book_snapshots' inside timescaledb database. <br>
[ Important note -> inside store_order_book.py, on line no 19, 'engine = create_engine('postgresql://saniyashah:your_secure_password@localhost:5432/dummy')', kindly replace 'saniyashah' with your username and 'your_secure_password' with your password ]<br><br>

9) After running, store_order_book.py file, your order book data should be appended inside the database in table 'order_book_snapshots' by running -> <br>
SELECT * FROM order_book_snapshots;<br>
Your database should have multiple entries such as ->

![database_image!](timescale_db_orderbook.png)
<br><br>

Our orderbook is populated inside the database and updated every 1 second, using an async collector function.<br><br>

10) Finally, I have attached a pdf 'Open_Ended_Questions.pdf' which answers the 3 open ended questions.