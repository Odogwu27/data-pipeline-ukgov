# Multi-Cloud Data Engineering Platform: Automated UK Gov Ingestion & Data Warehousing
An end-to-end modern data platform orchestrating automated batch data pipelines, enterprise-grade credential isolation, multi-cloud relational warehousing, and centralized corporate data governance framework structures across Microsoft Azure and Snowflake.

## 🏛️ Enterprise Architecture Overview
*   *Orchestration & Ingestion:* Configured serverless ingestion workflows via *Azure Data Factory (ADF)* to pull multi-line JSON datasets natively from the UK Gov public REST API into an enterprise data lake container.
*   *Security & Identity Governance:* Hardened the cloud infrastructure network perimeter using *Azure Key Vault. Isolated access token strings under strict **Azure Role-Based Access Control (RBAC)* policies using custom Key Vault Secrets Officer identity clearances.
*   *Cloud Data Warehousing:* Built an enterprise relational analytics engine within *Snowflake* to handle complex sharded analytics data. Implemented a secure cloud-native *External Stage Bridge* using Azure SAS tokens to automatically map and bulk-ingest raw files cleanly via bulk COPY INTO SQL script streams.
*   *Central Data Governance:* Deployed *Microsoft Purview* within the local region network pool to ensure complete end-to-end transactional compliance, asset mapping, data lineage, and metadata discovery patterns across corporate files.

## 🚀 Key Engineering Milestones Cleared
1.  *Production Credential Isolation:* Eliminated raw text passwords from cloud codes by establishing automated secret-fetching parameters via enterprise vaults.
2.  *Infrastructure Pivot Agility:* Successfully managed cloud vendor subscription and regional quota limits by pivoting compute resources smoothly over to multi-cloud server configurations (Snowflake) with zero network data loss.
3.  *Regional Network Optimization:* Co-located core tracking layers inside the local UK South data hubs to lower operational network latency and completely remove cross-region traffic costs.
