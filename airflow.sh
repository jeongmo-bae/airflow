### airflow  py3.8 가상환경에 설치 진행
pyenv virtualenv 3.8.19 airflow_3_8_19
cd ~ && mkdir airflow && cd airflow
# 가상환경 local 등록
pyenv local airflow_3_8_19

echo $"AIRFLOW_HOME=~/airflow" >> ~/.zshrc

AIRFLOW_VERSION=2.8.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# 초기 설정
airflow db migrate
airflow users create --username bjm000 --firstname jungmo --lastname bae --role Admin --email jungmob1024@gmail.com
airflow webserver --port 8080
airflow scheduler

# Delete example DAGs 
sed -i '' 's/load_examples = True/load_examples = False/' /Users/jeongmo/airflow/airflow.cfg
rm -rf ~/airflow/airflow.db
airflow db init
airflow users create --username bjm000 --firstname jungmo --lastname bae --role Admin --email jungmob1024@gmail.com

