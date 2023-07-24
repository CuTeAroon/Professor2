#Create api method program bxb 
 #Facebook sidra_malik 
  
 import requests 
  
 def make_facebook_api_request(endpoint, access_token): 
     base_url = "https://graph.facebook.com/v14.0/"  # Update the API version as needed 
     url = f"{base_url}{endpoint}" 
     params = {"access_token": access_token} 
  
     response = requests.get(url, params=params) 
  
     if response.status_code == 200: 
         return response.json() 
     else: 
         print(f"Error {response.status_code}: {response.text}") 
         return None 
  
 # Example usage: 
 access_token = "YOUR_ACCESS_TOKEN" 
 user_info = make_facebook_api_request("me", access_token) 
 if user_info: 
     print(user_info)
