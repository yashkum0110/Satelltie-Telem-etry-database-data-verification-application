# Data Matching and Validation System

## Project Overview

This **Data Matching and Validation System** is a full-stack web application developed using **Python (Flask)** designed to enhance data integrity and streamline quality assurance processes. Originally conceived during a Project Traineeship at the U. R. Rao Satellite Centre (URSC) in ISRO's Reliability and Quality Assurance Group (RQSG), this system automates the comparison and validation of diverse user-provided data against a secure, administrative master database.

It addresses the critical need for precise data verification in environments where even minor discrepancies can have significant consequences, such as in aerospace telemetry and engineering data. By leveraging advanced matching algorithms and a scalable architecture, the system significantly reduces manual data checking efforts and improves overall data accuracy.

## Key Features

* **Secure Admin Panel:**
    * Protected by a basic login mechanism for administrative users.
    * Allows secure upload and configuration of a master reference database (Excel/CSV).
    * Enables selection of specific sheets and a "key field" within the database for matching.
* **User Data Upload & Configuration:**
    * Provides an interface for general users to upload their own data files (Excel/CSV).
    * Allows users to select a sheet and specify multiple parameters (columns) for comparison against the configured master database.
* **Automated Data Processing & Validation:**
    * Employs **fuzzy string matching (FuzzyWuzzy)** on the designated key field to intelligently link records between the user's data and the master database, accommodating minor variations.
    * Performs detailed, cell-level comparisons for selected parameters, providing clear "Passed" or "Failed" results.
* **Scalable Data Handling:**
    * Optimized to manage large datasets efficiently by storing processed results as **Parquet** files on the server's file system, avoiding in-memory session limitations.
* **Interactive Results Display:**
    * Presents streamlined validation reports in a clean, interactive web table, showing only the input key, matched reference key, and the comparison results for selected parameters.
    * Includes pagination for easy navigation through large result sets.
* **Data Export Functionality:**
    * Allows users to download the complete processed comparison results in an Excel file for further analysis and record-keeping.

## Technologies Used

* **Backend:**
    * **Python 3.x**: Core programming language.
    * **Flask**: Web framework for building the application.
    * **Pandas**: For robust data manipulation, reading, and writing Excel/CSV and Parquet files.
    * **FuzzyWuzzy**: For fuzzy string matching (record linkage).
    * **openpyxl**: For Excel file reading/writing (used internally by Pandas for `.xlsx`).
* **Frontend:**
    * **HTML5 / CSS3**: For structuring and styling web pages.
    * **Tailwind CSS**: A utility-first CSS framework for rapid and responsive UI development.
    * **Jinja2**: Templating engine for rendering dynamic HTML.
* **Development Environment:**
    * **Visual Studio Code (VS Code)**: Integrated Development Environment (IDE).
    * **SSH Server (Linux Virtual Machine)**: Remote development environment.
