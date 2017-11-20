# Online Shopping Portal - Intrusion Detection System (IDS)

Intrusion Detection System (IDS) is a Full Stack Web Application for monitoring a network for malicious activity or policy violations. Our team used the IDS on an online shopping portal to simulate the malicious activities being queried onto the database using different actions performed on the portal. 

<ul> <em>Actions such as</em>
  <li> Adding/Fetching a product on a shopping cart  - <strong>SELECT</strong> operation on the database </li>
  <li> Removing a product from the shopping cart - <strong>DELETE</strong> operation on the database </li>
  <li> Checking out products from the shopping cart - <strong>INSERT</strong> operation on the database </li>
</ul>

<strong>Flow of Data:</strong>

User -> Presentation Tier (Flask WebUI) -> Application Tier (Python 3) -> IDS -> Persistence Tier (psychopg2 library) -> Data Tier (PostgreSQL)

<strong>Tech Used:</strong> Python (Flask), Jinja2, HTML5, CSS3, Bootstrap 4, jQuery, AJAX, PostgreSQL (PgAdmin4, psychopg2)
