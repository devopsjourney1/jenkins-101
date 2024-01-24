pipeline {
    agent { 
        node {
            label 'docker-agent-alpine-python'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Pull') {
            steps {
                git branch: '${branch}, url: 'https://github.com/ningzaichun/hello-springboot'
            }
        }
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                python3 -m venv ~/.venv
                source ~/.venv/bin/activate
                pip3 install --upgrade pip3
                pip3 install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                source ~/.venv/bin/activate
                python3 hello.py
                python3 hello.py --name=Brad
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}