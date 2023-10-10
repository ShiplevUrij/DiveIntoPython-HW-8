from pack import file

JSON_FILENAME = "info.json"
CSV_FILENAME = "info.csv"
PICK_FILENAME = "info.pcl"

if __name__ == '__main__':
    print("Информация о каталоге: ")
    dir_info = file.dir_info()  
    print(dir_info)
    print("Сохранение информации в файлы")
    file.save_to_json(dir_info, JSON_FILENAME)
    file.save_to_picle(dir_info, PICK_FILENAME)
    file.save_to_csv(dir_info, CSV_FILENAME)

    print(f"Информация в файлах: {JSON_FILENAME}, {CSV_FILENAME}, {PICK_FILENAME}")