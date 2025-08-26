import streamlit as st
import pandas as pd
import json
import os

CONFIG_FILE = "config.json"

# Load config into session state if not already present
if 'target_columns' not in st.session_state:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
    else:
        config = {"target_columns": [], "mappings": {}}
    st.session_state.target_columns = config.get("target_columns", [])
    st.session_state.mappings = config.get("mappings", {})

st.title("Data Integration Tool")

st.header("Define Target Columns")
target_input = st.text_area("Enter target column names, one per line", value="\n".join(st.session_state.target_columns))
if st.button("Update Target Columns"):
    st.session_state.target_columns = [line.strip() for line in target_input.split("\n") if line.strip()]

st.header("Upload CSV Files")
uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True, type="csv")

dataframes = {}
columns = {}
for file in uploaded_files or []:
    df = pd.read_csv(file)
    dataframes[file.name] = df
    columns[file.name] = df.columns.tolist()

# Preview section for imported tables with mappings
if dataframes:
    st.header("📋 Data Import & Mapping")
    st.write("Click to expand each file to preview data and configure column mappings:")
    
    mappings = st.session_state.mappings
    
    for filename, df in dataframes.items():
        with st.expander(f"🔍 {filename} ({len(df)} rows, {len(df.columns)} columns)"):
            # Data preview section
            st.subheader("📊 Data Preview")
            st.write(f"**Columns:** {', '.join(df.columns.tolist())}")
            st.dataframe(df.head(10), use_container_width=True)
            if len(df) > 10:
                st.caption(f"Showing first 10 rows of {len(df)} total rows")
            
            # Column mapping section
            st.subheader("🔗 Column Mapping")
            if filename not in mappings:
                mappings[filename] = {}
            
            if st.session_state.target_columns:
                source_cols = ["None"] + columns[filename]
                
                # Create two columns for better layout
                col1, col2 = st.columns(2)
                
                for i, target_col in enumerate(st.session_state.target_columns):
                    selected = mappings[filename].get(target_col, "None")
                    if selected not in source_cols:
                        selected = "None"
                    
                    # Alternate between columns for better layout
                    with col1 if i % 2 == 0 else col2:
                        mapping = st.selectbox(
                            f"Map to **{target_col}**", 
                            source_cols, 
                            index=source_cols.index(selected), 
                            key=f"map_{filename}_{target_col}"
                        )
                        mappings[filename][target_col] = mapping if mapping != "None" else None
            else:
                st.info("⚠️ Please define target columns first to configure mappings.")
    
    st.session_state.mappings = mappings

# Reset mappings button
if dataframes and st.session_state.mappings:
    st.divider()
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔄 Reset All Mappings", type="secondary", use_container_width=True):
            st.session_state.mappings = {}
            st.success("All mappings have been reset!")
            st.rerun()

if st.button("Merge and Export"):
    if st.session_state.target_columns and dataframes:
        merged_df = pd.DataFrame(columns=st.session_state.target_columns)
        for filename, df in dataframes.items():
            mapping = st.session_state.mappings.get(filename, {})
            renamed = {target: df[source] for target, source in mapping.items() if source}
            file_df = pd.DataFrame(renamed)
            for col in st.session_state.target_columns:
                if col not in file_df:
                    file_df[col] = pd.NA
            merged_df = pd.concat([merged_df, file_df], ignore_index=True)
        csv = merged_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download Merged CSV", csv, "merged.csv", "text/csv")
    else:
        st.warning("Define target columns and upload files first.")

if st.button("Save Settings"):
    config = {
        "target_columns": st.session_state.target_columns,
        "mappings": st.session_state.mappings
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)
    st.success("Settings saved!")