# PRTR transfers

<p align="center">
  <img src=https://github.com/jodhernandezbe/PRTR_transfers/blob/data-driven/logo.svg width="50%">
</p>

<hr/>

## 1. Overview

### 1.1. Project tree

The following is the project tree considering only its most important files for a developer. Don't hesitate to fully check the folders, including the [ancillary](https://github.com/jodhernandezbe/PRTR_transfers/tree/master/ancillary) one that contains important information for the data processing.  

```bash

PRTR_transfers
├── ancillary
|
├── data_driven
│   ├── data_preparation
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── initial_preprocessing.py
│   │   ├── mlsmote.py
│   │   ├── opening_dataset.py
│   │   ├── rdkit_descriptors.py
│   │   ├── preprocessing.py
│   │   ├── input
│   │   └── output
│   │
│   └── modeling
│       ├── scripts
|       |   ├── __init__.py
|       |   ├── ancillary.py
|       |   ├── evaluation.py
|       |   ├── metrics.py
|       |   ├── models.py
│       |   └── tuning.py
│       |
│       ├── notebooks
|       |   ├── multi-class_classification
|       |   ├── multi-label_classification
│       |   └── multi-model_binary_classification
│       |
│       ├── input
│       └── output
│    
└── data_engineering
    └── load
        └── output

```

### 1.2. Enhanced entity-relationship diagram (EERD) for the PRTR_transfers database 

The EERD model in the following figure represents the PRTR_transfers database schema created after data engineering. The prtr_system table is shown without any explicit relationship between the other tables in the database. The reason is that the columns of the prtr_system table were not set as foreign key; however, its columns could be used to connect to other tables like the national_substance table to know the PRTR system the report comes from. 

<p align="center">
  <img src=https://github.com/jodhernandezbe/PRTR_transfers/blob/data-engineering/data_engineering/load/PRTR_transfers_EER_Diagram.svg width="100%">
</p>

<hr/>

## 2. Requirements

### 2.1. Developers

#### 2.1.1. Creating conda environment

A conda environment can be created by executing the following command:


```
conda env create -n PRTR -f environment.yml

```

The above command is written assuming that you are in the folder containing .yml file, i.e. the root folder PRTR_transfers. 

#### 2.1.2. Avoiding ModuleNotFoundError and ImportError<sup>[1](#myfootnote1)</sup>

If you are working as a Python developer, you should avoid both ```ModuleNotFoundError``` and ```ImportError``` (see the following [link](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c)). Thus, follow the steps below to solve the above mentioned problems:

<ol>
  <li>
    Run the following command in order to obtain the PRTR_transfers project location and then saving its path into the variable PACKAGE
    
    PACKAGE=$(locate -br '^PRTR_transfers$')
  </li>
  <li>
    Check the PACKAGE value by running the following command
    
    echo $PACKAGE
   </li>
   <li>
    Run the following command to add the PRTR_transfers project to the system paths
     
    export PYTHONPATH="${PYTHONPATH}:$PACKAGE"
   </li>
</ol>

If you prefer to save the path to the PRTR_transfers project folder as a permanent environment variable, follow these steps:

<ol>
   <li>
    Open the .bashrc file with the text editor of your preference (e.g., Visual Studio Code)
        
    code ~/.bashrc
   </li>
   <li>
    Scroll to the bottom of the file and add the following lines
       
    export PACKAGE=$(locate -br '^PRTR_transfers$')
    export PYTHONPATH="${PYTHONPATH}:$PACKAGE"
   </li>
   <li>
    Save the file with the changes
   </li>
   <li>
    You can open another terminal to verify that the variable has been successfully saved by running the following command
    
    echo $PYTHONPATH
   </li>
</ol>

<hr/>

#### 2.1.3. Installation of Relational Database Management System (RDMS)

The Extract, Transform, Load (ETL) procedure uses an Object–Relational Mapping (ORT) for data persistence by an RDMS. PostgreSQL and MySQL are the RDMS currently supported by the ETL. Thus, you must have installed any of these RDMSs to run the data engineering pipeline or the data-driven modeling module.

## 3. How to use

### 3.1. Data-driven module

#### 3.1.1. Data preparation

In order to run the data preparation, you should use the main.py file inside the [data_preparation](https://github.com/USEPA/PRTR-QSTR-models/tree/data-driven/data_driven/data_preparation) folder. Follow the following steps:

<ol>
   <li>
    In your terminal or command line, navigate to the data_engineering folder
   </li>
   <li>
    Run the following command

    python main.py --help
   </li>
   <li>
    You will see the following help menu

    usage: main.py [-h] [--rdbms RDBMS] [--password PASSWORD] [--username USERNAME] [--host HOST] [--port PORT] [--db_name DB_NAME]
                   [--sql_file SQL_FILE]

    optional arguments:
          -h, --help           show this help message and exit
          --rdbms {mysql,postgresql}
                               The Relational Database Management System (RDBMS) you would like to use
          --password PASSWORD  The password for using the RDBMS
          --username USERNAME  The username for using the RDBMS
          --host HOST          The computer hosting for the database
          --port PORT          Port used by the database engine
          --db_name DB_NAME    Database name
          --id                 What id would your like to use for the data preparation workflow
          --before_2005        Would you like to include data reported before 2005?
          --including_groups   Would you like to include the chemical groups
          --grouping_type      How you want to calculate descriptors for the chemical groups
          --flow_handling      How you want to handle the transfer flow rates
          --number_of_intervals How many intervals would you like to use for the transfer flow rates
          --output_column      What column would you like to keep as the classifier output
          --outliers_removal   Would you like to keep the outliers
          --balanaced_split    Would you like to obtain an stratified train-test split?
          --dimensionality_reduction What method for dimensionality reduction would you like to apply?. In this point, after encoding, we only apply feature      transformation by FAMD - Factor Analysis of Mixed Data or feature selection by UFS - Univariate Feature Selection with mutual infomation (filter method) or RFC - Random Forest Classifier (embedded method via feature importance)
          --balanced_dataset  Would you like to balance the dataset
          --classification_type What kind of classification problem would you like
          --target_class       If applied, What is the target class (only for multi-model binary classification)
          --input_file        Do you have an input file?
          --save_info          Would you like to save information?
          --data_fraction_to_use  What fraction of the data would you like to use?'
   </li>
   <li>
    You must indicate the value for each parameter. Each argument except <code>--password</code> has a default value (see the table below)
    
   |Argument|Default| Comment |
   |---|---|---|
   | rdbms | mysql | Only two options: MySQL and PostgreSQL |
   | username | root | root is the default username for MySQL. For PostgreSQL is postgres |
   | host | 127.0.0.1 | 127.0.0.1 (localhost) is the default host for MySQL. The same is for PostgreSQL |
   | port | 3306 | 3306 is the default port for MySQL. For PostgreSQL is 5432 |
   | db_name | PRTR_transfers | You are free to choose a name for the database |
   | id | 0 | You are free to choose an id for your workflow |
   | before_2005 | True |  |
   | including_groups | True |  |
   | grouping_type | 1 | <ol> <li> (1) mean value without outliers</li><li> (2) mean value with outliers</li><li> (3) median value</li><li> (4) min value</li><li> (5) max value</li><li> (6) random value</li><li> (7) random chemical</li><li> (8) keep chemicals (keep all chemicals having non-null records (95%))</li> </ol> |
   | flow_handling | 1 |  <ol><li> (1) Float values</li><li> (2) Integer values</li><li> (3) m balanced intervals split by quantiles</li><li> (4) m non-balanced equal-width intervals</li></ol> |
   | number_of_intervals | 10 | You are free to choose a value for your workflow |
   | output_column | generic | Whether you use the generic transfer classes as the model output or the waste managementh hiearchy categories |
   | outliers_removal | True |  |
   | balanaced_split | True |  |
   | dimensionality_reduction | True |  |
   | dimensionality_reduction_method | FAMD | Options: FAMD, UFS, and RFC |
   | balanced_dataset | True |  |
   | classification_type | multi-class classification | Options: multi-model binary classification, multi-label classification, and multi-class classification |
   | target_class | M1 | Options: M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, Disposal, Sewerage, Treatment, Energy recovery, and Recycling |
   | input_file | No | Look at the following sample file [data_preparations.xlsx](https://github.com/USEPA/PRTR-QSTR-models/blob/data-driven/data_driven/data_preparation/input/data_preparations.xlsx) |
   | save_info | No |  |
   | data_fraction_to_use | 1.0 | You are free to choose a value for your workflow |
   </li>
</ol>

##### 3.1.1.1. Data preparation (paper)

In the case of the data preparation pipelines that are part of the paper, you have to use the [.xlsx file](https://github.com/USEPA/PRTR-QSTR-models/blob/data-driven/data_driven/data_preparation/input/data_preparations.xlsx) and run the following command:

```
python main.py --rdbms postgresql --input_file Yes --save_info Yes --data_fraction_to_use 0.3 --password your-rdbms-password
```
<ul>
<li>In the command described above, it is assumed you are using PostgreSQL with default parameters (i.e., host, port, and username).</li>
<li>Replace your-rdbms-password with your PostgreSQL password.</li>
<li>The .zip file called [PRTR_transfers_v_PostgreSQL.zip](https://github.com/USEPA/PRTR-QSTR-models/blob/data-driven/data_engineering/load/output/PRTR_transfers_v_PostgreSQL.zip) will be used for creating the database schema and populating the tables.</li>
<li>To avoid the problem with disk space, you should upload the data to a cloud storage service like Google Drive, which will facilitate you to follow the modeling stage presented below.</li>
</ul>

#### 3.1.2. Modelling

For modelling, as a normal Data Science practice, you can check the [Jupyter Notebooks](https://github.com/USEPA/PRTR-QSTR-models/tree/data-driven/data_driven/modeling/notebooks) to run each experiment iteractively. Those notebooks call functions that are stored in the [scripts](https://github.com/USEPA/PRTR-QSTR-models/tree/data-driven/data_driven/modeling/scripts) folder. The input [folder](https://github.com/USEPA/PRTR-QSTR-models/tree/data-driven/data_driven/modeling/input) contains information used to set the model params both for building the base model and perform hyperparameter tuning. The [output](https://github.com/USEPA/PRTR-QSTR-models/tree/data-driven/data_driven/modeling/output) folder contains the results obtain during the modelling and optimization stages.

 
<hr/>

## 4. Notes

<a name="myfootnote1">1</a>: If you have troubles with this step, update ```updatedb```  by running ```sudo updatedb```.
