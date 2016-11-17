sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/ff7f.py /etc/gunicorn.d/ff7f.py
sudo gunicorn -c /etc/gunicorn.d/ff7f.py ff7f:app
sudo /etc/init.d/gunicorn restart