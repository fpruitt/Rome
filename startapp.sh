echo "=========== Checking For Unmigrated Changes ==========="
python rome/manage.py makemigrations

echo "=========== Running Migrations ==========="
python rome/manage.py migrate

echo "=========== Starting Server ==========="
python rome/manage.py runserver 0.0.0.0:8000
