def decimal_to_binary(n: int, bits: int) -> str:
    """המרת מספר עשרוני לייצוג בינארי בגודל ביטים נתון"""
    if n >= 2 ** bits:
        raise ValueError("המספר גדול מדי עבור גודל הזיכרון הנתון")
    binary = bin(n)[2:]  # הסרת '0b'
    return binary.zfill(bits)


def twos_complement(binary: str) -> str:
    """המרת ייצוג בינארי למשלים ל-2"""
    # שלב 1: היפוך סיביות
    inverted = ''.join('1' if bit == '0' else '0' for bit in binary)

    # שלב 2: הוספת 1
    result = list(inverted)
    carry = 1
    for i in range(len(result) - 1, -1, -1):
        if result[i] == '1' and carry == 1:
            result[i] = '0'
        elif result[i] == '0' and carry == 1:
            result[i] = '1'
            carry = 0
    return ''.join(result)


def main():
    try:
        number = int(input("הכנס מספר עשרוני חיובי: "))
        bits = int(input("הכנס גודל זיכרון (במספר סיביות): "))
        
        if number < 0:
            raise ValueError("יש להזין מספר חיובי בלבד")
        if bits <= 0:
            raise ValueError("גודל הזיכרון חייב להיות מספר חיובי")

        binary = decimal_to_binary(number, bits)
        negative_binary = twos_complement(binary)

        print(f"\nהמספר הבינארי של {number} הוא: {binary}")
        print(f"המשלים ל-2 (ייצוג של -{number}) הוא: {negative_binary}")

    except ValueError as e:
        print(f"שגיאה: {e}")


if __name__ == "__main__":
    main()