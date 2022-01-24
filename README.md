# Beetroot_python_diploma_project
Final diploma project for 'Python for begginers' course

## Ideas and purposes:
This Telegram bot app might help couples with ideas for cooking. 
This app sends user a reciept from his notes(Dishes list) via Telegram. 
So when you are busy and don't have time to think what exactly you need/want for breakfast/lunch/dinner just start this app, and choose the one best suits you. Fulfill your database with your favourite meals. 

## How to use app:
App propose 2keyboards: visible(client mode), and hidden(admin mode).
After '/start' command entered by user it sends client keyboard. Here are 2 buttons: 'What_to_cook' and 'Show_all_dishes'. 'What_to_cook' will randomly generate a meal from your DB.

For editing dishes list, use admin mode: '/admin' hidden command for starting. Here you will be send admin keyboard, so you can delete dishes or add a new one(upload image, add reciepe). The only limit here is a text in reciept description might be <200 symbols, you can just add a link for a meal actually. 

## Backend part (Debian10/Ubuntu20.04 are recommended, you may use any other OS with familiar setup)
For starting using this app you need only Python3 and aiogram library for python enironment. See steps below:

#### Python3 installation
1.Check python3 is installed
python3 --version 
2.If no python3 installed, please install it:
You can use link how to: https://linuxhint.com/install-python-debian-10/
#### Database:
SQLite local database will be in use as data storage, no additional software installation required. 
DB will be created, if it wasn't yet.

#### Python reguirements installation:
git clone git@github.com:artemol86/beetroot_python_diploma_project.git
python3 -m venv venv
source venv/bin/activate
pip3 install -r ./requirements.txt

#### Setup secrets
Then update 'setup_keys.py':
#Telegram token key here:
token_key='your_token_key_here'

#Admins user_list here. This bot will tell your id: @userinfobot , separate each admin user by comma:
admins = [xxxxxx, yyyyyy, zzzzzz]


