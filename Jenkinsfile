pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
      triggers {
        pollSCM '*/1 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff.."

                cd myapp
                
                python3 hello.py
                python3 hello.py --name=Haston
                python3 pyinstaller --onefile hello.py
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