# app.py
import streamlit as st
from inference import diagnose
from solutions import SOLUTIONS

st.set_page_config(page_title="Laptop Fault Diagnosis", layout="centered")
st.title("نظام خبير لتشخيص أعطال اللابتوب")
st.write("جاوبي على الأسئلة التالية عشان نساعدك نعرف العطل المحتمل ونقدملك خطوات للحل وفيديو شرح.")

# ===== جمع الحقائق (Facts) =====
heating = st.radio("هل الجهاز بيحس بسخونة عالية؟", ("لا", "نعم")) == "نعم"
noise = st.radio("هل في صوت غريب (مثل طرقات أو صوت المروحة عالي)؟", ("لا", "نعم")) == "نعم"
battery_drop = st.radio("هل البطارية بتنقص بسرعة أو الجهاز يفصل لما تشيله من الشاحن؟", ("لا", "نعم")) == "نعم"
screen_issue = st.radio("هل الشاشة بتفصل أو تظهر خطوط/تهتز؟", ("لا", "نعم")) == "نعم"
slow = st.radio("هل الجهاز بطيء جداً مقارنة بالمعتاد؟", ("لا", "نعم")) == "نعم"
freeze = st.radio("هل الجهاز بيهنج أو يعمل Restart مفاجئ؟", ("لا", "نعم")) == "نعم"

facts = {
    "heating": heating,
    "noise": noise,
    "battery_drop": battery_drop,
    "screen_issue": screen_issue,
    "slow": slow,
    "freeze": freeze
}

st.write("---")

# ===== زر التشخيص =====
if st.button("شخّص الجهاز"):
    result = diagnose(facts)
    st.subheader("التشخيص المتوقع:")
    st.write("➡️", result)

    sol = SOLUTIONS.get(result)
    if sol:
        st.write("**نصائح سريعة:**")
        for tip in sol["tips"]:
            st.write("- " + tip)

        st.write("")
        st.write("**فيديو شرح مقترح:**")
        # نعرض الرابط قابل للنقر
        st.markdown(f"[افتح فيديو الشرح]({sol['video']})")
        st.write("")
        st.info("لو الرابط لم يفتح تلقائيًا، انسخي الرابط وافتحيه في متصفح.")
    else:
        st.write("لا توجد حلول مسجلة لهذا النتيجة بعد. حاولي تزويدنا بمعلومات أدق.")
