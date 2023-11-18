from django.shortcuts import render


import requests
import json

def virusTotal(ip):
    api_key = '4c7961ebec72afb28a6ffe97a9c59281675264cedb9be53856c5f7655652a62f'
    
    headers = {
        'x-apikey': api_key,
        'Accept': 'application/json'
    }

    try:
        response = requests.get(f'https://www.virustotal.com/api/v3/ip_addresses/{ip}', headers=headers)
        print(response.headers)
        result = json.loads(response.text)
        return result['data']['attributes']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
ip_address = '8.8.8.8'
result = virusTotal(ip_address)
if result:
    print(result)


def virus_total_view(request, ip_address):
    result = virusTotal(ip_address)
    context = {'result': result, 'ip_address': ip_address}
    return render(request, 'index.html', context)

