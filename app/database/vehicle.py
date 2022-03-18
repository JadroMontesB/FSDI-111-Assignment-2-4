from app.database import get_db

def output_formatter(results):
    out = []
    for result in results:
        res_dict = {
            
            "id": result[0],
            "color": result[1],
            "license_plate": result[2],
            "vehicle_type": result[3],
            "user_id": result[4],
            "active": result[5]

        }
        out.append(res_dict)      
    return out

def insert(vehicle_dict):
    value_tuple = (
        vehicle_dict["color"],
        vehicle_dict["license_plate"],
        vehicle_dict["vehicle_type"],
    )

    stmt = """
        INSERT INTO user (
            color,
            license_plate,
            vehicle_type
        ) VALUES (?, ?, ?)
    """
    cursor = get_db()
    last_row_id = cursor.execute(stmt, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE active=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_user_id(uid):
    cursor = get_db().execute(
        "SELECT * FROM vehicle WHERE id=?", (uid, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data["color"],
        vehicle_data["license_plata"],
        vehicle_data["vehicle_type"],
        pk
    )
    stmt = """
        UPDATE user
        SET color=?,
        license_plata=?,
        vehicle=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(stmt, value_tuple)
    cursor.commit()
