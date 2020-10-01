from db.run_sql import run_sql
from models.biting import Biting

def save(biting):
    sql = "INSERT INTO bitings (human_id, zombie_id) VALUES (%s,%s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    biting.id = id

def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    result = run_sql(sql)
    for row in results:
        biting = Biting(row["human_id"], row["zombie_id"], row["id"])
        bitings.append(biting)
    return bitings