import requests

def send_real_subs(user_link):
    # یہ وہ جگہ ہے جہاں اصلی کام ہوتا ہے
    api_url = "https://smm-provider.com/api/v2" 
    my_key = "YOUR_SECRET_API_KEY" # یہاں آپ کی اپنی چابی لگے گی
    
    data = {
        'key': my_key,
        'action': 'add',
        'service': '102', # یہ اصلی سبسکرائبر سروس کا کوڈ ہے
        'link': user_link,
        'quantity': '1000' # جتنے سبسکرائبر آپ بھیجنا چاہتے ہیں
    }
    
    response = requests.post(api_url, data=data)
    return response.json()