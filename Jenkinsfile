pipeline {
    agent { 
        node {
            label 'docker-agent-python'
            }
      }
    
    // triggers {
    //     pollSCM '*/5 * * * *'
    // }
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
        stage('SonarQube'){
            steps {
                sh '''
                cd myapp
                sonar-scanner \
                -Dsonar.projectKey=MyFirstSonarPorjectKey \
                -Dsonar.sources=. \
                -Dsonar.host.url=https://2702-70-134-213-247.ngrok-free.app \
                -Dsonar.token=sqp_aba115f3aaf8552b0a726fa2e5e0ab4edf152a56
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd myapp
                python3 hello.py
                python3 hello.py --name=Fred
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