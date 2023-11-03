import psycopg2

# データベースに接続
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="trareco",
    user="haya",
    password=""
)

# カーソルを作成
cur = conn.cursor()

# テーブル名と列名を指定
table_name = "tourist_area"

# 指定する画像
img = [1, 5, 10, 15, 20]

# クエリを指定
query = f'SELECT * FROM {table_name} WHERE {table_name}.tourist_id = {img[0]} OR {table_name}.tourist_id = {img[1]} OR {table_name}.tourist_id = {img[2]} OR {table_name}.tourist_id = {img[3]} OR {table_name}.tourist_id = {img[4]};'

# SQLクエリを実行
cur.execute(query)

# 結果を取得
result = cur.fetchall()

# 結果を表示
print('選択された画像')
i = 0
for row in result:
    print('選択された画像番号：', img[i])
    print(row)
    i += 1

# カーソルと接続をクローズ
cur.close()
conn.close()
