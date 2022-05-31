pipeline {
    agent { 
        node {
            label: 'python-agent'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                cd myapp
                pip install requirements.txt
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
                curl http://localhost:5000
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
            }
        }
    }
}