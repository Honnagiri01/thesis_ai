import streamlit as st

st.set_page_config(page_title='Thesis AI', page_icon='📚', layout='wide')

st.title('📚 Thesis AI')
st.write('Upload multiple research papers or theses and generate one combined report.')

uploaded_files = st.file_uploader('Upload PDF files', type=['pdf'], accept_multiple_files=True)

if uploaded_files:
    st.success(f'{len(uploaded_files)} PDF(s) uploaded successfully.')
    if st.button('Start Processing'):
        progress = st.progress(0)
        for i, f in enumerate(uploaded_files):
            st.write(f'Processing {f.name}...')
            progress.progress((i+1)/len(uploaded_files))
        st.success('Processing complete.')
        st.button('Generate Final Report')