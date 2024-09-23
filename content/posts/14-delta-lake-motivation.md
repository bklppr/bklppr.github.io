Title: Delta Lake - Motivation: Characteristics and Challenges of Object Stores  
Date: 2024-09-14  
Category: General  
Slug: delta-lake-motivation-characteristics-object-stores  
Tags: Delta Lake, Cloud Storage, Data Management, Object Stores  

*Summary of section 2 of the [paper](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf).*

In this post, we look at the API and performance characteristics of cloud object stores and explain the challenges of building efficient table storage on them.

---

### Object Store APIs  
Cloud object stores, such as **Amazon S3**, **Azure Blob Storage**, and **Google Cloud Storage**, provide a simple key-value store interface. Users create buckets and store objects, which are binary blobs identified by a string key. These systems allow large objects (up to several terabytes) and provide metadata APIs for operations like listing objects (e.g., S3's **LIST** operation). However, these APIs are often expensive, and listing large datasets can take considerable time.

**Read operations** are optimized with support for byte-range requests, allowing efficient retrieval of parts of large objects. However, **updating objects** requires rewriting the entire object, making updates costly. Some cloud systems provide a **distributed filesystem interface** (e.g., Azure ADLS Gen2), but issues like handling small files and atomic updates persist.

---

### Consistency Properties  
Most cloud object stores offer **eventual consistency**, meaning updates may not be immediately visible across clients. For example, after a client uploads a new object, other clients might not see it right away in subsequent **LIST** or **GET** requests. Some object stores (e.g., Amazon S3) provide **read-after-write consistency** for new objects but still lack atomic operations across multiple objects, creating challenges when managing large datasets.

---

### Performance Characteristics  
To achieve high throughput with object stores, it is essential to balance **large sequential I/Os** and **parallelism**. While object stores can deliver good performance for large reads, operations like **LIST** and **write operations** are more challenging. Listing large datasets is particularly expensive because **LIST** requests are limited (e.g., S3 can return only 1000 objects per request), requiring parallelism to list datasets efficiently. 

In table storage, performance considerations include keeping data close together for sequential reads, using **columnar formats** like Parquet, and balancing object size for updates and reads.

---

### Existing Approaches for Table Storage  
There are three common approaches to managing tabular datasets on cloud object stores:

1. **Directories of Files**: The most common approach is to store tables as collections of objects, typically in a columnar format (e.g., Parquet). This method allows for partitioning based on attributes like date, but it suffers from **lack of atomicity** across multiple objects, **eventual consistency**, and **poor performance** for operations like listing objects and accessing metadata.
   
2. **Custom Storage Engines**: Some systems (e.g., **Snowflake**) manage metadata in a separate, strongly consistent service to avoid issues like partial updates. However, this requires a proprietary service and adds overhead when querying data using external computing engines. This approach can also lock users into a specific provider.

3. **Metadata in Object Stores**: Delta Lake introduces a new approach by storing the **transaction log** and **metadata** directly within the cloud object store. By using protocols over object store operations, Delta Lake ensures **serializability** while storing data in Parquet format. This approach allows for efficient metadata access and compatibility with other systems that support Parquet.
