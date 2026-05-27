hashtag = []

while True:
    print("""
+===============================================+
|        HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK       |
+===============================================+
|   1. Nhập và phân tích thông tin video        |
|   2. Chuẩn hóa tên tài khoản                  |
|   3. Kiểm tra tính hợp lệ của hashtag         |
|   4. Tìm kiếm và thay thế từ khóa trong mô tả |
|   5. Thoát chương trình                       |
+===============================================+
""")
    choice = input("> Mời bạn chọn chức năng (1-5): ")
    print()
    match choice:
        case "1":
            account_name = input("Nhập tên tài khoản: ").strip()
            video_title = input("Nhập tiêu đề video: ").strip().title()
            video_description = input("Nhập mô tả của video: ").strip()
            hashtag_quantity = int(input("Nhập số lượng hashtag muốn thêm: "))
            for i in range(hashtag_quantity):
                hashtag_chid = input(f"Nhập hashtag {i+1}: ").strip()
                hashtag.append(hashtag_chid)
            
            print(f"- Tên tài khoản sau khi loại bỏ khoảng trắng đầu và cuối: {account_name}")
            print(f"- Tiêu đề sau khi loại bỏ khoảng trắng đầu và cuối, viết hoa chữ cái đầu mỗi từ: {video_title}")
            print(f"- Mô tả sau khi loại bỏ khoảng trắng đầu và cuối: {video_description}")
            print(f"- Độ dài mô tả video: {len(video_description)}")
            print(f"- Số lượng từ trong mô tả video: {len(video_description.split(" "))}")
            print(f"- Danh sách hashtag sau khi chuẩn hóa khoảng trắng: {hashtag}")
            print(f"- Số lượng hashtag: {hashtag_quantity}")
            print(f"- Mô tả video được chuyển toàn bộ sang chữ thường: {video_description.lower()}")
            print(f"- Mô tả video được chuyển toàn bộ sang chữ hoa: {video_description.upper()}")

        case "2":
            account_name = input("Nhập tên tài khoản: ").strip()
            new_account_name = account_name.lower()
            new_account_name = "@" + new_account_name
            print(f"- Tên tài khoản ban đầu: {account_name}")
            print(f"- Tên tài khoản sau khi được chuẩn hoá: {new_account_name}")
        case "3":
            input_hashtag = input("Nhập hashtag: ").strip()
            if input_hashtag == "":
                print("Hashtag không được rỗng hoặc không được có khoảng trắng")
            elif input_hashtag.startswith("#") == False:
                print("Hashtag phải bắt đầu bằng ký tự #")
            elif len(input_hashtag) < 2:
                print("Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #")
            else:
                print("Hashtag hợp lệ")
        case "4":
            input_search_description = input("Nhập từ khóa cần tìm: ").strip()
            input_change = input("Từ khóa cần thay đổi: ").strip()
            if input_search_description in video_description:
                video_description = video_description.replace(input_search_description, input_change)
                print(video_description)
            else:
                print("Không tìm thấy từ khóa cần tìm")
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại từ 1 - 5")