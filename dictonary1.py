dict={
    "pankha":"fan",
    "kitab":"notebook",
    "dabba":"box"
}
print("options are", dict.keys())
a=input("Enter your Hindi word: ")
print("English translation of your hindi word is:",dict.get(a))