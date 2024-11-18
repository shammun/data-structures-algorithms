from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()  # Use deque to store finish times of packets

    def process(self, request):
        # Remove all packets that have finished processing by the time this packet arrives
        while self.finish_time and self.finish_time[0] <= request.arrived_at:
            self.finish_time.popleft()

        # Check if the buffer is full
        if len(self.finish_time) == self.size:
            return Response(True, -1)  # Packet is dropped

        # Calculate the start time of the current packet
        if not self.finish_time:
            # Buffer is empty, so packet starts processing immediately
            start_time = request.arrived_at
        else:
            # Buffer is not empty, so packet starts processing after the last packet finishes
            start_time = self.finish_time[-1]

        # Calculate the finish time of the current packet and add it to the buffer
        finish_time = start_time + request.time_to_process
        self.finish_time.append(finish_time)

        # Return the response indicating that the packet was processed and its start time
        return Response(False, start_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
