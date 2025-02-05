from difflib import SequenceMatcher
with open("demo_1.txt") as file1, open("demo_2.txt") as file2:
    file1_data = file1.read()
    file2_data = file2.read()
    similarity_ratio = SequenceMatcher(None, file1_data, file2_data).ratio()
    print(f"Similarity ratio: {similarity_ratio}")
    if similarity_ratio > 0.7:
        print("Plagiarism detected")
    else:
        print("No plagiarism detected")
