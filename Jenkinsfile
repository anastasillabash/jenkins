pipeline {
    options { timestamps() }

    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('arsgoo-dockerhub')
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
                sh 'cp Lab3/pawnshop_tests.py .'
                sh 'python3 Lab3/pawnshop_tests.py'
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
                sh 'cp Lab3/Dockerfile .'
                sh 'docker build -t arsgoo/pawnshop_tests:latest .'
            }
        }
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push arsgoo/pawnshop_tests:latest'
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}