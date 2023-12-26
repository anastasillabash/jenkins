pipeline {
    options { timestamps() }

    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('anastaasiill-dockerhub')
    }
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'alpine'
                    args '-u=\"root\"'
                }
            }
            steps {
                sh 'apk add --update python3 py-pip'
                sh 'pip install xmlrunner'
                sh 'cp testapp.py .'
                sh 'python3 testapp.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Tests successfully completed!"
                }
                failure {
                    echo "Ops! Tests failed! Try again, please"
                }
            }
        }
        stage('Image creation') {
            steps {
                sh 'cp Dockerfile .'
                sh 'docker build -t anastaasiill/testapp:latest .'
            }
        }
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push anastaasiill/testapp:latest'
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}