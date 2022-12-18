from bs4 import BeautifulSoup
import requests
import smtplib
# import lxml

email = "your mail id"
password = "your mail access pwd(generated)"

amazon_product_url = "https://www.amazon.in/Noise-ColorFit-Display-Monitoring-Smartwatches/dp/B09NVP6HXY/?_encoding=UTF8&pd_rd_w=k7MvE&content-id=amzn1.sym.86bd9ba7-f177-459f-9995-c8e962dd9848&pf_rd_p=86bd9ba7-f177-459f-9995-c8e962dd9848&pf_rd_r=833ZK6JV333EMM3Q3PTR&pd_rd_wg=3lziS&pd_rd_r=a79cdfc9-4857-4278-9531-fe864bf21648&ref_=pd_gw_ci_mcx_mi&th=1"
headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

response = requests.get(url=amazon_product_url, headers=headers)
amazon_product_html = response.text

soup = BeautifulSoup(amazon_product_html, "html.parser")
product_cost = soup.find(class_="a-section a-spacing-none aok-align-center")
cost_in_string = product_cost.find("span", class_="a-price-whole").text
price = float(cost_in_string.rstrip('.').replace(",", ""))
print(price)

if price < 1999:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs="mail address you want to send",
        msg=f"The product 'Noise ColorFit Pulse' you wanna buy is triggered the lowest set by you. The current price is {price}.\n{amazon_product_url}"
    )
    print("mail sent")


