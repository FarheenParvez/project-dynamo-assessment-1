An Apache-style access log is located at /app/access.log.

Parse the log and write a JSON summary to /app/report.json.

Success criteria:

1. Write the output to /app/report.json.
2. The output must be a single JSON object.
3. The JSON object must contain exactly these keys:
   - "total_requests"
   - "unique_ips"
   - "top_path"
4. "total_requests" must equal the number of non-empty log entries.
5. "unique_ips" must equal the number of distinct client IP addresses (the first whitespace-separated field on each line).
6. "top_path" must equal the request path that appears most frequently across all requests (the path from the HTTP request line, e.g. "/index.html").

Do not modify /app/access.log.