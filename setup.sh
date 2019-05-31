#!/bin/bash
setup(){
  if [[ ! -d env ]]; then
    virtualenv env
  fi
  source env/bin/activate
  pip install -r requirements.txt
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py collectstatic
  python3 manage.py createsuperuser
}

run(){
  source env/bin/activate
  screen -dmSL alarm gunicorn mysite.wsgi:application
}

helpI(){
  echo "
        -h: help
        -s: Prepares the platform execution environment
        -r: Brings the platform running"
}

while [[ "$1" =~ ^- && ! "$1" == "--" ]]; do
    case $1 in
        -h) helpI
        ;;
        -s) setup
        ;;
        -r) run
    esac;
    cd $DIR
    shift;
done
