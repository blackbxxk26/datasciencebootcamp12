"""
ดึงข้อมูลราคาน้ำมัน Bangchak จาก API
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


def get_bangchak_oil_prices():
    """ดึงข้อมูลราคาน้ำมันจาก Bangchak"""
    
    url = "https://www.bangchak.co.th/th/oilprice/historical"
    
    print("🔄 กำลังดึงข้อมูลราคาน้ำมันจาก Bangchak...")
    
    try:
        # ส่ง request ไปยังเว็บไซต์
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # หาตาราง
        table = soup.find('table', class_='table--historical-oilprice')
        
        if not table:
            print("❌ ไม่พบตารางข้อมูล")
            return None
        
        # ดึงข้อมูลจากตาราง
        data = []
        rows = table.find('tbody').find_all('tr')
        
        for row in rows:
            cols = row.find_all(['th', 'td'])
            row_data = [col.text.strip() for col in cols]
            data.append(row_data)
        
        # สร้าง DataFrame
        columns = [
            'วันที่',
            'Hi Premium Diesel S',
            'Hi Diesel S',
            'Hi Premium 97 Gasohol 95',
            'Gasohol E85 S EVO',
            'Gasohol E20 S EVO',
            'Gasohol 91 S EVO',
            'Gasohol 95 S EVO'
        ]
        
        df = pd.DataFrame(data, columns=columns)
        
        # แปลงราคาเป็นตัวเลข
        for col in columns[1:]:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        print("✅ ดึงข้อมูลสำเร็จ!\n")
        
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
        return None
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        return None


def display_latest_prices(df):
    """แสดงราคาน้ำมันล่าสุด"""
    if df is None or df.empty:
        print("ไม่มีข้อมูลให้แสดง")
        return
    
    print("="*80)
    print("📊 ราคาน้ำมัน Bangchak ล่าสุด")
    print("="*80)
    
    latest = df.iloc[0]
    print(f"\nวันที่: {latest['วันที่']}\n")
    
    fuel_types = [
        ('Hi Premium Diesel S', '🚛'),
        ('Hi Diesel S', '🚗'),
        ('Hi Premium 97 Gasohol 95', '⛽'),
        ('Gasohol E85 S EVO', '🌿'),
        ('Gasohol E20 S EVO', '🌿'),
        ('Gasohol 91 S EVO', '⛽'),
        ('Gasohol 95 S EVO', '⛽')
    ]
    
    for fuel, icon in fuel_types:
        price = latest[fuel]
        if pd.notna(price):
            print(f"{icon} {fuel:30s} : {price:6.2f} บาท/ลิตร")
    
    print("="*80 + "\n")


def save_to_csv(df, filename='bangchak_oil_prices.csv'):
    """บันทึกข้อมูลลง CSV"""
    if df is None or df.empty:
        print("ไม่มีข้อมูลให้บันทึก")
        return
    
    try:
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"✅ บันทึกข้อมูลลงไฟล์ '{filename}' สำเร็จ\n")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")


def compare_prices(df):
    """เปรียบเทียบราคาน้ำมันระหว่างวันล่าสุดกับวันก่อนหน้า"""
    if df is None or len(df) < 2:
        print("ข้อมูลไม่เพียงพอสำหรับการเปรียบเทียบ")
        return
    
    print("="*80)
    print("📈 การเปรียบเทียบราคา (ล่าสุด vs ก่อนหน้า)")
    print("="*80)
    
    latest = df.iloc[0]
    previous = df.iloc[1]
    
    print(f"\nวันที่ล่าสุด: {latest['วันที่']}")
    print(f"วันก่อนหน้า: {previous['วันที่']}\n")
    
    fuel_columns = df.columns[1:]
    
    for fuel in fuel_columns:
        latest_price = latest[fuel]
        previous_price = previous[fuel]
        
        if pd.notna(latest_price) and pd.notna(previous_price):
            diff = latest_price - previous_price
            
            if diff > 0:
                symbol = "📈 ↑"
                color = "เพิ่มขึ้น"
            elif diff < 0:
                symbol = "📉 ↓"
                color = "ลดลง"
            else:
                symbol = "➡️ ="
                color = "ไม่เปลี่ยนแปลง"
            
            print(f"{symbol} {fuel:30s} : {latest_price:6.2f} บาท ({color} {abs(diff):.2f} บาท)")
    
    print("="*80 + "\n")


# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    # ดึงข้อมูล
    df = get_bangchak_oil_prices()
    
    if df is not None:
        # แสดงราคาล่าสุด
        display_latest_prices(df)
        
        # เปรียบเทียบราคา
        compare_prices(df)
        
        # แสดงตารางข้อมูล 5 วันล่าสุด
        print("📋 ตารางราคา 5 วันล่าสุด:")
        print(df.head().to_string(index=False))
        print()
        
        # บันทึกลง CSV
        save_to_csv(df)
