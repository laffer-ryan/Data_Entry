from playwright.sync_api import sync_playwright
import time
import csv

# orders = [3000, 3001, 3002]
# # is used to indicate an html id 

# import orders from a csv file
with open("orders.csv", "r") as f:
    reader = csv.reader(f)
    orders = [order[0] for orders in reader]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.opencart.com")
    page.get_by_placeholder("Username").fill("your_username") # Use to fill in a username on a form
    page.get_by_placeholder("Password").fill("your_password") # Use to fill in a password on a form
    page.get_by_role("button", name="Login").click() # Use to click a button on the page
    time.sleep(5)
    page.get_by_role("button", name="Login").click() # Use to click a button on the page
    page.get_by_role("button").nth(1).click() # Get the nth button selector
    time.sleep(5)


    page_url = page.url
    sales_page = page.url.replace("common/dashboard", "sale/order|info")


    results = []
    # Loops through different orders on different pages, print the results and append them to a list.
    for order in orders:
        page.goto('{sales_page}&order_id={str.order}')
        shipping_method = page.query_selector(
            "#input-shipping-mehthod > option:nth-child(2)"
        )

        if shipping_method:
            print(shipping_method.text_content())
            results.append((order, shipping_method.text_content()))
        time.sleep(2)
    browser.close()
    print(results)