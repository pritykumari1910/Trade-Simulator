import time

def record_latency(start_time):
    latency = time.time() - start_time
    print(f"[Latency] {latency:.6f} sec")
