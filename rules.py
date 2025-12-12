# rules.py
"""
قائمة القواعد بصيغة يمكن ل inference.py استدعاؤها.
كل قاعدة هي دالة بسيطة تأخذ facts (قاموس) وتُرجع True لو القاعدة تنطبق.
نستخدم دوال بدل نصوص عشان نقدر نعطي قواعد أكثر تعقيدًا لاحقًا.
"""

def rule_fan_problem(f):
    # مروحة: سخونة + صوت عالي
    return f.get("heating") and f.get("noise")

def rule_fan_problem_alt(f):
    # مروحة بديل: سخونة مع بطء (قد تكون المروحة غير فعّالة)
    return f.get("heating") and f.get("slow")

def rule_ram_fault(f):
    # رام: تهنيج متكرر + بطء
    return f.get("freeze") and f.get("slow")

def rule_ssd_issue(f):
    # SSD: بطء بدون سخونة أو صوت (قد يكون تخزين بطيء)
    return f.get("slow") and (not f.get("noise")) and (not f.get("heating"))

def rule_battery_problem(f):
    # بطارية/شاحن: البطارية تنفذ بسرعة أو الجهاز يفصل عند فصل الشاحن
    return f.get("battery_drop")

def rule_display_gpu(f):
    # شاشة/كرت شاشة: مشاكل في العرض
    return f.get("screen_issue")

# قائمة القواعد مع اسم العطل المطابق (أولوية يمكن تعديلها في inference)
RULES = [
    ("Display/GPU Problem", rule_display_gpu),
    ("Fan Problem", rule_fan_problem),
    ("Fan Problem", rule_fan_problem_alt),
    ("RAM Fault", rule_ram_fault),
    ("SSD Issue", rule_ssd_issue),
    ("Battery/Charger Problem", rule_battery_problem),
]
