Title: Delta Lake - Storage Format and Access Protocols  
Date: 2024-09-15  
Category: General  
Slug: delta-lake-storage-format-and-access-protocols  
Tags: Delta Lake, Data Management, Storage Format  

*Summary of section 3 of the [paper](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf).*

Delta Lake uses a directory on a cloud object store or file system to manage table contents and maintain a log of transaction operations. This ensures data consistency and atomicity using **optimistic concurrency control**. In this post, we look at Delta Lake's storage format and access protocols, which support **serializable** and **snapshot isolation**.

---

### Storage Format  
Each **Delta Lake table** is stored in a directory or with a common key prefix in an object store. The data is stored in **Apache Parquet** format, and the metadata and transaction log are kept in a subdirectory (`_delta_log`).

- **Data Objects**: Table data is stored as Parquet files, partitioned by columns if needed (e.g., date). Parquet was chosen for its compression support, columnar format, and compatibility with many big data engines.
  
- **Transaction Log**: Stored in the `_delta_log` subdirectory, the transaction log consists of JSON objects, each representing changes (e.g., adding/removing files). Log entries include actions like `add`, `remove`, and metadata updates. It allows for a historical record of all operations performed on the table, enabling time travel and versioning.

- **Log Checkpoints**: To improve performance, Delta Lake periodically compacts logs into **checkpoints** in Parquet format. Checkpoints store the table state at a specific point and reduce the number of logs that need to be replayed during reads.

---

### Access Protocols  
Delta Lake uses access protocols to ensure **serializable transactions** on object stores that provide eventual consistency.
Serializable transactions are the highest level of isolation in a database or storage system. They ensure that each transaction is completed without being affected by others, as though transactions were processed one by one, even if they are actually processed concurrently. This guarantees that the final outcome is consistent, just as if the transactions had been processed serially.
The key element is the log record (e.g., `000003.json`), which contains a sequence of actions that clients use to reconstruct the table’s state. The following steps describe how Delta Lake manages reads and writes:

- **Reading from Tables**: A read transaction starts by retrieving the latest checkpoint and subsequent logs, reconstructing the table state based on the `add` and `remove` actions. This ensures that reads return a consistent snapshot, even with eventual consistency in the object store.
  
- **Write Transactions**: When writing data, a client reads the latest log record and attempts to write a new log entry. Only one client can write the next log entry, ensuring atomicity for write transactions. Delta Lake's protocol supports retrying failed write attempts.

---

### Available Isolation Levels  
Delta Lake supports two isolation levels:

- **Snapshot Isolation**: This ensures that each read transaction sees a consistent snapshot of the table as it existed at the start of the transaction. Even if writes happen during the read, the snapshot doesn’t change, providing stability for analysis.

- **Serializable Isolation**: This is the strongest form of isolation, where write transactions are executed in sequence as if they occurred one after the other. This prevents conflicts and guarantees that no transactions interfere with each other, ensuring data integrity.

---

### Transaction Rates  
Delta Lake’s transaction rate is limited by the latency of writing new log records, which usually takes tens to hundreds of milliseconds. This is sufficient for most applications, including those that ingest streaming data. Read transactions, which only retrieve data, can run concurrently without contention.
