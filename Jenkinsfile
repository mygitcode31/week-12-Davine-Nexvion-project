pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        COMPOSE_PROJECT_NAME = 'nexvion'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git rev-parse --short HEAD'
            }
        }

        stage('Validate Source') {
            steps {
                sh '''
                    set -eu

                    for file in index.html products.html payment.html \
                                style.css products.css payment.css \
                                script.js payment.js Dockerfile \
                                docker-compose.yml nginx.conf; do
                        test -s "$file"
                        echo "PASS: $file"
                    done
                '''
            }
        }

        stage('Build and Deploy') {
            steps {
                sh '''
                    docker compose -p "$COMPOSE_PROJECT_NAME" config -q
                    docker compose -p "$COMPOSE_PROJECT_NAME" up -d --build
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    python3 - <<'PY'
import time
import urllib.request

base = "http://127.0.0.1:8081"
pages = ["/", "/products.html", "/payment.html"]

for path in pages:
    for attempt in range(20):
        try:
            with urllib.request.urlopen(base + path, timeout=5) as response:
                if response.status != 200:
                    raise RuntimeError(f"{path}: HTTP {response.status}")
                print(f"PASS: {path} - HTTP {response.status}")
                break
        except Exception:
            if attempt == 19:
                raise
            time.sleep(3)

print("DEPLOYMENT VERIFICATION SUCCESSFUL")
PY
                '''
            }
        }
    }

    post {
        success {
            echo 'Nexvion CI/CD pipeline completed successfully.'
        }
        failure {
            echo 'Nexvion CI/CD pipeline failed. Check the stage logs.'
        }
    }
}
