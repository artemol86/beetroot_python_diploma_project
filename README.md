# beetroot_python_diploma_project
Final diploma project for "Python for begginers" course

## Ideas and purposes:
This Telegram bot might help couples with ideas for cooking. 
So when you are busy and don't have time to think what exactly you need/want for breakfast/lunch/dinner just start this app.

## How to use app:
Available Buttons: 'Give me idea'; 'Meal menu': 'Add meal', 'Delete meal', 'Edit meal #number', 'help'.
-Add/delete meal you like most to fulfill your dishes list. 
-After clicking on 'Give me idea' app will randomly generate idea from your dishes list. If you don't like the idea, click again on 'Give me idea'.


## Backend part____(Debian10/Ubuntu20.04 are recommended, you may use any other OS with familiar setup)

#### Python3 installation
1.Check python3 is installed
python3 --version 
2.If no python3 installed, please install it:
You can use link how to: https://linuxhint.com/install-python-debian-10/
#### MySQL installation(Debian/Ubuntu OS):
1.Check you have MySQL installed and it's version:
mysql -V
2. If you don't have MySQL, please install it(MySQL 8.0 is recommended):
You can use link how to: https://linuxize.com/post/how-to-install-mysql-on-debian-10/
3. Create database:
https://www.cyberciti.biz/faq/howto-linux-unix-creating-database-and-table/
4. Create DB user for your app:
https://linuxize.com/post/how-to-create-mysql-user-accounts-and-grant-privileges/

###### Examples: 
mysql> CREATE DATABASE Dishes;

mysql> use Dishes;
Database changed
mysql> CREATE TABLE Dishes_List
    -> (
    -> ID int NOT NULL UNIQUE,
    -> Name varchar(100) NOT NULL,
    -> Ingredients varchar(1000) NOT NULL,
    -> HowToCook varchar(1000) NOT NULL,
    -> Photo varchar(100) NOT NULL,
    -> Video varchar(100) NOT NULL
    -> );
Query OK, 0 rows affected (0,04 sec)


mysql> SHOW COLUMNS FROM Dishes_List;
+-------------+---------------+------+-----+---------+-------+
| Field       | Type          | Null | Key | Default | Extra |
+-------------+---------------+------+-----+---------+-------+
| ID          | int           | NO   | PRI | NULL    |       |
| Name        | varchar(100)  | NO   |     | NULL    |       |
| Ingredients | varchar(1000) | NO   |     | NULL    |       |
| HowToCook   | varchar(1000) | NO   |     | NULL    |       |
| Photo       | varchar(100)  | NO   |     | NULL    |       |
| Video       | varchar(100)  | NO   |     | NULL    |       |
+-------------+---------------+------+-----+---------+-------+
6 rows in set (0,01 sec)

mysql>

mysql> quit

####Telegram API installation and bot creation
https://core.telegram.org/bots 
https://github.com/python-telegram-bot/python-telegram-bot#getting-started 
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot 
https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/ 

####Python reguirements installation:
git clone git@github.com:artemol86/beetroot_python_diploma_project.git
python3 -m venv venv
source venv/bin/activate
pip3 install -r ./requirements.txt


####Setup secrets
Then update 'setup_keys.ini':

	[MySQL]
	user_name = your_name
	user_pass = user_pass
	database = db_name_here
	
	[Telegram_bot]
	token = your_secret_token
	

