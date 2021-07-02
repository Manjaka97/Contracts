<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Manjaka97?tab=repositories">
    <img src="images/logo - black.svg" alt="Logo" width="250" height="50">
  </a>

  <h3 align="center">CONTRACTS BY ELVNOSIX</h3>

  <p align="center">
    A FAST AND EASY TO USE CONTRACTS MANAGEMENT SOFTWARE
    <br />
    <br />
    <a href="https://github.com/Manjaka97/Contracts/issues">Report Bug or Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Demo](#demo)
* [Installation](#installation)
* [Features](#features)
* [Built With](#built-with)
* [License](#license)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project

![product-screenshot]

Contracts by Elvnosix is a contracts management desktop application that is designed to greatly simplify a company or an individual's administrative duties by providing a fast, easy to use organizing tool for contracts, companies, contacts and risks. Take advantage of automation, quick document storage and retrieval, reminders for regular tasks or contracts key dates, quick search and filtering, and much more. Seamlessly export your data to a spreadsheet for further analysis and sharing. Have a look at a detailed list of features [here](#features).


<!-- DEMO -->
## Demo

![demo]

<!-- GETTING STARTED -->
## Installation

No installation needed. Simply download the Build folder, run contracts.exe  and start managing your contracts. Once you run contracts.exe the first time, please do not move the location of the build folder and its content.
(Alternatively, you can run the command 'python setup.py build' to build your own build directory, but you will need to copy the database file data.db from the original build directory to your own build directory)

N.B.: You can directly run contracts.py if you do not wish to use a .exe file. The database file data.db must be in the same directory as contracts.py and you must comment out line 31 in contracts.py.

<!-- FEATURES -->
## Features
### Create:
* Contracts
	* Save all the important information and details concerning your contract: Title, 13 types to choose from, 17 classifications for further precision, contract value, references, master contract, value, key dates, description and more.
	* Automatize the contract status using the provided key dates.
* People
	* Save all the involved parties and their contact information all in one place.
* Companies
	* Save involved companies details and contact information.
* Reminders
	* Create reminders to not miss any deadline and important dates.
	* Snooze or auto-renew your alerts depending on their nature.
* Risks
	* Generate risks associated with your contracts, organized by 5 possible classifications.
	* Define mitigation measures and severity of the risk based on probability and/or impact.
* To-Dos
	* Make a list of tasks for increased productivity. 
	* Rank your tasks by priority and/or severity.
### Link:
* Everything is connected to each other for a smooth management experience. 
* Each created contract can be associated to multiple created people. People can be associated with created companies. 
* Reminders can be associated with contracts to use the contracts key dates as reminder reference (e.g. 1 month after contract start date, 3 weeks before contract cancellation date, the day of contract review date, etc...)
* Each risk can be associated to the contract generating the risk
* Assign the task from your To-Dos to a created person for accountability.
### Store:
* Store any type of document or multiple documents with each contract, reminder and risk.
* Open your stored document from the app to directly open selected document in appropriate linked application.
* Search:
	* Mark anything you create as favorite from fast retrieval.
	* Filter down your view with handy filters based on creation date, archived status, active status, favorites, and many more. 
	* Quickly and precisely search anything by typing your search query in the bars provided for each category.
	* Search all stored documents from all contracts, reminders and risks using the library.
### Export:
* Export any of your data category to a .csv file for printing or analysis.
* You can export a single selected element or the entire view.
* You can also export with full details or summarized details depending on your needs.


<!-- BUILT WITH -->
## Built With

* [PyQt5](https://pypi.org/project/PyQt5/)
* [SQLite](https://www.sqlite.org/index.html)


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

* Manjaka Andriamasinoro 
* Email: manjaka.andriamasinoro@gmail.com / elvnosix@gmail.com
* LinkedIn: https://www.linkedin.com/in/manjaka-andriamasinoro/

* Project Link: [https://github.com/Manjaka97/Contracts/](https://github.com/Manjaka97/Contracts/)


<!-- MARKDOWN LINKS & IMAGES -->
[license-url]: https://github.com/Manjaka97/Contracts/blob/master/LICENSE
[linkedin-url]: https://www.linkedin.com/in/manjaka-andriamasinoro/
[product-screenshot]: images/screenshot.PNG
[demo]: images/demo.gif
