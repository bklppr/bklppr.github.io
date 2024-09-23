Title: Lakehouse - Motivation: Data Warehousing Challenges  
Date: 2024-09-19  
Category: General  
Slug: lakehouse-motivation  
Tags: Lakehouse, Data Warehousing, Data Lakes, Data Management  

*Summary of section 2 of the [paper](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf).*

While data warehouses are critical to many business processes, they pose challenges with **data quality issues**, **staleness**, and **high costs**. These challenges, in part, stem from the **"accidental complexity"** introduced by the separation of data lakes and warehouses in current architectures. The Lakehouse architecture aims to solve these problems.

---

### Key Challenges with Data Warehousing

1. **Data Quality and Reliability**:  
   One of the biggest challenges reported by enterprise data users is data quality. The two-tier architecture (separate data lakes and warehouses) adds complexity to data pipelines. Differences in data types, SQL dialects, and schemas between the lake and warehouse can lead to failures and bugs during ETL processes, worsening data quality.

2. **Data Staleness**:  
   Many business applications require up-to-date data, but the current architecture introduces **data staleness** due to staging data in lakes before loading it into the warehouse. Batch jobs delay data availability, and while streaming pipelines could reduce this lag, they are harder to operate. In first-generation systems, users had immediate access to data from operational systems, minimizing staleness.

3. **Unstructured Data**:  
   A growing fraction of enterprise data is **unstructured** (e.g., images, sensor data, documents). Traditional SQL data warehouses struggle to support these data types, making it harder for organizations to manage and analyze unstructured data.

4. **Machine Learning and Data Science**:  
   **Machine learning (ML)** and **data science** applications often need to process large datasets using non-SQL code, which is inefficient over traditional data warehouse interfaces (e.g., ODBC/JDBC). Moreover, these applications face the same challenges of **data quality**, **consistency**, and **isolation** as classical analytics, creating a need for better data management systems that support these workloads.

---

### Industry Trends Towards Lakehouses

Several industry trends indicate dissatisfaction with the two-tier model:

- **External Table Support**: Major data warehouses have added support for **external tables** in formats like Parquet and ORC, allowing users to query the data lake directly from the warehouse. However, this does not resolve the management complexities or performance issues, as these systems are optimized for their internal formats.
- **SQL Engines on Data Lakes**: Engines like **Spark SQL**, **Presto**, **Hive**, and **AWS Athena** allow querying data lake storage directly, but data lakes still lack key features like **ACID transactions** and **indexing**, which are necessary to achieve data warehouse-level performance and reliability.

---

These challenges and trends show that the two-tier architecture is struggling to meet modern data needs. The Lakehouse aims to provide a unified architecture that eliminates the complexity and inefficiencies of current systems.
