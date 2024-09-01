from cleantext import preprocess_text
from categorizer import categorize_complaint


sample_text = ""
clean_text = preprocess_text(sample_text)
category, sub_category = categorize_complaint(clean_text)
print(category, sub_category)