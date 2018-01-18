echo "install"
pip install gunicorn flask

echo "run it"
nohup gunicorn -w 4 -b 0.0.0.0:7001 wsgi:app --log-file error.log </dev/null &>/dev/null & sleep 1
