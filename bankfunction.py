class KBank:
    """ระบบแอปพลิเคชันธนาคารกสิกร (K-PLUS)"""
    
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []
    
    def __str__(self):
        return f"บัญชี {self.account_name} ({self.account_number}) มียอดเงิน {self.balance:,.2f} บาท"
    
    def check_balance(self):
        """ตรวจสอบยอดเงินคงเหลือ"""
        print(f"\n{'='*50}")
        print(f"ยอดเงินคงเหลือ: {self.balance:,.2f} บาท")
        print(f"{'='*50}\n")
        return self.balance
    
    def deposit(self, amount):
        """ฝากเงิน"""
        if amount <= 0:
            print("❌ จำนวนเงินไม่ถูกต้อง กรุณาระบุจำนวนที่มากกว่า 0")
            return False
        
        self.balance += amount
        self.transaction_history.append(f"ฝากเงิน +{amount:,.2f} บาท")
        print(f"✅ ฝากเงิน {amount:,.2f} บาท สำเร็จ")
        print(f"ยอดเงินคงเหลือ: {self.balance:,.2f} บาท\n")
        return True
    
    def withdraw(self, amount):
        """ถอนเงิน"""
        if amount <= 0:
            print("❌ จำนวนเงินไม่ถูกต้อง")
            return False
        
        if amount > self.balance:
            print(f"❌ ยอดเงินไม่เพียงพอ (คงเหลือ {self.balance:,.2f} บาท)\n")
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"ถอนเงิน -{amount:,.2f} บาท")
        print(f"✅ ถอนเงิน {amount:,.2f} บาท สำเร็จ")
        print(f"ยอดเงินคงเหลือ: {self.balance:,.2f} บาท\n")
        return True
    
    def transfer(self, amount, recipient_account, recipient_name):
        """โอนเงิน"""
        if amount <= 0:
            print("❌ จำนวนเงินไม่ถูกต้อง")
            return False
        
        if amount > self.balance:
            print(f"❌ ยอดเงินไม่เพียงพอสำหรับการโอน (คงเหลือ {self.balance:,.2f} บาท)\n")
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"โอนเงิน -{amount:,.2f} บาท ไปยัง {recipient_name}")
        print(f"✅ โอนเงิน {amount:,.2f} บาท")
        print(f"ไปยัง: {recipient_name} ({recipient_account})")
        print(f"ยอดเงินคงเหลือ: {self.balance:,.2f} บาท\n")
        return True
    
    def pay_bill(self, bill_type, amount, ref_number):
        """จ่ายบิล (ค่าไฟ ค่าน้ำ ค่าโทรศัพท์ ฯลฯ)"""
        if amount <= 0:
            print("❌ จำนวนเงินไม่ถูกต้อง")
            return False
        
        if amount > self.balance:
            print(f"❌ ยอดเงินไม่เพียงพอสำหรับการชำระบิล (คงเหลือ {self.balance:,.2f} บาท)\n")
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"ชำระบิล{bill_type} -{amount:,.2f} บาท")
        print(f"✅ ชำระบิล{bill_type} จำนวน {amount:,.2f} บาท")
        print(f"เลขที่อ้างอิง: {ref_number}")
        print(f"ยอดเงินคงเหลือ: {self.balance:,.2f} บาท\n")
        return True
    
    def topup_phone(self, phone_number, amount):
        """เติมเงินโทรศัพท์"""
        if amount not in [10, 20, 50, 100, 300, 500]:
            print("❌ จำนวนเงินไม่ถูกต้อง (เลือกได้: 10, 20, 50, 100, 300, 500 บาท)")
            return False
        
        if amount > self.balance:
            print(f"❌ ยอดเงินไม่เพียงพอสำหรับการเติมเงิน (คงเหลือ {self.balance:,.2f} บาท)\n")
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"เติมเงินโทรศัพท์ -{amount:,.2f} บาท")
        print(f"✅ เติมเงินโทรศัพท์ {phone_number}")
        print(f"จำนวน {amount:,.2f} บาท สำเร็จ")
        print(f"ยอดเงินคงเหลือ: {self.balance:,.2f} บาท\n")
        return True
    
    def show_transaction_history(self, limit=10):
        """แสดงประวัติการทำรายการ"""
        print(f"\n{'='*50}")
        print(f"ประวัติการทำรายการ (ล่าสุด {limit} รายการ)")
        print(f"{'='*50}")
        
        if not self.transaction_history:
            print("ยังไม่มีประวัติการทำรายการ")
        else:
            recent_transactions = self.transaction_history[-limit:]
            for i, transaction in enumerate(reversed(recent_transactions), 1):
                print(f"{i}. {transaction}")
        
        print(f"{'='*50}\n")


def show_menu():
    """แสดงเมนูหลัก"""
    print("\n" + "="*50)
    print("🏦 K-PLUS - ธนาคารกสิกรไทย")
    print("="*50)
    print("1. ตรวจสอบยอดเงิน")
    print("2. ฝากเงิน")
    print("3. ถอนเงิน")
    print("4. โอนเงิน")
    print("5. จ่ายบิล")
    print("6. เติมเงินโทรศัพท์")
    print("7. ดูประวัติการทำรายการ")
    print("0. ออกจากระบบ")
    print("="*50)


def main():
    """ฟังก์ชันหลักสำหรับรันโปรแกรม"""
    print("\n🏦 ยินดีต้อนรับสู่ K-PLUS")
    print("="*50)
    
    # สร้างบัญชี
    account_name = input("ชื่อ-นามสกุล: ")
    account_number = input("เลขที่บัญชี (เช่น 123-4-56789-0): ")
    
    while True:
        try:
            initial_balance = float(input("ยอดเงินเริ่มต้น (บาท): "))
            if initial_balance < 0:
                print("❌ ยอดเงินต้องไม่ติดลบ")
                continue
            break
        except ValueError:
            print("❌ กรุณาใส่ตัวเลขเท่านั้น")
    
    my_account = KBank(account_name, account_number, initial_balance)
    print(f"\n✅ สร้างบัญชีสำเร็จ!")
    print(my_account)
    
    # เมนูหลัก
    while True:
        show_menu()
        choice = input("เลือกรายการ (0-7): ").strip()
        
        if choice == "1":
            # ตรวจสอบยอดเงิน
            my_account.check_balance()
            
        elif choice == "2":
            # ฝากเงิน
            try:
                amount = float(input("จำนวนเงินที่ต้องการฝาก (บาท): "))
                my_account.deposit(amount)
            except ValueError:
                print("❌ กรุณาใส่ตัวเลขเท่านั้น\n")
                
        elif choice == "3":
            # ถอนเงิน
            try:
                amount = float(input("จำนวนเงินที่ต้องการถอน (บาท): "))
                my_account.withdraw(amount)
            except ValueError:
                print("❌ กรุณาใส่ตัวเลขเท่านั้น\n")
                
        elif choice == "4":
            # โอนเงิน
            try:
                amount = float(input("จำนวนเงินที่ต้องการโอน (บาท): "))
                recipient_account = input("เลขที่บัญชีผู้รับ: ")
                recipient_name = input("ชื่อผู้รับ: ")
                my_account.transfer(amount, recipient_account, recipient_name)
            except ValueError:
                print("❌ กรุณาใส่ตัวเลขเท่านั้น\n")
                
        elif choice == "5":
            # จ่ายบิล
            try:
                print("\nประเภทบิล: ค่าไฟฟ้า, ค่าน้ำ, ค่าโทรศัพท์, ค่าอินเทอร์เน็ต, ฯลฯ")
                bill_type = input("ประเภทบิล: ")
                amount = float(input("จำนวนเงิน (บาท): "))
                ref_number = input("เลขที่อ้างอิง: ")
                my_account.pay_bill(bill_type, amount, ref_number)
            except ValueError:
                print("❌ กรุณาใส่ตัวเลขเท่านั้น\n")
                
        elif choice == "6":
            # เติมเงินโทรศัพท์
            try:
                phone_number = input("หมายเลขโทรศัพท์: ")
                print("จำนวนเงิน: 10, 20, 50, 100, 300, 500 บาท")
                amount = float(input("เลือกจำนวนเงิน: "))
                my_account.topup_phone(phone_number, amount)
            except ValueError:
                print("❌ กรุณาใส่ตัวเลขเท่านั้น\n")
                
        elif choice == "7":
            # ดูประวัติ
            my_account.show_transaction_history()
            
        elif choice == "0":
            # ออกจากระบบ
            print("\n" + "="*50)
            print("ขอบคุณที่ใช้บริการ K-PLUS")
            print(f"สรุป: {my_account}")
            print("="*50 + "\n")
            break
            
        else:
            print("❌ กรุณาเลือกรายการ 0-7 เท่านั้น\n")
        
        input("กด Enter เพื่อดำเนินการต่อ...")


# รันโปรแกรม
if __name__ == "__main__":
    main()
