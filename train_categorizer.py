from dotenv import load_dotenv
import os
import openai

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Predefined categories and sub-categories
categories = {
    "Medical Assistance": ["Medical Assistance"],
    "Security": ["Eve-teasing/Misbehaviour with lady passengers/Rape", "Theft of Passengers Belongings/Snatching",
                 "Unauthorized person in Ladies/Disabled Coach/SLR/Reserve Coach",
                 "Harassment/Extortion by Security Personnel/Railway personnel", "Nuisance by Hawkers/Beggar/Eunuch",
                 "Luggage Left Behind/Unclaimed/Suspected Articles", "Passenger Missing/Not responding call",
                 "Smoking/Drinking Alcohol/Narcotics", "Dacoity/Robbery/Murder/Riots", "Quarrelling/Hooliganism",
                 "Passenger fallen down", "Nuisance by passenger", "Misbehaviour", "Others"],
    "Divyangjan Facilities": ["Divyangjan coach unavailability", "Divyangjan toilet /washbasin",
                              "Braille signage in coach", "Others"],
    "Facilities for Women with Special needs": ["Baby Food"],
    "Electrical Equipment": ["Air Conditioner", "Fans", "Lights", "Charging Points", "Others"],
    "Coach - Cleanliness": ["Toilet", "Washbasin", "Cockroach / Rodents", "Coach Interior", "Coach Exterior", "Others"],
    "Punctuality": ["NTES APP", "Late Running", "Others"],
    "Water Availability": ["Packaged Drinking Water / Rail Neer", "Toilet", "Washbasin", "Others"],
    "Coach - Maintenance": ["Window/Seat Broken", "Window/Door locking problem", "Tap leaking/Tap not working",
                            "Broken/Missing Toilet Fittings", "Jerks/Abnormal Sound", "Others"],
    "Catering & Vending Services": ["Overcharging", "Service Quality & Hygiene", "Food Quality & Quantity",
                                    "E-Catering", "Food & Water Not Available", "Others"],
    "Staff Behaviour": ["Staff Behaviour"],
    "Corruption / Bribery": ["Corruption / Bribery"],
    "Bed Roll": ["Dirty / Torn", "Overcharging", "Non Availability", "Others"]
}


def categorize_complaint(text):
    # Construct a detailed prompt to guide the model
    prompt = (
        "You are a helpful assistant that categorizes railway complaints into predefined categories and sub-categories. "
        "Here are the available categories and their sub-categories:\n\n"
    )
    for cat, subcategories in categories.items():
        prompt += f"{cat}: {', '.join(subcategories)}\n"
    prompt += (
        "\nCategorize the following complaint based on these categories and sub-categories. "
        "If the complaint doesn't fit into any category or sub-category, respond with 'Uncategorized'.\n\n"
        f"Complaint: {text}"
    )

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant that categorizes railway complaints into predefined categories and sub-categories."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the category and sub-category
    raw_response = response['choices'][0]['message']['content'].strip()

    # Initialize default category and sub-category
    category = "Miscellaneous"
    sub_category = "Miscellaneous"

    # Check against predefined categories and sub-categories
    found = False
    for cat, subcategories in categories.items():
        for sub in subcategories:
            if sub.lower() in raw_response.lower():
                category = cat
                sub_category = sub
                found = True
                break
        if found:
            break

    return category, sub_category

