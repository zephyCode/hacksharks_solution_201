import requests as r
from bs4 import BeautifulSoup
import smtplib
import sqlite3
import schedule as sc


def get_url(interests):
    url = "https://paperswithcode.com/search?q_meta=&q_type=&q={}".format(interests.replace(" ", "+"))
    response = r.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    anchors = soup.find_all("a")
    nxt_url = "https://paperswithcode.com"
    hrefs = []
    for link in anchors:
        try:
            if "/paper/" in link["href"] and "#code" not in link["href"]:
                if nxt_url + link["href"] not in hrefs:
                    hrefs.append(nxt_url + link["href"])
        except:
            continue

    return hrefs


hrefs = get_url("electromagnetic effect")


def get_paras(hrefs):
    paras_of_paper = []
    for link in hrefs:
        print(link)
        r1 = r.get(link)
        soup = BeautifulSoup(r1.text, "html.parser")
        paras = soup.find_all("p")
        paragraph = [para.text for para in paras]
        paras_of_paper.append(paragraph[-1])
    return paras_of_paper


def send_mail(from_mail, to_mail, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail, password)
    server.sendmail(from_mail, to_mail, message)
    server.quit()


paras = get_paras(hrefs)


def get_paper_pdf_links(hrefs):
    dic = {}
    for i in hrefs:
        url = i
        dict_key = url.split("/")[-1]
        r2 = r.get(url)
        soup = BeautifulSoup(r2.text, "html.parser")
        anchors = soup.find_all("a")
        try:
            anchors = [link["href"] for link in anchors if "pdf" in link["href"]]
            dic[dict_key] = anchors
        except:
            continue
    return dic


def read_db(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    user_data_lst = []
    try:
        cursor.execute("SELECT email, topic FROM database")
        rows = cursor.fetchall()
        for row in rows:
            user_data_lst.append(row)
    except sqlite3.OperationalError as e:
        print("Error: " + str(e))

    cursor.close()
    conn.close()
    return user_data_lst


pdfs = get_paper_pdf_links(hrefs)
# print(pdfs)
send_mail("pundeerutkarsh2001@gmail.com", read_db('C:\\Users\\Utkarsh Pundeer\\Desktop\\desktop\\hack2sharks_solution\\instance\\users.sqlite3')[0][0], "vicodblcxcjuohmc", pdfs['the-impact-of-plasma-instabilities-on-the'][0])
print("\nMail sent successfully...")

# read_db('C:\\Users\\Utkarsh Pundeer\\Desktop\\desktop\\hack2sharks_solution\\instance\\users.sqlite3')
