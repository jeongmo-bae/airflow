# homebrew 활용 설치
brew install openssl readline sqlite3 xz zlib
brew install pyenv
brew install pyenv-virtualenv


# pyenv/bin 경로를 PATH 에 등록하여 pyenv를 어디에서도 사용 가능하도록 하기 위해 추가
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.zshrc
# pyenv 를 정상적으로 사용할 수 있도록 zshrc 에 init 명령어를 추가
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
# pyenv virtualenv 를 정상적으로 사용할 수 있도록 zshrc 에 init 명령어를 추가
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

source ~/.zshrc


pyenv install --list | grep  " 3\.[678910]"

# 설치
pyenv install -v 3.9.6
# 설치 된 모든 파이썬 버전 확인
pyenv versions  # 또는 ls ~/.pyenv/versions/
# 최근 활성화 된 파이썬 버전 확인
pyenv version
# 삭제 할 때: pyenv uninstall 3.9.6
# python 3.9.6 을 global 로 선언
pyenv global 3.9.6
# pyenv 활성화 버전 확인
pyenv versions
# 현재 사용중인 python 버전 확인
python -V


# airflow 용 가상환경 만들기 
pyenv virtualenv 3.8.19 airflow_3_8_19
cd ~ && mkdir airflow && cd airflow
# 가상환경 local 등록
pyenv local airflow_3_8_19

### 수동으로 가상환경 활성화/비활성화
pyenv activate airflow_3_8_19
pyenv deactivate airflow_3_8_19

# gitignore 
$echo ".python-version" >> .gitignore
$echo ".gitignore" >> .gitignore
