echo "Cloning Repository"
git clone github.com/unknownforall1/paidrenamerbot /paidrenamerbot
cd /paidrenamerbot 
echo "installing requirements"
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
