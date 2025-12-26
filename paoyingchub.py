"""
เกมเป่ายิ้งชุบ (Rock Paper Scissors) - เวอร์ชันแก้ไขแล้ว
"""
import random


def get_bot_choice():
    """ให้บอทสุ่มเลือก"""
    return random.choice(["rock", "scissors", "paper"])


def determine_winner(user, bot):
    """ตรวจสอบผู้ชนะ"""
    if user == bot:
        return "draw"

    # ผู้เล่นชนะ - แก้จาก computer เป็น bot
    if (user == "rock" and bot == "scissors" or
            user == "scissors" and bot == "paper" or
            user == "paper" and bot == "rock"):
        return "user_wins"

    # บอทชนะ
    return "bot_wins"


def play_game():
    """ฟังก์ชันหลักของเกม"""
    score = 0

    print("=" * 50)
    print("🎮 ยินดีต้อนรับสู่เกมเป่ายิ้งชุบ!")
    print("=" * 50)

    while True:
        print("\n--- รอบใหม่ ---")
        user_hand = input("เลือกมือของคุณ (rock/scissors/paper) หรือ 'x' เพื่อออก: ").lower().strip()

        # ออกเกม
        if user_hand in ("x", "exit"):
            print(f"\n🏆 คะแนนสุดท้ายของคุณ: {score}")
            print("ขอบคุณที่เล่นเกม! 👋")
            break

        # ตรวจสอบ Input ถูกต้องหรือไม่
        if user_hand not in ("rock", "scissors", "paper"):
            print("❌ กรุณาเลือก rock, scissors หรือ paper เท่านั้น!")
            continue

        bot_hand = get_bot_choice()
        result = determine_winner(user_hand, bot_hand)

        print(f"\n👤 คุณ: {user_hand}")
        print(f"🤖 บอท: {bot_hand}")

        if result == "draw":
            print("🤝 เสมอ!")
        elif result == "user_wins":
            score += 1
            print(f"✅ คุณชนะ! 🎉 คะแนน: {score}")
        else:
            print(f"❌ คุณแพ้! คะแนน: {score}")


if __name__ == "__main__":
    play_game()
