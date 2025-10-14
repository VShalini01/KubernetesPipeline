pipeline { 
    agent any 

    environment {
        IMAGE_NAME = "mypythonflaskapp"
        CONTAINER_NAME = "kubecluster_container"
        K8S_NAMESPACE = "default"
        CONTAINER_PORT = "5050"
    }

    stages { 
        stage('Build Docker Image') { 
            steps { 
                echo "🔧 Building Docker Image..."
                bat """
                docker build -t %IMAGE_NAME% .
                """
            } 
        }

        stage('Run New Container') { 
            steps { 
                echo "🚀 Running Flask App in a NEW Docker Container..."
                bat """
                echo "Cleaning up old container (if any)..."
                docker rm -f %CONTAINER_NAME% || exit 0

                echo "Starting new container on port %CONTAINER_PORT%..."
                docker run -d -p %CONTAINER_PORT%:5000 --name %CONTAINER_NAME% %IMAGE_NAME%
                """
                echo "✅ New container started successfully at http://localhost:%CONTAINER_PORT%"
            } 
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "⚙️ Deploying Flask App to Kubernetes..."
                bat """
                kubectl apply -f namespace.yaml || exit 0
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                kubectl get pods -n %K8S_NAMESPACE%
                kubectl get svc -n %K8S_NAMESPACE%
                """
            }
        }
    }

    post { 
        success { 
            echo '✅ Pipeline completed successfully! App deployed to Kubernetes.'
        } 
        failure { 
            echo '❌ Pipeline failed. Please check the logs for details.' 
        } 
    } 
}