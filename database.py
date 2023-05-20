import psycopg2
conn = psycopg2.connect(user="postgres", password="Joselina1979", database="product", host="localhost", port="5432")
print("Successfully connected!")