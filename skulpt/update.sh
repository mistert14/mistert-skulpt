echo "updating skulpt" 
cd /var/www/skulpt/git/skulpt/
python2.7 skulpt.py dist 
cp -v dist/skulpt*.js /var/www/skulpt/lib
cd /var/www/skulpt/
echo "update done" 
