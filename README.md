# TradeDog
Securing investment banking trades with real-time anomaly detection.

## Project Description
TradeDog is designed to monitor and secure the trade cycle of investment banking products such as FX, Equity, and Fixed Income. Utilizing Python and Bash, the system collects, processes, and analyzes trade data to identify anomalies and potential security breaches in real-time.

## Key Objectives
1. **Understand the Trade Cycle:** Gain in-depth knowledge of the trade cycle for various investment banking products.
2. **Data Collection and Processing:** Use Bash scripts to automate the collection and preprocessing of trade data.
3. **Anomaly Detection:** Implement Python-based statistical methods to detect anomalies and potential security issues in trade data.
4. **Security Alerts and Reports:** Generate alerts and comprehensive reports on detected anomalies.
5. **Integration and Automation:** Integrate the system into a continuous monitoring framework.

## Project Components

### 1. Trade Data Simulation (Bash & Python)
- **Bash Script:** Create a Bash script to simulate the generation of trade data for FX, Equity, and Fixed Income products.
- **Python Script:** Develop a Python script to inject anomalies into the simulated trade data for testing purposes.

### 2. Data Collection and Preprocessing (Bash)
- Automate the collection of trade data from different sources.
- Use Bash scripts to clean and preprocess the collected data.

### 3. Anomaly Detection Module (Python)
- **Data Analysis:** Use Python libraries like Pandas and NumPy for data analysis.
- **Statistical Methods:** Apply statistical methods such as z-score, IQR (Interquartile Range), and moving averages to detect anomalies in trade data.

### 4. Security Alerts and Reporting (Python)
- Generate real-time alerts for detected anomalies using Python.
- Create detailed reports on trade anomalies, including potential security breaches and unusual trade patterns.
- Use libraries like Matplotlib or Seaborn to visualize trade data and anomalies.

### 5. Integration and Continuous Monitoring (Bash & Python)
- Integrate the anomaly detection module into a continuous monitoring framework.
- Develop Bash scripts to automate the end-to-end process, from data collection to reporting.

## Technologies and Tools
- **Programming Languages:** Python, Bash
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Tools:** cron (for scheduling scripts), syslog (for logging alerts), Jupyter Notebook (for development and testing)

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

