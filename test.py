import streamlit as st


class ToDoApp:
    def __init__(self):
        self.page_title = "To Do List"
        self.page_icon = "🧾"
        self.layout = "wide"

    def configure_page(self):
        # يجب أن يكون هذا أول أمر Streamlit في الملف
        st.set_page_config(
            page_title=self.page_title,
            page_icon=self.page_icon,
            layout=self.layout
        )

    def initialize_state(self):
        """ننشئ قائمة المهام مرة واحدة فقط لكل جلسة (session)."""
        if "tasks" not in st.session_state:
            st.session_state.tasks = []  # كل عنصر: {"task": "...", "done": False}

    def show_header(self):
        """عرض العنوان وحقل إدخال اسم المستخدم."""
        st.header("To Do List 🧾")

        user_name = st.text_input("👉 من فضلك أدخل اسمك لتخطط ليومك:")
        if user_name:
            st.write(f"أهلاً بك {user_name} 👋")

        st.subheader("خطتك اليوم")

    def add_task_form(self):
        """
        نموذج لإضافة مهمة جديدة.
        استخدام st.form مهم جداً هنا لتقليل rerun غير المطلوب.
        """
        with st.form("add_task_form", clear_on_submit=True):
            new_task = st.text_input("اكتب مهمة جديدة:")
            submitted = st.form_submit_button("➕ إضافة المهمة")

            if submitted and new_task.strip():
                st.session_state.tasks.append(
                    {"task": new_task.strip(), "done": False}
                )
                st.rerun()

    def show_tasks(self):
        """عرض المهام الحالية مع checkbox للتحديد و زر حذف."""
        if not st.session_state.tasks:
            st.info("لا توجد مهام بعد، أضيفي أول مهمة من الأعلى 👆")
            return

        for i, item in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([8, 1])

            with col1:
                checked = st.checkbox(
                    item["task"],
                    value=item["done"],
                    key=f"task_{i}"
                )
                st.session_state.tasks[i]["done"] = checked

            with col2:
                if st.button("🗑️", key=f"delete_{i}"):
                    st.session_state.tasks.pop(i)
                    st.rerun()

    def show_progress(self):
        """حساب نسبة إنجاز المهام المكتملة وعرضها كشريط تقدم."""
        total = len(st.session_state.tasks)
        completed = sum(1 for t in st.session_state.tasks if t["done"])
        progress = completed / total if total > 0 else 0

        st.divider()
        st.progress(progress, text=f"لقد أنجزت {int(progress * 100)}% من مهامك")

    def run(self):
        """تشغيل التطبيق."""
        self.configure_page()
        self.initialize_state()
        self.show_header()
        self.add_task_form()
        self.show_tasks()
        self.show_progress()


if __name__ == "__main__":
    ToDoApp().run()
