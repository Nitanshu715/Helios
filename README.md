# Helios – Cloud-based AI Anomaly Detection 🚀

<img src="https://github.com/Nitanshu715/Helios/blob/main/logo.png" align="right" width="120" height="120">

---

## 📖 Overview  

**Helios** is a cloud-native anomaly detection framework designed to provide **real-time monitoring, prediction, and alerting** for critical cloud infrastructure metrics.  
It integrates **Machine Learning models** with **AWS cloud services** to detect anomalies across multiple domains including:  

- 🔥 CPU Utilization Anomalies  
- 🌐 Network Traffic Spikes  
- 🔑 Unauthorized Login Attempts  
- 📝 Malicious Content Injection  
- 💾 Storage Usage Irregularities  

Helios acts as a **self-healing agent** for cloud environments, capable of detecting abnormal behavior, notifying stakeholders, and providing the foundation for automated remediation.

---

## 🏗️ Architecture  

The project follows a **modular and scalable architecture**:  

1. **Model Training (Google Colab):**  
   - Five ML models trained (Isolation Forest, KMeans, Logistic Regression, TF-IDF + Logistic Regression).  
   - Exported to `.pkl` files for deployment.  

2. **Model Storage (AWS S3):**  
   - Models stored in a versioned S3 bucket.  
   - Ensures durability and rollback support.  

3. **Deployment (AWS EC2):**  
   - Flask-based API agent running on EC2 instance.  
   - Endpoints exposed for prediction requests.  

4. **Access Control (AWS IAM):**  
   - Least-privilege IAM role with **S3ReadOnlyAccess** for EC2 agent.  

5. **Monitoring & Alerts (AWS CloudWatch + SNS):**  
   - CloudWatch dashboards monitor real-time metrics.  
   - CloudWatch alarms send alerts via **SNS email notifications**.  

6. **Testing & Validation (Postman):**  
   - REST APIs validated using Postman.  
   - Anomalies confirmed across all models.  

---

## ✨ Features  

- **Multi-domain Anomaly Detection:** CPU, Network, Login, Content, Storage.  
- **RESTful API Interface:** Exposed endpoints (`/predict/cpu`, `/predict/network`, etc.).  
- **Cloud-Native Deployment:** Integrated with AWS services for scalability.  
- **Real-time Alerts:** Email notifications for anomalies.  
- **Secure Architecture:** IAM role restrictions + Security Groups.  
- **Extensible Design:** New models can be added seamlessly.  

---

## ⚙️ Tech Stack  

- **Languages & Libraries:** Python, Flask, scikit-learn, joblib, boto3  
- **Cloud Services:** AWS EC2, S3, IAM, CloudWatch, SNS  
- **Tools:** Google Colab, Postman, GitHub  
- **OS & Deployment:** Amazon Linux on EC2  

---

## 🚀 Setup & Installation  

### 1. Train Models  
Use **Google Colab** to run `helios_models.ipynb` and export `.pkl` files.  

### 2. Upload Models to S3  
- Create an S3 bucket (`helios-nitanshu`).  
- Enable versioning.  
- Upload `.pkl` files into `models/` folder.  

### 3. Launch EC2 Instance  
- Launch instance named `helios-agent`.  
- Configure Security Group: SSH(22), HTTP(80), TCP(5000).  
- Attach IAM user with `S3ReadOnlyAccess`.  

### 4. Configure EC2  
```bash
sudo yum update -y
sudo yum install python3-pip -y
pip3 install flask boto3 scikit-learn joblib
mkdir helios && cd helios && mkdir models
aws configure  # enter IAM keys
aws s3 cp s3://helios-nitanshu/models/ ./models --recursive
```  

### 5. Run Flask App  
```bash
cd helios
python3 app.py
```  

---

## 🔍 API Endpoints (Test via Postman)  

### 1. CPU Anomaly  
POST `http://<EC2_IP>:5000/predict/cpu`  
```json
{"value": 95}
```  

### 2. Network Anomaly  
POST `http://<EC2_IP>:5000/predict/network`  
```json
{"value": 600}
```  

### 3. Login Anomaly  
POST `http://<EC2_IP>:5000/predict/login`  
```json
{"value": [6,2]}
```  

### 4. Content Injection  
POST `http://<EC2_IP>:5000/predict/content`  
```json
{"text": "click http://spam.com"}
```  

### 5. Storage Anomaly  
POST `http://<EC2_IP>:5000/predict/storage`  
```json
{"value": 950}
```  

---

## 📊 CloudWatch & Alerts  

- **Dashboards:** CPUUtilization, NetworkIn, NetworkOut, Disk metrics.  
- **Alarms:** Triggers on CPU > 1% → SNS Email Notification.  
- **SNS Integration:** Instant alerts to stakeholders’ inbox.  

---

## 🎥 Demo Video  

> 📌 Add demo video link here once recorded.  

---

## 📸 Screenshots  

> 📌 Add screenshots here for each phase:  
- Model training in Colab  
- S3 bucket setup  
- EC2 configuration  
- Flask running  
- Postman tests  
- CloudWatch dashboard  
- SNS alert email  

---

## 📑 Research Alignment  

This project supports research in **AI-driven anomaly detection for cloud computing**, aligning with cloud monitoring, predictive maintenance, and self-healing infrastructure studies.  

Key points:  
- Demonstrates **practical deployment** of ML in a cloud setting.  
- Shows how anomaly detection models can be operationalized at scale.  
- Highlights the synergy between AI/ML and cloud-native monitoring tools.  

---

## 📈 Future Scope  

- ✅ Auto-remediation workflows (e.g., restart services automatically).  
- ✅ Containerization using Docker + AWS ECS/EKS.  
- ✅ Multi-region deployment for fault tolerance.  
- ✅ Support for streaming data (Kafka + Kinesis).  

---

## 🙌 Acknowledgements  

- **Open-source Libraries:** scikit-learn, Flask, boto3.  
- **Platforms:** AWS Free Tier, Google Colab.  
- **Inspiration:** Cloud-native monitoring systems & self-healing infrastructure concepts.  

---

## 📜 License  

This project is licensed under the MIT License – feel free to fork, modify, and contribute.  

---

💡 *Helios is not just a project—it’s a vision towards **autonomous, self-healing cloud systems*** 🌌  


