Background
----------

In real-world backend systems, a single API request often depends on data from **multiple external services**.For example:

*   User profile service
    
*   Orders service
    
*   Payments service
    

If these APIs are called **one after another**, the total response time becomes slow and directly impacts user experience.Demonstrates how **multithreading** can be used to make such API calls **concurrently**, reducing overall latency.

Problem Statement
-----------------

Build a Python backend module that fetches data from **multiple external APIs in parallel** instead of sequentially.

The goal is to:

*   Reduce total response time
    
*   Learn how multithreading works for I/O-bound tasks
    
*   Compare performance between sequential and concurrent execution
    

Functional Requirements
-----------------------

### Input

*   A list of API endpoints (URLs)
    
*   Optional request headers
    
*   Timeout value (in seconds)
    

### Output

*   API response status for each endpoint
    
*   Time taken by each API call
    
*   Total execution time
    
*   Comparison of:  Sequential execution time & Concurrent execution time
    

Sample APIs for Testing
-----------------------

You can use public APIs such as:

*   [https://httpbin.org/delay/2](https://httpbin.org/delay/2)
    
*   [https://httpbin.org/delay/3](https://httpbin.org/delay/3)
    
*   [https://jsonplaceholder.typicode.com/posts/1](https://jsonplaceholder.typicode.com/posts/1)
    
*   [https://jsonplaceholder.typicode.com/users/1](https://jsonplaceholder.typicode.com/users/1)
    

These are intentionally slow to make concurrency benefits visible.