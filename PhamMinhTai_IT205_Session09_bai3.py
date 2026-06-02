# Danh sach don hang ban dau
order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HE THONG QUAN LY DON HANG GRAB EXPRESS =====")
    print("1. Hien thi danh sach don hang")
    print("2. Them don hang moi")
    print("3. Xoa don hang theo ma")
    print("4. Thoat chuong trinh")

    choice = input("Nhap lua chon: ")

    if choice == "1":
        if len(order_list) == 0:
            print("Danh sach don hang hien dang trong.")
        else:
            print("Danh sach don hang hien tai:")
            for i in range(len(order_list)):
                print(i + 1, ".", order_list[i], sep="")

    elif choice == "2":
        order_code = input("Nhap ma don hang moi: ")

        order_code = order_code.strip().upper()

        order_list.append(order_code)

        print("Them don hang thanh cong!")

    elif choice == "3":
        order_code = input("Nhap ma don hang can xoa: ")

        order_code = order_code.strip().upper()

        if order_code in order_list:
            order_list.remove(order_code)
            print("Xoa don hang thanh cong!")
        else:
            print("Khong tim thay ma don hang can xoa!")

    elif choice == "4":
        print("Thoat chuong trinh.")
        break

    else:
        print("Lua chon khong hop le, vui long nhap lai!")