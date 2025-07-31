1) I have created a dummy infrastructure that generates crypto currency prices using a random function and performs functionalities as mentioned in the "Work Trail Crpto" pdf. 
2) For tasks 1,2 and 3, run main.py file and the output would look like 

![main_py_image!](main_py_image.png)

3) For task 4, run file run_symbol_mapper.py (modular_connector/symbol_mapper/run_symbol_mapper.py) folder to see an output like 

![symbol_mapper_image!](symbol_mapper_image.png)

4) For task 5, firstly, we need to create a timescaledb database. Assuming the user has timescaledb, open terminal and run the following commnd -> "docker exec -it timescaledb psql -U postgres -d postgres"

5) This would take us inside postgres database and we create a dummy database with this command -> "CREATE DATABASE dummy;"

6) We are creating a username and password as follows -> "CREATE ROLE saniyashah WITH LOGIN PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE dummy TO saniyashah;"
kindly replace 'saniyashah' with your username and 'your_secure_password' with your password 

7) Then we navigate inside this database -> "docker exec -it timescaledb psql -U postgres -d dummy" and grant permissions for the username, in my case it was 'saniyashah' using ->
"GRANT USAGE, CREATE ON SCHEMA public TO saniyashah;
ALTER SCHEMA public OWNER TO saniyashah;"

8) After this, we run store_order_book.py (modular_connector/utils/store_order_book.py) that will call the combined_order_book function and append the newly made order book. 'collect_and_store' function will create a table called 'order_book_snapshots' inside timescaledb database. 
[ Important note -> inside store_order_book.py, on line no 19, 'engine = create_engine('postgresql://saniyashah:your_secure_password@localhost:5432/dummy')', kindly replace 'saniyashah' with your username and 'your_secure_password' with your password ]

9) After running, store_order_book.py file, your order book data should be appended inside the database in table 'order_book_snapshots' by running -> SELECT * FROM order_book_snapshots;
Your database should have multiple entries such as ->

![database_image!](timescale_db_orderbook.png)