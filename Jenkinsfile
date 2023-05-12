pipeline {
    agent any
    
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
            environment {
                scannerHome = tool 'SonarQube-Scanner'
            }
            steps {
                withSonarQubeEnv(installationName:'SonarQube'){
                    sh "cd myapp"
                    sh "${scannerHome}/bin/sonar-scanner"
                }
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