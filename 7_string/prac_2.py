#151. Reverse Words in a String


s = "  hello   world  "

# ✅ Step 1: strip() --> Remove starting & ending extra spaces only
# ✅ split() --> Break karega string ko words mein, beech ke multiple spaces ko ignore karega
# Example: "  hello   world  " --> ['hello', 'world']
words = s.strip().split()

# ✅ Step 2: Reverse the list of words
# words[::-1] --> List ko ulta kar dega
# ['hello', 'world'] --> ['world', 'hello']
words = words[::-1]

# ✅ Step 3: Join words with single space
# ' '.join(words) --> Words ko ek single space se jod ke final string bana dega
# ['world', 'hello'] --> "world hello"
result = ' '.join(words)

# ✅ Final output print karo
print(result)