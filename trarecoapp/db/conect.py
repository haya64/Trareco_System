import psycopg2

class SELECTDATA():
    def select(self, columns, table, where=None):
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

        # クエリを指定
        if where is not None:
            query = f'SELECT {columns} FROM {table} WHERE {where}'
        else:
            query = f'SELECT {columns} FROM {table} '

        # SQLクエリを実行
        cur.execute(query)

        # 結果を取得
        result = cur.fetchall()

        # # 結果を表示
        # print('テーブル一覧')
        # for row in result:
        #     print(row)

        # カーソルと接続をクローズ
        cur.close()
        conn.close()

        return result
