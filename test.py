import streamlit as st
import pandas as pd

# يجب أن يكون هذا أول أمر Streamlit في الملف، ويُستدعى مرة واحدة فقط
st.set_page_config(page_title="To Do List", page_icon="🧾", layout="wide")


def initialize_state():
    """ننشئ جدول المهام مرة واحدة فقط لكل جلسة (session)."""
    if "tasks_df" not in st.session_state:
        st.session_state.tasks_df = pd.DataFrame(
            [{"Task": "", "Done?": False}]
        )


def show_header():
    """عرض العنوان وحقل إدخال اسم المستخدم."""
    st.header("To Do List 🧾")

    user_name = st.text_input("👉 من فضلك أدخل اسمك لتخطط ليومك:")
    if user_name:
        st.write(f"أهلاً بك {user_name} 👋")

    st.subheader("خطتك اليوم")


def show_task_editor():
    """
    عرض جدول المهام القابل للتعديل.
    مهم: نمرر st.session_state.tasks_df مباشرة كمصدر البيانات، ونعيد حفظ
    الناتج فيها مباشرة بدون أي مقارنات يدوية معقدة. هذا يمنع مشكلة
    اختفاء المهمة أو الحاجة لكتابتها مرتين.
    """
    edited_df = st.data_editor(
        st.session_state.tasks_df,
        num_rows="dynamic",       # يسمح بإضافة صفوف/مهام جديدة مباشرة
        hide_index=True,
        use_container_width=True,
        key="task_editor",
    )

    st.session_state.tasks_df = edited_df
    return edited_df


def show_progress(edited_df):
    """حساب ونسبة إنجاز المهام المكتملة وعرضها كشريط تقدم."""
    total = len(edited_df)
    completed = edited_df["Done?"].sum() if total > 0 else 0
    progress = completed / total if total > 0 else 0

    st.divider()
    st.progress(
        progress,
        text=f"لقد أنجزت {int(progress * 100)}% من مهامك",
    )


def main():
    initialize_state()
    show_header()
    edited_df = show_task_editor()
    show_progress(edited_df)


if __name__ == "__main__":
    main()
