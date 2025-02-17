morphology_rules = {
 "prefixes": ["un","re", "in", "dis"],
 "roots": ["play", "work", "use", "do"],
 "suffixes": ["ing", "ed", "er", "able", "s"],
}
def is_valid_word(word, rules):
 
 prefixes = rules["prefixes"]
 roots = rules["roots"]
 suffixes = rules["suffixes"]
 original_word = word

 for prefix in prefixes:
  if word.startswith(prefix):
    word = word[len(prefix):]
    break
 for root in roots:
  if word.startswith(root):
    word = word[len(root):]
    break
  else:
    return False
 for suffix in suffixes:
  if word.endswith(suffix):
    word = word[: -len(suffix)]
    break

 return word == ""

test_words = [
 "unplayable",
 "reworking",
 "inuse",
 "displayer",
 "nonsense",
 "playinged",
 'unplaying',
 'jumped',


]
for word in test_words:
 print(f"Word: {word}, Valid: {is_valid_word(word, morphology_rules)}")