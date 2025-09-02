from collections import defaultdict, Counter, deque
import heapq

# Lists and list comprehensions (useful for storing and manipulating data)
data = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
print(f"Multiples of 3 or 5: {data[:10]}...")

# Dictionaries (often used for feature engineering and storing model parameters)
word_vectors = {
    "AI": [0.2, 0.8, -0.3, 0.5],
    "ML": [0.5, 0.1, 0.9, -0.2],
    "Deep": [-0.1, 0.3, 0.7, 0.4]
}

# Defaultdict (useful for counting occurrences or grouping data)
word_counts = defaultdict(int)
text = "AI and ML are subfields of computer science that often overlap"
for word in text.split():
    word_counts[word.lower()] += 1

print("\nWord counts:")
print(dict(word_counts))

# Counter (efficient for counting and finding most common elements)
char_counts = Counter(text.lower())
print("\nMost common characters:")
print(char_counts.most_common(5))

# Sets (useful for efficient lookup and removing duplicates)
unique_words = set(text.split())
print(f"\nUnique words: {unique_words}")

# Tuples (used for immutable data and as dictionary keys)
data_point = (10, 20, 30)
labeled_data = [(1, [0.5, 0.3, 0.8]), (0, [0.1, 0.9, 0.2])]

# Deque (efficient for queue operations, useful in some ML algorithms)
buffer = deque(maxlen=5)
for i in range(10):
    buffer.append(i)
print(f"\nLast 5 elements: {list(buffer)}")

# Heapq (useful for priority queues, e.g., in search algorithms)
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(data)
print(f"\nTop 3 smallest elements: {[heapq.heappop(data) for _ in range(3)]}")

# Custom class (for creating more complex data structures)
class DataPoint:
    def __init__(self, features, label):
        self.features = features
        self.label = label
    
    def distance(self, other):
        return sum((a - b) ** 2 for a, b in zip(self.features, other.features)) ** 0.5

# Example usage of custom class
dataset = [
    DataPoint([1, 2, 3], 0),
    DataPoint([4, 5, 6], 1),
    DataPoint([7, 8, 9], 1)
]

print("\nDistances between data points:")
for i, point1 in enumerate(dataset):
    for j, point2 in enumerate(dataset[i+1:], i+1):
        print(f"Distance between point {i} and {j}: {point1.distance(point2):.2f}")

# Annotation: These data structures are fundamental in implementing various ML algorithms.
# For example, dictionaries are used in neural network weight storage, deques in sequence models,
# heapq in search algorithms, and custom classes in representing complex data or model architectures.