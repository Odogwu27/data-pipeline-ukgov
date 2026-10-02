# Automated Azure Cloud ETL Data Pipeline Platform

## 📌 Project Overview
An enterprise-grade, decoupled Data Engineering pipeline designed to automatically extract, load, and verify semi-structured public service data feeds. This platform transitions manual data ingestion workflows into an automated cloud data lakehouse architecture, utilizing secure IAM protocols and local task orchestration to ensure consistent data delivery.

## 🏗️ Architecture Blueprint
[ 1. Data Origin ]       ──►   
[ 2. Processing Engine ]   ──►  
[ 3. Target Cloud Data Lake ]
Official UK Gov API             Python 3.13 Runtime               Azure Blob Storage Account
(Semi-Structured JSON)         Local Task Scheduler CLI           Container: raw-data-landing

## 🛠️ Tech Stack & Cloud Infrastructure Matrix
* **Cloud Infrastructure Environment:** Microsoft Azure Platform
* **Object Storage Layer (Data Lake):** Azure Blob Storage (Staging Drop-Zone Container Network)
* **Secure Access Protocol:** Identity Access Management (IAM) Shared Cryptographic Connection Strings
* **Core Scripting Language Engine:** Python 3.13 Runtime Environment
* **External Core Library Dependencies:** `requests` (API Handshakes), `json` (Data Serialization), `azure-storage-blob` (Cloud SDK Contexts)
* **Pipeline Orchestrator & Monitor:** Windows Task Scheduler Engine

## ⚙️ Core Engineering Pipeline Workflows
1. **Data Ingestion (Extract & Load):** Programmatic HTTP get requests query the endpoint to grab live JSON payloads. The system enforces an *Idempotent file-naming convention* using dynamic execution timestamps (`YYYYMMDD_HHMMSS`) to prevent tracking record overwrites.
2. **Cloud Security Handshake:** Connections to the target storage lake are completely decoupled from local hard drives. The script utilizes isolated environment parameters to negotiate encrypted data transfers straight to the cloud staging zone.
3. **Automated Orchestration:** A localized task engine runs background cron-style executions to trigger pipeline instances cleanly at scheduled intervals, eliminating manual runtime requirements.
4. **Schema-On-Read Verification:** Raw landing objects maintain structural integrity formats, rendering clear database schema profiles directly compatible with downstream analytical query tools (T-SQL, Synapse, Power BI).

## 🚀 Key Professional Skills Demonstrated
* **Cloud Systems Architecture & Operations (DevOps)**
* **Identity Access Management (IAM) Security Implementations**
* **Semi-Structured Data Handling & Parsing (JSON Objects)**
* **Decoupled System Architecture Design Principles**
* **Automated Data Pipeline Scheduling & Orchestration**
