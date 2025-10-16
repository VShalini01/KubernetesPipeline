pipeline { 
    agent any 

    stages { 
        stage('Build Docker Image') { 
            steps { 
                echo "🔧 Building Docker Image..."
                bat "docker build -t kubedemoapp:v1 ."
            } 
        }
        stage('Docker login') {
            steps {
                bat 'docker login -u vshalini01 -p Shalinfo@102'
            }
        }

        stage('push Docker image to docker hub'){
            steps{
                echo "push Docker image to docker hub"
                bat "docker tag kubedemoapp:v1 vshalini01/sample:kubeimage1"

                bat "docker push vshalini01/sample:kubeimage1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
               bat 'kubectl apply -f deployment.yaml --validate=false'
               bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post { 
        success { 
            echo 'Pipeline completed successfully! App deployed to Kubernetes.'
        } 
        failure { 
            echo 'Pipeline failed. Please check the logs for details.' 
        } 
    } 

}

