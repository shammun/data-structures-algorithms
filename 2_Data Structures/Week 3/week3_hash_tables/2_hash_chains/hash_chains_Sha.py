class HashTable:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]
        self.p = 1000000007
        self.x = 263

    def hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self.x + ord(c)) % self.p
        return ans % self.bucket_count
    
    def add(self, string):
        hash_key = self.hash_func(string)
        if string not in self.buckets[hash_key]:
            self.buckets[hash_key].insert(0, string)

    def delete(self, string):
        hash_key = self.hash_func(string)
        if string in self.buckets[hash_key]:
            self.buckets[hash_key].remove(string)
    
    def find(self, string):
        hash_key = self.hash_func(string)
        return "yes" if string in self.buckets[hash_key] else "no"

    def check(self, i):
        return " ".join(self.buckets[i])
    
def process_queries(bucket_count, queries):
    hash_table = HashTable(bucket_count)
    result = []

    for query in queries:
        query = query.split()
        if query[0] == "add":
            hash_table.add(query[1])
        elif query[0] == "del":
            hash_table.delete(query[1])
        elif query[0] == "find":
            result.append(hash_table.find(query[1]))
        elif query[0] == "check":
            result.append(hash_table.check(int(query[1])))
        
    return result
    
def main():
    bucket_count = int(input())
    n = int(input())
    queries = [input() for _ in range(n)]

    result = process_queries(bucket_count, queries)
    print("\n".join(result))

if __name__ == "__main__":
    main()
