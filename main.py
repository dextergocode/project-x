import sqlite3
from passporteye import read_mrz

def process_images(image_paths):
    for image_path in image_paths:
        mrz = read_mrz(image_path)
        if mrz:
            passport_data = {
                "country": mrz.country,
                "surname": mrz.surname,
                "names": " ".join(mrz.names),
                "passport_number": mrz.number,
                "nationality": mrz.nationality,
                "date_of_birth": mrz.date_of_birth,
                "sex": mrz.sex,
                "expiration_date": mrz.expiration_date
            }
            insert_into_policy_db(passport_data)

if __name__ == "__main__":
    setup_databases()
    image_paths = ["./Selected/temp_image.png"]  # Add your image paths here
    process_images(image_paths)
