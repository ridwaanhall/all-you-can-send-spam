import requests

class MailSender:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def send_mail(self, payload):
        try:
            # Sending the HTTP POST request
            response = requests.post(self.url, headers=self.headers, data=payload, timeout=10)
            # Check if the request was successful
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
        return None

def main():
    # URL where the form submits data
    url = "https://sia.uty.ac.id/mail/send_mail"

    # Custom headers can include content type, user-agent etc.
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }

    # Prepare payload with the data to be sent
    payload = {
        'nomor_id': '0',
        'nama': 'Unknown',
        'waktu': '1000-01-01 00:00:01',
        'referensi': 'http:///std',
        'ip': '111.000.001.100 ( 111.000.001.100 )',
        'platform': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        'pesan': 'None'
    }

    # Create an instance of the MailSender class
    mail_sender = MailSender(url, headers)

    # Send mail using the send_mail method
    response = mail_sender.send_mail(payload)
    
    # Process the response if sending was successful
    if response:
        if response.status_code == 200:
            print("Mail sent successfully!")
            # print("with response: ", response.text)
        else:
            print(f"Failed to send mail. Status code: {response.status_code}")
    else:
        print("Failed to send mail due to an exception.")

if __name__ == "__main__":
    main()
