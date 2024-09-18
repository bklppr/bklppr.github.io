Title: ACID Transactions in Databases
Date: 2024-09-18
Category: General
Slug: acid-transactions
Tags: Data Integrity

ACID (Atomicity, Consistency, Isolation, Durability) defines properties essential for reliable database transactions.

1. **Atomicity**: A transaction is all-or-nothing. If any part fails, the entire transaction is rolled back.  
   *Example*: When updating both a customer's address and billing information, either both changes are saved successfully, or none if one fails.

2. **Consistency**: Transactions move the database from one valid state to another, maintaining all rules and constraints.  
   *Example*: A transaction that updates an insurance claim must ensure it adheres to the insurance policy’s terms (e.g., limits and deductibles); otherwise, it is rejected.

3. **Isolation**: Transactions are executed independently, without intermediate states affecting others.  
   *Example*: Two insurance underwriters calculating risk on the same policy will not see each other’s incomplete updates during the process.

4. **Durability**: Once committed, a transaction is permanent, even in case of system failure.  
   *Example*: Once an insurance claim approval is finalized, it remains in the system.