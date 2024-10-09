Title: Delta Lake: Higher-Level Features  
Date: 2024-09-16  
Category: General  
Slug: delta-lake-higher-level-features  
Tags: Delta Lake, Data Management, Time Travel, Data Layout

*Summary of section 4 of the [paper](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf).*

Delta Lake’s transactional design enables a range of high-level features similar to traditional analytical databases. In this post, we look at some of the most widely used features.

---

### Time Travel and Rollbacks  
Data pipelines often encounter issues, especially when ingesting “dirty” data. With traditional data lakes, it is difficult to undo updates that have already been applied. Similarly, some workflows, such as machine learning, require reproducing old versions of data for comparisons.

Delta Lake’s immutable data objects and logs make it easy to query past snapshots of data using **time travel**. Users can specify a **timestamp** or a **commit ID** to read a previous version of the table. This feature is particularly useful for fixing errors in data pipelines or restoring data for machine learning experiments. Additionally, Delta Lake supports a **CLONE** command to create a copy-on-write a copy-on-write new version of a table starting at one of its existing snapshots.

---

### Efficient UPSERT, DELETE, and MERGE  
Many enterprise datasets need to be updated over time due to regulatory requirements like **GDPR**, data correction, or late-arriving data. In traditional data lakes, applying these updates can be challenging without pausing reads.

Delta Lake allows **UPSERT**, **DELETE**, and **MERGE** operations to be performed **transactionally**, replacing updated objects with new ones in the Delta log. This ensures that updates are applied atomically, with no partial updates visible to other users.

---

### Streaming Ingest and Consumption  
Deploying **streaming pipelines** is often complex in traditional cloud data lakes. To handle real-time data ingestion, users typically rely on separate message buses like **Apache Kafka** or **Kinesis**, which adds management overhead.

Delta Lake integrates features that allow users to treat a Delta table as a **message queue**, eliminating the need for separate message systems in many scenarios:

- **Write Compaction**: Small objects are compacted into larger ones in the background, improving read performance while preserving write speed for real-time streaming.
- **Exactly-Once Streaming Writes**: Delta Lake enables **exactly-once writes**, ensuring that streaming jobs avoid duplicate writes after failures.
- **Efficient Log Tailing**: Consumers can easily find new records using **log tailing**, making it easy for streaming applications to process only the new data.

These features allow many users to build streaming pipelines directly on low-cost cloud object stores with Delta, avoiding the need for separate messaging infrastructure.

---

### Data Layout Optimization  
Optimizing **data layout** is crucial for improving query performance in analytical systems, especially for highly selective queries. Delta Lake allows background processes to optimize data layout without affecting other operations. 

- **OPTIMIZE Command**: Users can run the **OPTIMIZE** command to compact small objects and compute missing statistics. By default, it creates 1 GB-sized objects, but this can be customized.
- **Z-Ordering by Multiple Attributes**: Delta Lake supports **Z-ordering** to cluster data along multiple attributes (e.g., `sourceIp`, `destIp`, `time`). This improves locality and reduces the amount of data read during queries, making it especially useful for highly selective workloads.

---

### Caching  
Many cloud users run long-lived clusters for ad-hoc queries. Delta Lake supports **caching** on local storage (e.g., SSDs), improving performance by storing frequently accessed data and metadata locally. Since Delta objects are immutable, caching is safe and can significantly speed up queries.

---

### Audit Logging  
Delta Lake’s **transaction log** can be used for **audit logging** by recording commit information in `commitInfo` records. This ensures data security and compliance, as users can track the history of changes to the table. Delta Lake’s **DESCRIBE HISTORY** command allows users to view this history, ensuring transparency and auditability.

---

### Schema Evolution and Enforcement  
Over time, datasets often require **schema changes**. Delta Lake supports schema changes **transactionally**, ensuring that updates are applied consistently. Delta’s transaction log keeps track of schema updates, allowing old data to be queried with new schemas without needing to rewrite the data. This prevents errors caused by mismatched schemas during data ingestion.
