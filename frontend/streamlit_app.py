import os
import requests
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="CRUD Customers", layout="centered")
st.title("📇 CRUD Customers (Streamlit + FastAPI)")

# ----------------------------
# Helpers
# ----------------------------
def api_get(path, **kwargs):
    r = requests.get(f"{API_URL}{path}", timeout=10, **kwargs)
    if r.status_code >= 400:
        st.error(f"Erro {r.status_code}: {r.text}")
        return None
    return r.json()

def api_post(path, json):
    r = requests.post(f"{API_URL}{path}", json=json, timeout=10)
    if r.status_code >= 400:
        st.error(f"Erro {r.status_code}: {r.text}")
        return None
    return r.json()

def api_put(path, json):
    r = requests.put(f"{API_URL}{path}", json=json, timeout=10)
    if r.status_code >= 400:
        st.error(f"Erro {r.status_code}: {r.text}")
        return None
    return r.json()

def api_delete(path):
    r = requests.delete(f"{API_URL}{path}", timeout=10)
    if r.status_code >= 400:
        st.error(f"Erro {r.status_code}: {r.text}")
        return False
    return True

# ----------------------------
# Tabs
# ----------------------------
tab_list, tab_create, tab_edit_delete = st.tabs(["📋 Listar", "➕ Criar", "✏️ Editar/🗑️ Deletar"])

with tab_list:
    st.subheader("Clientes cadastrados")
    customers = api_get("/customers")
    if customers is not None:
        st.dataframe(customers, use_container_width=True)

with tab_create:
    st.subheader("Criar novo cliente")
    name = st.text_input("Nome")
    email = st.text_input("Email")

    if st.button("Criar"):
        if not name or not email:
            st.warning("Preencha nome e email.")
        else:
            created = api_post("/customers", {"name": name, "email": email})
            if created:
                st.success(f"Cliente criado com ID {created['id']}")
                st.rerun()

with tab_edit_delete:
    st.subheader("Editar ou deletar cliente")

    customers = api_get("/customers")
    if customers:
        ids = [c["id"] for c in customers]
        selected_id = st.selectbox("Selecione o ID do cliente", ids)

        selected = next((c for c in customers if c["id"] == selected_id), None)
        if selected:
            new_name = st.text_input("Nome", value=selected["name"])
            new_email = st.text_input("Email", value=selected["email"])

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Salvar alterações"):
                    payload = {"name": new_name, "email": new_email}
                    updated = api_put(f"/customers/{selected_id}", payload)
                    if updated:
                        st.success("Atualizado com sucesso!")
                        st.rerun()

            with col2:
                if st.button("Deletar", type="primary"):
                    ok = api_delete(f"/customers/{selected_id}")
                    if ok:
                        st.success("Deletado com sucesso!")
                        st.rerun()