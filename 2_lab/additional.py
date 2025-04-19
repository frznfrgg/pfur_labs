import re

with open("data/server_logs.txt") as f:
    lines = f.readlines()
    lines = [re.findall(r"\[(.*?)\]", line) for line in lines]
    
    successful_requests = 0
    total_data = 0
    ips = set()
    for _, _, ip, _, _, status, size in lines:
        ips.add(ip)
        if status == "200":
            successful_requests += 1
        total_data += int(size)
    sorted_lines = sorted(lines, key=lambda x: (x[0], x[1]))
    print(sorted_lines)

with open("results/log_analysis.txt", "w") as f:
    f.write(f"Total successful requests: {successful_requests}\n")
    f.write(f"Total data transferred: {total_data} bytes\n")
    f.write(f"Unique IP addresses: {len(ips)}\n")
