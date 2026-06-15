class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available

    def get_status_str(self):
        return "Đang bán" if self.is_available else "Ngừng bán"

menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

while True:
    print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    
    choice = input("\nChọn chức năng (1-4): ")

    match choice:
        case '1':
            print("\n--- DANH SÁCH ĐỒ UỐNG ---")
            print(f"{'Mã món':<6} | {'Tên món':<15} | {'Giá bán':<8} | {'Trạng thái'}")
            print("-" * 50)
            for drink in menu:
                print(f"{drink.code:<6} | {drink.name:<15} | {drink.price:<8} | {drink.get_status_str()}")

        case '2':
            code = input("Nhập mã món: ")
            if any(d.code == code for d in menu):
                print("Mã món đã tồn tại trong hệ thống!")
            else:
                name = input("Nhập tên món: ")
                try:
                    price = int(input("Nhập giá bán: "))
                    if price > 0:
                        menu.append(Drink(code, name, price))
                        print(f"Thành công: Đã thêm món {name} vào thực đơn!")
                    else:
                        print("Giá bán không hợp lệ!")
                except ValueError:
                    print("Giá bán phải là số nguyên!")

        case '3':
            code = input("Nhập mã món cần cập nhật: ")
            drink = next((d for d in menu if d.code == code), None)
            if drink:
                drink.toggle_available()
                print(f"\nĐã cập nhật trạng thái món {drink.code}.")
                print(f"Trạng thái hiện tại: {drink.get_status_str()}")
            else:
                print("Không tìm thấy món có mã này!")

        case '4':
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")