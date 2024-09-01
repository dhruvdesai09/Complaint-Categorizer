from cleantext import preprocess_text
from categorizer import categorize_complaint


sample_text = "There are hooligans teasing women in my coach"
clean_text = preprocess_text(sample_text)
category, sub_category = categorize_complaint(clean_text)
print(f"Category:{category} \nSub-category:{sub_category}")