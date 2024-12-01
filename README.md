# Fraud Detection for Card transactions

Target Solution Architecture

![img.png](img.png)

TODOs:
- [ ] Create automation script to set up environment on any cloud or VM
  - [X] Kubernetes
  - [X] PostgreSQL
  - [X] Kafka
  - [ ] *Kubeflow+Mlflow
  - [ ] *Spark
- [ ] Ingest data from CSV to the PG
- [ ] Stream data from PG to the Kafka "Transactions" topic
- [ ] *Deploy Pytorch model for fraud detection
- [ ] Deploy Spark MLlib model for fraud detection 
- [ ] *Create data exploration notebook on the PG data
- [ ] Notebooks
  - [ ] *model training notebook using Pytorch
  - [ ] model training notebook with MLlib
- [ ] *Pipelines
  - [ ] *data drift detection pipeline
  - [ ] *model training using Pytorch
  - [ ] *model training using Spark
- [ ] Visualization of Fraud detection results
