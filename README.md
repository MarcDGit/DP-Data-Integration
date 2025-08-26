# DP Data Integration Tool

A Streamlit-based web application for integrating and merging CSV data from multiple sources with customizable column mappings.

## 🚀 Features

- **Multi-file CSV Upload**: Upload multiple CSV files simultaneously
- **Interactive Table Preview**: Collapsible preview of imported data with row/column counts
- **Flexible Column Mapping**: Map source columns to target schema with intuitive dropdowns
- **Data Merging**: Combine data from multiple sources into a unified format
- **Configuration Persistence**: Save and load column mappings and target schema
- **Export Functionality**: Download merged data as CSV

## 📋 Requirements

- Python 3.7+
- Streamlit
- Pandas

## 🛠️ Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd DP-Data-Integration
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 Usage

1. **Start the application**:
```bash
streamlit run app.py
```

2. **Define Target Columns**:
   - Enter your desired column names (one per line)
   - These will be the columns in your final merged dataset

3. **Upload CSV Files**:
   - Use the file uploader to select multiple CSV files
   - Preview your data using the collapsible table preview section

4. **Map Columns**:
   - For each uploaded file, map source columns to your target columns
   - Use "None" to skip columns you don't need

5. **Merge and Export**:
   - Click "Merge and Export" to combine all data
   - Download the merged CSV file

6. **Save Settings** (Optional):
   - Save your column mappings and target schema for future use

**💡 Pro Tips:**
- You can leave some mappings as "None" if you don't need certain columns
- The preview shows you the first 10 rows - perfect for checking if your data looks right
- Your settings are saved automatically, so you can use the same setup again

## 📊 Sample Data

The repository includes sample CSV files demonstrating different data formats:

- `smpl_oracle_sales.csv` - Oracle system sales data
- `smpl_m3_sales.csv` - M3 system sales data  
- `smpl_SAP_sales.csv` - SAP system sales data

Each file has different column names but similar data structure, perfect for testing the integration capabilities.

## 🔧 Configuration

The application automatically saves your settings in `config.json`, including:
- Target column definitions
- Column mappings for each data source

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 🆘 Support

For issues or questions, please create an issue in the repository or contact me.
