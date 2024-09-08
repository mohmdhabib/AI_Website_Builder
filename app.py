import requests
from langchain_ollama.llms import OllamaLLM

# Unsplash API settings
UNSPLASH_ACCESS_KEY = 'PXbkQKESJO-k-E1SQoCsDIIJbPncLcVeeljtCR2dQAY'

def get_images_from_unsplash(query, per_page=1):
    url = "https://api.unsplash.com/search/photos"
    params = {
        'query': query,
        'client_id': UNSPLASH_ACCESS_KEY,
        'per_page': per_page,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        images = [img['urls']['regular'] for img in data['results']]
        return images
    else:
        print(f"Error fetching images: {response.status_code}")
        return None

def extract_keywords_for_image(user_input):
    # Use LLM to extract the most relevant keywords for an image search
    llm = OllamaLLM(model="llama3.1", temperature=0.5)
    
    # Define the prompt to extract the most relevant image query from the user's input
    prompt = f"""
    Extract the most relevant keywords for an image search based on the following task description: "{user_input}".
    Provide the keywords in a concise form without any additional text.
    """
    
    # Call the model with the prompt
    keywords = llm.invoke(prompt)
    
    return keywords.strip()  # Clean the response

def generate_code_with_images(user_input):
    # Step 1: Extract relevant keywords for image search
    image_query = extract_keywords_for_image(user_input)
    
    # Step 2: Fetch an image based on the extracted keywords
    images = get_images_from_unsplash(image_query, per_page=1)
    if images:
        image_url = images[0]  # Use the first image found
    else:
        image_url = "https://via.placeholder.com/150"  # Fallback image if none found

    # Step 3: Use LLM to generate HTML, CSS, and JavaScript with the image included
    llm = OllamaLLM(model="llama3.1", temperature=0.8)
    
    # Define the prompt to generate the website code
    prompt = f"""
    Generate modern and responsive website code in HTML, CSS, and JavaScript for the following task: "{user_input}". 
    Include the following image in the code: <img src="{image_url}" alt="Related image">.
    
    Only provide the code without any explanation or comments. 
    
    The format should be:
    <html>
    <!-- HTML code here -->
    </html>
    <style>
    /* CSS code here */
    </style>
    <script>
    // JavaScript code here
    </script>
    
    Use Bootstrap or Google Fonts, and make sure to include the import statements explicitly.
    """
    
    # Step 4: Call the model to generate the code with the image URL
    response = llm.invoke(prompt)
    
    return response

