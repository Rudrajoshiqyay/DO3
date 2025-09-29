pipeline {
    agent any
    
    environment {
        SONAR_SCANNER_HOME = tool 'SonarScanner'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/YOUR_USERNAME/DO3.git'
                echo 'Code checked out successfully'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                echo 'Dependencies installed'
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python -m pytest test_app.py -v --junitxml=test-results.xml --cov=. --cov-report=xml
                '''
                echo 'Tests completed'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh '''
                        ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                          -Dsonar.projectKey=DO3 \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://localhost:9000 \
                          -Dsonar.python.coverage.reportPaths=coverage.xml
                    '''
                }
                echo 'SonarQube analysis completed'
            }
        }
        
        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
                echo 'Quality Gate passed'
            }
        }
    }
}
