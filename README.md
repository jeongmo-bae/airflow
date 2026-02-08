# airflow study

## Settings
```shell
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/3.1.7/docker-compose.yaml'
```
- airflow 3.1.7 with docker (CeleryExecutor를 사용하여 Airflow를 실행가능)
  - airflow-scheduler - 모든 작업과 DAG를 모니터링한 후, 종속 작업이 완료되면 해당 작업 인스턴스를 실행 
  - airflow-dag-processor - Dag 프로세서는 Dag 파일을 구문 분석
  - airflow-api-server - API 서버는 다음 주소에서 이용 가능 (http://localhost:8080)
  - airflow-worker - 스케줄러가 지정한 작업을 실행하는 작업자 
  - airflow-triggerer - 지연 가능한 작업을 위해 이벤트 루프를 실행 
  - airflow-init - 초기화 서비스 
  - postgres - DB
  - redis - 스케줄러에서 워커로 메시지를 전달하는 브로커 
  - flower - 환경 모니터링을 위한 앱 (http://localhost:5555) 
    - 선택적으로, 옵션을 추가하여 flower 기능을 활성화할 수 있음 
    - ```shell
      --profile flowerdocker compose --profile flower updocker compose up flower
      ```
- files
  - ./dags - Dag 파일을 넣을 수 있음
  - ./logs - 작업 실행 및 스케줄러 로그를 포함
  - ./config - 사용자 지정 로그 파서를 추가하거나 airflow_local_settings.py 클러스터 정책을 구성하도록 추가 가능
  - ./plugins - 사용자 지정 플러그인

- Airflow 사용자 설정
  - ```shell
    mkdir -p ./dags ./logs ./plugins ./config
    echo -e "AIRFLOW_UID=$(id -u)" > .env
    ```
- airflow.cfg 파일 초기화
  - ```shell
    docker compose run airflow-cli airflow config list
    ```
- 데이터베이스를 초기화
  - ```shell
    docker compose up airflow-init
    ```
- airflow service start 
  - ```shell
    docker compose up -d
    ```

- local python settings
  - airflow-scheduler image 내 python interpreter 사용 하도록 IDE 설정


## references
- (local - standalone) https://airflow.apache.org/docs/apache-airflow/stable/start.html
- (docker) https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html