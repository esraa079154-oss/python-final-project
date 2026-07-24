import streamlit as st
import pandas as pd

# يجب أن يكون هذا أول أمر Streamlit في الملف، ويُستدعى مرة واحدة فقط
st.set_page_config(page_title="To Do List", page_icon="🧾", layout="wide")


def initialize_state():
    """ننشئ قائمة المهام مرة واحدة فقط لكل جلسة (session)."""
    if "tasks" not in st.session_state:
        st.session_state.tasks = []  # كل عنصر: {"task": "...", "done": False}


def show_header():
    """عرض العنوان وحقل إدخال اسم المستخدم."""
    st.header("To Do List 🧾")

    user_name = st.text_input("👉 من فضلك أدخل اسمك لتخطط ليومك:")
    if user_name:
        st.write(f"أهلاً بك {user_name} 👋")

    st.subheader("خطتك اليوم")


def add_task_form():
    """
    نموذج لإضافة مهمة جديدة.
    استخدام st.form مهم جداً هنا: التطبيق ما يعيد التحميل (rerun) إلا
    لما تضغطي زر "إضافة المهمة"، فما تنمسح المهمة ولا تحتاجي تكتبيها
    مرتين، لأن الكتابة نفسها ما تسبب rerun فوري.
    """
    with st.form("add_task_form", clear_on_submit=True):
        new_task = st.text_input("اكتب مهمة جديدة:")
        submitted = st.form_submit_button("➕ إضافة المهمة")

        if submitted and new_task.strip():
            st.session_state.tasks.append({"task": new_task.strip(), "done": False})
            st.rerun()


def show_tasks():
    """عرض المهام الحالية مع خانة اختيار لتحديد المهام المنجزة، وزر حذف لكل مهمة."""
    if not st.session_state.tasks:
        st.info("لا توجد مهام بعد، أضيفي أول مهمة من الأعلى 👆")
        return

    for i, item in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([8, 1])
        with col1:
            checked = st.checkbox(item["task"], value=item["done"], key=f"task_{i}")
            st.session_state.tasks[i]["done"] = checked
        with col2:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()


def show_progress():
    """حساب نسبة إنجاز المهام المكتملة وعرضها كشريط تقدم."""
    total = len(st.session_state.tasks)
    completed = sum(1 for t in st.session_state.tasks if t["done"])
    progress = completed / total if total > 0 else 0

    st.divider()
    st.progress(
        progress,
        text=f"لقد أنجزت {int(progress * 100)}% من مهامك",
    )


def main():
    initialize_state()
    show_header()
    add_task_form()
    show_tasks()
    show_progress()


if __name__ == "__main__":
    main()
    
