# inference.py
from rules import RULES

def diagnose(facts):
    """
    محرك استنتاج بسيط يعتمد على قائمة RULES:
    - يفحص كل قاعدة حسب ترتيبها (الأولوية).
    - يرجع اسم العطل الأول اللي تطابق القاعدة.
    - لو مفيش تطابق يرجع "No Clear Issue Detected".
    """
    matches = []

    for fault_name, rule_func in RULES:
        try:
            if rule_func(facts):
                matches.append(fault_name)
        except Exception:
            # لو قاعدة فيها خطأ، نتجاهلها لكن نسجل أو نعدل لاحقًا
            continue

    if not matches:
        return "No Clear Issue Detected"

    # نرجع أول نتيجة حسب أولوية RULES (أقوى نتيجة)
    return matches[0]

# دالة مساعدة لاختبار الوحدات
if __name__ == "__main__":
    sample = {
        "heating": True,
        "noise": True,
        "battery_drop": False,
        "screen_issue": False,
        "slow": False,
        "freeze": False
    }
    print("Diagnosis:", diagnose(sample))
